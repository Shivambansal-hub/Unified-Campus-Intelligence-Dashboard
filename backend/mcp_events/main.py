from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import data

app = FastAPI(
    title="MARS Events MCP Server",
    description="Model Context Protocol server for campus events and clubs",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return {"status": "healthy", "service": "events"}


@app.get("/events")
async def get_events(
    club: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
):
    return data.get_all_events(club=club, category=category)


@app.get("/events/today")
async def get_today_events():
    return data.get_today_events()


@app.get("/events/this-week")
async def get_this_week_events():
    return data.get_this_week_events()


@app.get("/events/{event_id}")
async def get_event(event_id: int):
    event = data.get_event_by_id(event_id)
    if not event:
        return {"error": "Event not found"}
    return event


@app.get("/clubs")
async def get_clubs():
    return data.get_all_clubs()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
