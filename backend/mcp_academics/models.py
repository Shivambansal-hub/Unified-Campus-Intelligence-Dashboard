from pydantic import BaseModel
from typing import List, Optional


class CourseSchedule(BaseModel):
    day: str
    time: str
    room: str
    type: str = "lecture"  # lecture, lab, tutorial


class Course(BaseModel):
    id: int
    code: str
    name: str
    instructor: str
    credits: int
    department: str
    semester: int
    schedule: List[CourseSchedule]
    description: str = ""
    prerequisites: List[str] = []


class Deadline(BaseModel):
    id: int
    title: str
    course_code: str
    date: str
    type: str  # assignment, exam, project, registration
    description: str = ""


class Resource(BaseModel):
    id: int
    title: str
    type: str  # handbook, form, link, document
    url: str
    department: str = "General"
    description: str = ""
