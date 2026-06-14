from pydantic import BaseModel
from typing import Optional
from datetime import date


class Book(BaseModel):
    id: int
    title: str
    author: str
    isbn: str
    category: str
    available: bool
    shelf_location: str
    total_copies: int
    available_copies: int
    due_date: Optional[date] = None
    cover_color: str = "#6C63FF"  # For UI display


class LibraryStats(BaseModel):
    total_books: int
    available_books: int
    checked_out: int
    categories: int
