"""
Query Router — classifies natural language queries and routes to MCP servers.

This uses keyword-based classification as a temporary approach.
Replace with a real LLM call by swapping out llm_stub.py.
"""

import re
from typing import List, Tuple

ROUTING_RULES = {
    "library": {
        "keywords": [
            "book", "borrow", "return", "library", "read", "isbn", "shelf",
            "available", "checked out", "due date", "catalog", "reference",
            "textbook", "novel", "author", "title",
        ],
        "base_url": "http://localhost:8001",
    },
    "cafeteria": {
        "keywords": [
            "food", "menu", "lunch", "dinner", "breakfast", "cafeteria",
            "eat", "canteen", "meal", "snack", "veg", "non-veg", "price",
            "today's menu", "special", "calorie", "allergen", "hungry",
        ],
        "base_url": "http://localhost:8002",
    },
    "events": {
        "keywords": [
            "event", "fest", "club", "workshop", "hackathon", "competition",
            "seminar", "concert", "sports", "tournament", "registration",
            "cultural", "tech fest", "open mic", "lecture", "demo",
            "cricket", "basketball", "yoga", "debate",
        ],
        "base_url": "http://localhost:8003",
    },
    "academics": {
        "keywords": [
            "course", "class", "schedule", "syllabus", "deadline", "exam",
            "professor", "instructor", "assignment", "semester", "credit",
            "department", "curriculum", "timetable", "lab", "quiz",
            "project", "moodle", "placement", "handbook", "fee",
        ],
        "base_url": "http://localhost:8004",
    },
}


def classify_query(query: str) -> List[Tuple[str, str, float]]:
    """
    Classify a natural language query into one or more MCP server categories.
    Returns a list of (category, base_url, confidence) tuples sorted by confidence.
    """
    query_lower = query.lower()
    scores = {}

    for category, config in ROUTING_RULES.items():
        score = 0
        for keyword in config["keywords"]:
            # Use word boundary matching for single words, substring for phrases
            if " " in keyword:
                if keyword in query_lower:
                    score += 2  # Phrases get higher weight
            else:
                pattern = r'\b' + re.escape(keyword) + r'\b'
                matches = re.findall(pattern, query_lower)
                score += len(matches)

        if score > 0:
            scores[category] = (config["base_url"], score)

    if not scores:
        # Default: return all servers with low confidence
        return [
            (cat, config["base_url"], 0.1)
            for cat, config in ROUTING_RULES.items()
        ]

    max_score = max(s for _, s in scores.values())
    results = [
        (cat, url, round(score / max_score, 2))
        for cat, (url, score) in scores.items()
    ]

    return sorted(results, key=lambda x: x[2], reverse=True)


def get_server_url(category: str) -> str:
    """Get the base URL for a given MCP server category."""
    if category in ROUTING_RULES:
        return ROUTING_RULES[category]["base_url"]
    return None


def get_all_server_urls() -> dict:
    """Get all MCP server base URLs."""
    return {cat: config["base_url"] for cat, config in ROUTING_RULES.items()}
