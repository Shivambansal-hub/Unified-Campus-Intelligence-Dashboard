from pydantic import BaseModel
from typing import List, Optional


class MenuItem(BaseModel):
    id: int
    name: str
    price: float
    is_veg: bool
    calories: int
    allergens: List[str] = []
    description: str = ""
    is_special: bool = False


class Meal(BaseModel):
    meal_type: str  # breakfast, lunch, dinner, snacks
    items: List[MenuItem]
    timing: str


class DayMenu(BaseModel):
    day: str
    date: str
    meals: List[Meal]
