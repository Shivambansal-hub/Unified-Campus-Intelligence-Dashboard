from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import data

app = FastAPI(
    title="MARS Cafeteria MCP Server",
    description="Model Context Protocol server for campus cafeteria menu data",
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
    return {"status": "healthy", "service": "cafeteria"}


@app.get("/menu/today")
async def get_today_menu():
    return data.get_today_menu()


@app.get("/menu/week")
async def get_week_menu():
    return data.get_week_menu()


@app.get("/menu/{meal_type}")
async def get_meal(meal_type: str):
    result = data.get_meal(meal_type)
    if not result:
        return {"error": f"Unknown meal type: {meal_type}. Use breakfast, lunch, dinner, or snacks."}
    return result


@app.get("/specials")
async def get_specials():
    return data.get_specials()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
