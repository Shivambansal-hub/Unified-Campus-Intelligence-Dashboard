from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import httpx
import os

from router import classify_query, get_server_url, get_all_server_urls
from llm_stub import generate_response

app = FastAPI(
    title="MARS API Gateway",
    description="Central gateway that routes queries to independent MCP servers",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── MCP server URLs (configurable via env vars for deployment) ──
MCP_URLS = {
    "library": os.getenv("MCP_LIBRARY_URL", "http://localhost:8001"),
    "cafeteria": os.getenv("MCP_CAFETERIA_URL", "http://localhost:8002"),
    "events": os.getenv("MCP_EVENTS_URL", "http://localhost:8003"),
    "academics": os.getenv("MCP_ACADEMICS_URL", "http://localhost:8004"),
}


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str
    sources: list
    query: str


# ── Health ──
@app.get("/health")
async def health():
    return {"status": "healthy", "service": "gateway"}


@app.get("/api/health/all")
async def health_all():
    """Check health of all MCP servers."""
    results = {}
    async with httpx.AsyncClient(timeout=5.0) as client:
        for name, url in MCP_URLS.items():
            try:
                resp = await client.get(f"{url}/health")
                results[name] = resp.json()
            except Exception as e:
                results[name] = {"status": "unreachable", "error": str(e)}
    return results


# ── AI Chat Endpoint ──
@app.post("/api/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    """
    Receives natural language, classifies intent, queries MCP server(s),
    and returns a formatted response.
    """
    query = req.message.strip()
    if not query:
        return ChatResponse(
            response="Please type a question! I can help with library, cafeteria, events, and academics.",
            sources=[],
            query=query,
        )

    # Classify which MCP servers to query
    classifications = classify_query(query)

    # Query relevant MCP servers (top matches with confidence > 0.3)
    relevant = [(cat, url) for cat, url, conf in classifications if conf > 0.3]
    if not relevant:
        # Fallback: use top match
        relevant = [(classifications[0][0], classifications[0][1])]

    context_data = {}
    sources_used = []

    async with httpx.AsyncClient(timeout=10.0) as client:
        for category, base_url in relevant:
            try:
                data = await _fetch_from_mcp(client, category, base_url, query)
                if data is not None:
                    context_data[category] = data
                    sources_used.append(category)
            except Exception as e:
                context_data[category] = {"error": str(e)}

    # Generate response using LLM stub
    response_text = await generate_response(query, context_data)

    return ChatResponse(
        response=response_text,
        sources=sources_used,
        query=query,
    )


async def _fetch_from_mcp(client: httpx.AsyncClient, category: str, base_url: str, query: str):
    """Fetch relevant data from an MCP server based on category and query."""
    query_lower = query.lower()

    if category == "library":
        # Try search if query has specific terms
        search_terms = _extract_search_terms(query_lower, ["book", "library", "available", "find", "search", "read", "borrow"])
        if search_terms:
            resp = await client.get(f"{base_url}/books", params={"q": search_terms})
        elif "available" in query_lower:
            resp = await client.get(f"{base_url}/books/available")
        elif "stat" in query_lower or "how many" in query_lower:
            resp = await client.get(f"{base_url}/stats")
        else:
            resp = await client.get(f"{base_url}/books")
        return resp.json()

    elif category == "cafeteria":
        if "special" in query_lower:
            resp = await client.get(f"{base_url}/specials")
        elif "week" in query_lower:
            resp = await client.get(f"{base_url}/menu/week")
        elif "breakfast" in query_lower:
            resp = await client.get(f"{base_url}/menu/breakfast")
        elif "dinner" in query_lower:
            resp = await client.get(f"{base_url}/menu/dinner")
        elif "snack" in query_lower:
            resp = await client.get(f"{base_url}/menu/snacks")
        elif "lunch" in query_lower:
            resp = await client.get(f"{base_url}/menu/lunch")
        else:
            resp = await client.get(f"{base_url}/menu/today")
        return resp.json()

    elif category == "events":
        if "today" in query_lower:
            resp = await client.get(f"{base_url}/events/today")
        elif "week" in query_lower:
            resp = await client.get(f"{base_url}/events/this-week")
        elif "club" in query_lower:
            resp = await client.get(f"{base_url}/clubs")
        else:
            # Check for category filter
            for cat in ["tech", "cultural", "sports", "academic"]:
                if cat in query_lower:
                    resp = await client.get(f"{base_url}/events", params={"category": cat})
                    return resp.json()
            resp = await client.get(f"{base_url}/events")
        return resp.json()

    elif category == "academics":
        if "deadline" in query_lower or "due" in query_lower or "assignment" in query_lower:
            resp = await client.get(f"{base_url}/deadlines")
        elif "schedule" in query_lower or "timetable" in query_lower:
            dept = _extract_department(query_lower)
            resp = await client.get(f"{base_url}/schedule/{dept}")
        elif "resource" in query_lower or "handbook" in query_lower or "form" in query_lower:
            resp = await client.get(f"{base_url}/resources")
        else:
            # Check for department filter
            dept_param = _extract_department(query_lower)
            if dept_param and dept_param != "computer":
                resp = await client.get(f"{base_url}/courses", params={"department": dept_param})
            else:
                resp = await client.get(f"{base_url}/courses")
        return resp.json()

    return None


def _extract_search_terms(query: str, stop_words: list) -> str:
    """Extract meaningful search terms from a query, removing common stop words."""
    words = query.split()
    generic_stops = {"what", "where", "when", "how", "is", "are", "the", "a", "an",
                     "can", "i", "me", "my", "do", "does", "any", "about", "for",
                     "in", "on", "at", "to", "of", "and", "or", "there", "tell",
                     "show", "get", "list", "give", "please", "?", "want"}
    all_stops = generic_stops | set(stop_words)
    terms = [w for w in words if w not in all_stops and len(w) > 2]
    return " ".join(terms) if terms else ""


def _extract_department(query: str) -> str:
    """Extract department name from query."""
    dept_map = {
        "cs": "computer",
        "computer science": "computer",
        "computer": "computer",
        "ee": "electrical",
        "electrical": "electrical",
        "electronics": "electrical",
        "me": "mechanical",
        "mechanical": "mechanical",
        "math": "mathematics",
        "maths": "mathematics",
        "mathematics": "mathematics",
        "physics": "physics",
        "humanities": "humanities",
    }
    for key, value in dept_map.items():
        if key in query:
            return value
    return "computer"  # default


# ── Proxy Endpoints for structured API access ──

@app.get("/api/library/{path:path}")
async def proxy_library(path: str, request: Request):
    async with httpx.AsyncClient(timeout=10.0) as client:
        url = f"{MCP_URLS['library']}/{path}"
        params = dict(request.query_params)
        resp = await client.get(url, params=params)
        return resp.json()


@app.get("/api/cafeteria/{path:path}")
async def proxy_cafeteria(path: str, request: Request):
    async with httpx.AsyncClient(timeout=10.0) as client:
        url = f"{MCP_URLS['cafeteria']}/{path}"
        params = dict(request.query_params)
        resp = await client.get(url, params=params)
        return resp.json()


@app.get("/api/events/{path:path}")
async def proxy_events(path: str, request: Request):
    async with httpx.AsyncClient(timeout=10.0) as client:
        url = f"{MCP_URLS['events']}/{path}"
        params = dict(request.query_params)
        resp = await client.get(url, params=params)
        return resp.json()


@app.get("/api/academics/{path:path}")
async def proxy_academics(path: str, request: Request):
    async with httpx.AsyncClient(timeout=10.0) as client:
        url = f"{MCP_URLS['academics']}/{path}"
        params = dict(request.query_params)
        resp = await client.get(url, params=params)
        return resp.json()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
