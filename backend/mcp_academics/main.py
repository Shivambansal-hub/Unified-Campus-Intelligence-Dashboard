from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import data

app = FastAPI(
    title="MARS Academics MCP Server",
    description="Model Context Protocol server for academic courses, schedules, and resources",
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
    return {"status": "healthy", "service": "academics"}


@app.get("/courses")
async def get_courses(
    department: Optional[str] = Query(None),
    semester: Optional[int] = Query(None),
):
    return data.get_all_courses(department=department, semester=semester)


@app.get("/courses/{code}")
async def get_course(code: str):
    course = data.get_course_by_code(code)
    if not course:
        return {"error": f"Course {code} not found"}
    return course


@app.get("/schedule/{department}")
async def get_schedule(department: str):
    return data.get_schedule(department)


@app.get("/deadlines")
async def get_deadlines():
    return data.get_deadlines()


@app.get("/resources")
async def get_resources():
    return data.get_resources()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
