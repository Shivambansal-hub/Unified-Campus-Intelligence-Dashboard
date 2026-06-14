from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import data

app = FastAPI(
    title="MARS Library MCP Server",
    description="Model Context Protocol server for campus library data",
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
    return {"status": "healthy", "service": "library"}


@app.get("/books")
async def get_books(q: Optional[str] = Query(None, description="Search query")):
    if q:
        return data.search_books(q)
    return data.get_all_books()


@app.get("/books/available")
async def get_available_books():
    return data.get_available_books()


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    book = data.get_book_by_id(book_id)
    if not book:
        return {"error": "Book not found"}
    return book


@app.get("/stats")
async def get_stats():
    return data.get_stats()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
