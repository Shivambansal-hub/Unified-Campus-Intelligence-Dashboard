"""
LLM Stub — temporary response formatter.

This module formats raw MCP server data into conversational responses.
To integrate a real LLM (OpenAI, Gemini, Claude), replace the
`generate_response` function below. The interface is:

    async def generate_response(query: str, context_data: dict) -> str

Where:
    - query: the user's original natural language question
    - context_data: dict with keys like {"library": [...], "cafeteria": [...]}
      containing raw data fetched from MCP servers

Returns:
    A formatted string response for the chat UI.
"""

import os
import json
import logging
import httpx
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)


async def generate_response(query: str, context_data: Dict[str, Any]) -> str:
    """
    Generate a conversational response using Google Gemini API.
    Falls back to basic template formatting if API fails or key is missing.
    """
    if not context_data:
        return "I'm sorry, I couldn't find any relevant information for your query. Could you try rephrasing? You can ask me about:\n\n📚 **Library** — book availability, search\n🍽️ **Cafeteria** — today's menu, specials\n📅 **Events** — upcoming events, clubs\n📖 **Academics** — courses, deadlines, schedules"

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logger.warning("GEMINI_API_KEY environment variable not set. Falling back to template formatter.")
        return _fallback_format_response(query, context_data)

    context_str = json.dumps(context_data, default=str, indent=2)
    prompt = f"""You are MARS, a helpful campus AI assistant for students.
You have access to the following real-time data from various campus systems:
{context_str}

The student asked: "{query}"

Please provide a helpful, concise, and friendly response using ONLY the data provided above.
Format your response nicely using markdown (e.g., bullet points, bold text).
If the provided data contains an error or is empty, gracefully let the student know.
Do not mention the "context data" or "JSON" directly to the student.
"""

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}",
                json={
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }]
                },
                timeout=45.0
            )
            resp.raise_for_status()
            data = resp.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        logger.warning(f"Gemini API failed ({e}). Falling back to template formatter.")
        return _fallback_format_response(query, context_data)


def _fallback_format_response(query: str, context_data: Dict[str, Any]) -> str:
    responses = []

    for source, data in context_data.items():
        if not data:
            continue

        try:
            if source == "library":
                result = _format_library(data, query)
            elif source == "cafeteria":
                result = _format_cafeteria(data, query)
            elif source == "events":
                result = _format_events(data, query)
            elif source == "academics":
                result = _format_academics(data, query)
            else:
                result = None

            if result:
                responses.append(result)
        except Exception as e:
            responses.append(f"⚠️ Error formatting {source} data: {str(e)}")

    if not responses:
        # Fallback: show raw data summary
        summaries = []
        for source, data in context_data.items():
            if isinstance(data, list):
                summaries.append(f"**{source}**: {len(data)} results found")
            elif isinstance(data, dict):
                summaries.append(f"**{source}**: data retrieved")
        if summaries:
            return "I found some data but had trouble formatting it:\n• " + "\n• ".join(summaries)
        return "I found some data but couldn't format a useful response. Try asking something more specific!"

    return "\n\n".join(responses)


def _format_library(data: Any, query: str) -> str:
    if isinstance(data, dict) and "total_books" in data:
        return f"📚 **Library Stats**\n• Total books: {data['total_books']}\n• Available: {data['available_books']}\n• Checked out: {data['checked_out']}\n• Categories: {data['categories']}"

    if isinstance(data, list):
        if not data:
            return "📚 No books found matching your search."
        books = data[:5]
        lines = ["📚 **Library Results:**"]
        for b in books:
            status = "✅ Available" if b.get("available") else f"❌ Due back {b.get('due_date', 'soon')}"
            lines.append(f"• **{b['title']}** by {b['author']} — {status} (Shelf: {b.get('shelf_location', 'N/A')})")
        if len(data) > 5:
            lines.append(f"_...and {len(data) - 5} more results_")
        return "\n".join(lines)

    return f"📚 **Library:** {json.dumps(data, default=str)[:300]}"


def _format_cafeteria(data: Any, query: str) -> str:
    if isinstance(data, dict) and "meals" in data:
        day = data.get("day", "Today")
        meals = data["meals"]
        lines = [f"🍽️ **{day}'s Menu:**"]

        for meal_type in ["breakfast", "lunch", "dinner", "snacks"]:
            meal = meals.get(meal_type)
            if meal:
                items_data = meal.get("items", []) if isinstance(meal, dict) else (meal.items if hasattr(meal, 'items') else [])
                timing = meal.get("timing", "") if isinstance(meal, dict) else (meal.timing if hasattr(meal, 'timing') else "")
                lines.append(f"\n**{meal_type.capitalize()}** ({timing}):")
                for item in items_data[:4]:
                    name = item.get("name", item.name) if isinstance(item, dict) else item.name
                    price = item.get("price", item.price) if isinstance(item, dict) else item.price
                    is_veg = item.get("is_veg", item.is_veg) if isinstance(item, dict) else item.is_veg
                    badge = "🟢" if is_veg else "🔴"
                    lines.append(f"  {badge} {name} — ₹{price}")

        return "\n".join(lines)

    if isinstance(data, dict) and "specials" in data:
        specials = data["specials"]
        if not specials:
            return "🍽️ No specials today."
        lines = [f"🍽️ **Today's Specials ({data.get('day', '')}):**"]
        for s in specials:
            item = s.get("item", {})
            name = item.get("name", item.name) if isinstance(item, dict) else item.name
            price = item.get("price", item.price) if isinstance(item, dict) else item.price
            lines.append(f"• ⭐ **{name}** — ₹{price} ({s.get('meal_type', '')} @ {s.get('timing', '')})")
        return "\n".join(lines)

    return f"🍽️ **Cafeteria:** Got menu data."


def _format_events(data: Any, query: str) -> str:
    if isinstance(data, list):
        if not data:
            return "📅 No upcoming events found."
        events = data[:5]
        lines = ["📅 **Upcoming Events:**"]
        for e in events:
            title = e.get("title", "")
            club = e.get("club", "")
            evt_date = e.get("date", "")
            time = e.get("time", "")
            venue = e.get("venue", "")
            category = e.get("category", "")
            emoji_map = {"tech": "💻", "cultural": "🎭", "sports": "🏆", "academic": "🎓", "social": "🤝"}
            emoji = emoji_map.get(category, "📅")
            lines.append(f"• {emoji} **{title}** ({club})\n  📍 {venue} | 🗓️ {evt_date} @ {time}")
        if len(data) > 5:
            lines.append(f"_...and {len(data) - 5} more events_")
        return "\n".join(lines)

    return f"📅 **Events:** {json.dumps(data, default=str)[:300]}"


def _format_academics(data: Any, query: str) -> str:
    if isinstance(data, list) and data:
        first = data[0]

        # Deadlines
        if isinstance(first, dict) and "course_code" in first and "type" in first:
            lines = ["📖 **Upcoming Deadlines:**"]
            for d in data[:5]:
                type_emoji = {"assignment": "📝", "exam": "📋", "project": "🗂️", "registration": "📌"}.get(d.get("type", ""), "📌")
                lines.append(f"• {type_emoji} **{d['title']}** ({d['course_code']})\n  📅 Due: {d['date']} — {d.get('description', '')[:60]}")
            return "\n".join(lines)

        # Courses
        if isinstance(first, dict) and "code" in first:
            lines = ["📖 **Courses:**"]
            for c in data[:5]:
                lines.append(f"• **{c['code']}** — {c['name']} ({c['instructor']}, {c['credits']} credits)")
            if len(data) > 5:
                lines.append(f"_...and {len(data) - 5} more courses_")
            return "\n".join(lines)

        # Schedule
        if isinstance(first, dict) and "day" in first and "time" in first and "room" in first:
            lines = ["📖 **Class Schedule:**"]
            current_day = ""
            for s in data[:10]:
                if s["day"] != current_day:
                    current_day = s["day"]
                    lines.append(f"\n**{current_day}:**")
                type_badge = "🔬" if s.get("type") == "lab" else "📚"
                lines.append(f"  {type_badge} {s['time']} — {s['course_code']} {s['course_name']} @ {s['room']}")
            return "\n".join(lines)

        # Resources
        if isinstance(first, dict) and "url" in first:
            lines = ["📖 **Academic Resources:**"]
            for r in data[:5]:
                lines.append(f"• 📄 **{r['title']}** — {r.get('description', '')[:60]}")
            return "\n".join(lines)

    return f"📖 **Academics:** {json.dumps(data, default=str)[:300]}"
