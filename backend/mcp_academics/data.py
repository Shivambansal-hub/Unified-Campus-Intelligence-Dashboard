from datetime import date, timedelta
from models import Course, CourseSchedule, Deadline, Resource

_today = date.today()

COURSES = [
    Course(id=1, code="CS301", name="Data Structures & Algorithms", instructor="Dr. Ananya Sharma", credits=4, department="Computer Science", semester=5,
           schedule=[CourseSchedule(day="Monday", time="9:00 AM – 10:00 AM", room="LH-201"), CourseSchedule(day="Wednesday", time="9:00 AM – 10:00 AM", room="LH-201"), CourseSchedule(day="Friday", time="9:00 AM – 10:00 AM", room="LH-201"), CourseSchedule(day="Tuesday", time="2:00 PM – 4:00 PM", room="CS Lab 1", type="lab")],
           description="Advanced data structures, graph algorithms, dynamic programming, and complexity analysis.",
           prerequisites=["CS101", "MA201"]),
    Course(id=2, code="CS302", name="Operating Systems", instructor="Prof. Rajesh Kumar", credits=4, department="Computer Science", semester=5,
           schedule=[CourseSchedule(day="Monday", time="10:00 AM – 11:00 AM", room="LH-202"), CourseSchedule(day="Wednesday", time="10:00 AM – 11:00 AM", room="LH-202"), CourseSchedule(day="Thursday", time="10:00 AM – 11:00 AM", room="LH-202"), CourseSchedule(day="Thursday", time="2:00 PM – 4:00 PM", room="CS Lab 2", type="lab")],
           description="Process management, memory management, file systems, and concurrency.",
           prerequisites=["CS201"]),
    Course(id=3, code="CS303", name="Database Management Systems", instructor="Dr. Meera Patel", credits=3, department="Computer Science", semester=5,
           schedule=[CourseSchedule(day="Tuesday", time="9:00 AM – 10:00 AM", room="LH-203"), CourseSchedule(day="Thursday", time="9:00 AM – 10:00 AM", room="LH-203"), CourseSchedule(day="Wednesday", time="2:00 PM – 4:00 PM", room="CS Lab 3", type="lab")],
           description="Relational databases, SQL, normalization, transaction processing, and NoSQL.",
           prerequisites=["CS201"]),
    Course(id=4, code="CS304", name="Computer Networks", instructor="Dr. Vikram Desai", credits=3, department="Computer Science", semester=5,
           schedule=[CourseSchedule(day="Monday", time="11:00 AM – 12:00 PM", room="LH-204"), CourseSchedule(day="Wednesday", time="11:00 AM – 12:00 PM", room="LH-204"), CourseSchedule(day="Friday", time="2:00 PM – 4:00 PM", room="CS Lab 1", type="lab")],
           description="OSI model, TCP/IP, routing, network security, and socket programming.",
           prerequisites=["CS201"]),
    Course(id=5, code="CS401", name="Machine Learning", instructor="Dr. Sanjay Gupta", credits=4, department="Computer Science", semester=7,
           schedule=[CourseSchedule(day="Tuesday", time="10:00 AM – 11:30 AM", room="LH-301"), CourseSchedule(day="Thursday", time="10:00 AM – 11:30 AM", room="LH-301"), CourseSchedule(day="Friday", time="10:00 AM – 12:00 PM", room="CS Lab 4", type="lab")],
           description="Supervised learning, unsupervised learning, neural networks, and deep learning fundamentals.",
           prerequisites=["CS301", "MA301"]),
    Course(id=6, code="EE201", name="Circuit Theory", instructor="Dr. Priya Nair", credits=4, department="Electrical Engineering", semester=3,
           schedule=[CourseSchedule(day="Monday", time="9:00 AM – 10:00 AM", room="LH-105"), CourseSchedule(day="Wednesday", time="9:00 AM – 10:00 AM", room="LH-105"), CourseSchedule(day="Friday", time="9:00 AM – 10:00 AM", room="LH-105"), CourseSchedule(day="Monday", time="2:00 PM – 4:00 PM", room="EE Lab 1", type="lab")],
           description="Network theorems, AC/DC analysis, transient response, and filter design.",
           prerequisites=["PH101"]),
    Course(id=7, code="EE301", name="Digital Signal Processing", instructor="Prof. Arun Reddy", credits=3, department="Electrical Engineering", semester=5,
           schedule=[CourseSchedule(day="Tuesday", time="11:00 AM – 12:00 PM", room="LH-106"), CourseSchedule(day="Thursday", time="11:00 AM – 12:00 PM", room="LH-106"), CourseSchedule(day="Wednesday", time="2:00 PM – 4:00 PM", room="EE Lab 2", type="lab")],
           description="DFT, FFT, FIR/IIR filter design, and applications in audio/image processing.",
           prerequisites=["EE201", "MA201"]),
    Course(id=8, code="ME201", name="Thermodynamics", instructor="Dr. Karthik Iyer", credits=4, department="Mechanical Engineering", semester=3,
           schedule=[CourseSchedule(day="Monday", time="10:00 AM – 11:00 AM", room="LH-107"), CourseSchedule(day="Wednesday", time="10:00 AM – 11:00 AM", room="LH-107"), CourseSchedule(day="Friday", time="10:00 AM – 11:00 AM", room="LH-107")],
           description="Laws of thermodynamics, entropy, thermodynamic cycles, and applications.",
           prerequisites=["PH101", "MA101"]),
    Course(id=9, code="ME301", name="Fluid Mechanics", instructor="Dr. Suresh Menon", credits=3, department="Mechanical Engineering", semester=5,
           schedule=[CourseSchedule(day="Tuesday", time="9:00 AM – 10:00 AM", room="LH-108"), CourseSchedule(day="Thursday", time="9:00 AM – 10:00 AM", room="LH-108"), CourseSchedule(day="Tuesday", time="2:00 PM – 4:00 PM", room="ME Lab 1", type="lab")],
           description="Fluid statics, dynamics, Bernoulli's equation, viscous flow, and pipe flow.",
           prerequisites=["ME201", "MA201"]),
    Course(id=10, code="MA201", name="Probability & Statistics", instructor="Dr. Lakshmi Venkatesh", credits=3, department="Mathematics", semester=3,
           schedule=[CourseSchedule(day="Monday", time="11:00 AM – 12:00 PM", room="LH-109"), CourseSchedule(day="Wednesday", time="11:00 AM – 12:00 PM", room="LH-109"), CourseSchedule(day="Friday", time="11:00 AM – 12:00 PM", room="LH-109")],
           description="Probability distributions, hypothesis testing, regression, and Bayesian inference.",
           prerequisites=["MA101"]),
    Course(id=11, code="MA301", name="Linear Algebra", instructor="Dr. Ramesh Babu", credits=3, department="Mathematics", semester=5,
           schedule=[CourseSchedule(day="Tuesday", time="10:00 AM – 11:00 AM", room="LH-110"), CourseSchedule(day="Thursday", time="10:00 AM – 11:00 AM", room="LH-110")],
           description="Vector spaces, linear transformations, eigenvalues, SVD, and applications.",
           prerequisites=["MA101"]),
    Course(id=12, code="PH201", name="Quantum Mechanics I", instructor="Dr. Neha Joshi", credits=4, department="Physics", semester=3,
           schedule=[CourseSchedule(day="Monday", time="9:00 AM – 10:00 AM", room="LH-111"), CourseSchedule(day="Wednesday", time="9:00 AM – 10:00 AM", room="LH-111"), CourseSchedule(day="Friday", time="9:00 AM – 10:00 AM", room="LH-111"), CourseSchedule(day="Thursday", time="2:00 PM – 4:00 PM", room="PH Lab 1", type="lab")],
           description="Wave-particle duality, Schrödinger equation, hydrogen atom, and angular momentum.",
           prerequisites=["PH101", "MA201"]),
    Course(id=13, code="HS201", name="Technical Communication", instructor="Prof. Anita Roy", credits=2, department="Humanities", semester=3,
           schedule=[CourseSchedule(day="Friday", time="2:00 PM – 4:00 PM", room="LH-112")],
           description="Academic writing, presentation skills, report formatting, and research methodology."),
    Course(id=14, code="CS305", name="Software Engineering", instructor="Dr. Arjun Srinivasan", credits=3, department="Computer Science", semester=5,
           schedule=[CourseSchedule(day="Tuesday", time="11:00 AM – 12:00 PM", room="LH-205"), CourseSchedule(day="Thursday", time="11:00 AM – 12:00 PM", room="LH-205")],
           description="Software lifecycle, agile methodologies, testing, design patterns, and project management.",
           prerequisites=["CS201"]),
    Course(id=15, code="CS402", name="Cloud Computing", instructor="Dr. Pooja Hegde", credits=3, department="Computer Science", semester=7,
           schedule=[CourseSchedule(day="Monday", time="2:00 PM – 3:30 PM", room="LH-302"), CourseSchedule(day="Wednesday", time="2:00 PM – 3:30 PM", room="LH-302")],
           description="Virtualization, containers, cloud architectures (AWS/GCP), serverless computing, and DevOps.",
           prerequisites=["CS302", "CS304"]),
]

DEADLINES = [
    Deadline(id=1, title="DSA Assignment 3: Graph Algorithms", course_code="CS301", date=(_today + timedelta(days=3)).isoformat(), type="assignment", description="Implement BFS, DFS, Dijkstra, and Kruskal's algorithms. Submit on Moodle."),
    Deadline(id=2, title="OS Mid-Semester Exam", course_code="CS302", date=(_today + timedelta(days=10)).isoformat(), type="exam", description="Covers processes, threads, scheduling, and synchronization. Closed book."),
    Deadline(id=3, title="DBMS Project Proposal", course_code="CS303", date=(_today + timedelta(days=5)).isoformat(), type="project", description="Submit 1-page project proposal with ER diagram. Teams of 3."),
    Deadline(id=4, title="CN Lab Report 4", course_code="CS304", date=(_today + timedelta(days=2)).isoformat(), type="assignment", description="Socket programming lab report — TCP echo server implementation."),
    Deadline(id=5, title="ML Quiz 2", course_code="CS401", date=(_today + timedelta(days=7)).isoformat(), type="exam", description="Covers SVM, decision trees, and ensemble methods. 30 minutes, in-class."),
    Deadline(id=6, title="Semester Registration for Fall 2026", course_code="ADMIN", date=(_today + timedelta(days=14)).isoformat(), type="registration", description="Complete course registration for next semester on the portal."),
    Deadline(id=7, title="SE Group Project Milestone 1", course_code="CS305", date=(_today + timedelta(days=8)).isoformat(), type="project", description="SRS document and system architecture diagrams due."),
    Deadline(id=8, title="Probability Assignment 5", course_code="MA201", date=(_today + timedelta(days=4)).isoformat(), type="assignment", description="Hypothesis testing and confidence intervals. Problems 4.1–4.15."),
    Deadline(id=9, title="Cloud Computing Lab: Docker Containers", course_code="CS402", date=(_today + timedelta(days=6)).isoformat(), type="assignment", description="Containerize a microservice app with Docker and docker-compose."),
    Deadline(id=10, title="End-Semester Exam Period Begins", course_code="ADMIN", date=(_today + timedelta(days=30)).isoformat(), type="exam", description="End-semester exams begin. Check individual course schedules for specific dates."),
]

RESOURCES = [
    Resource(id=1, title="Student Handbook 2025-26", type="handbook", url="https://mars.edu/handbook2025.pdf", description="Complete guide to academic policies, rules, and regulations."),
    Resource(id=2, title="Academic Calendar 2025-26", type="document", url="https://mars.edu/calendar2025.pdf", description="Semester dates, holidays, exam schedules, and important deadlines."),
    Resource(id=3, title="Moodle LMS", type="link", url="https://moodle.mars.edu", description="Learning management system for assignments, materials, and grades."),
    Resource(id=4, title="Fee Payment Portal", type="link", url="https://fees.mars.edu", description="Online fee payment and receipt download."),
    Resource(id=5, title="Library E-Resources", type="link", url="https://library.mars.edu/e-resources", description="Access to IEEE Xplore, ACM DL, Springer, and other e-journals."),
    Resource(id=6, title="Anti-Ragging Form", type="form", url="https://mars.edu/anti-ragging-form", department="Student Affairs", description="Mandatory anti-ragging undertaking for all students."),
    Resource(id=7, title="Hostel Leave Application", type="form", url="https://mars.edu/hostel-leave", department="Hostel", description="Apply for hostel leave and outing passes online."),
    Resource(id=8, title="CS Department Curriculum", type="document", url="https://cs.mars.edu/curriculum.pdf", department="Computer Science", description="Complete B.Tech CS curriculum with course structure."),
    Resource(id=9, title="Scholarship Application", type="form", url="https://mars.edu/scholarships", department="Finance", description="Merit and need-based scholarship applications."),
    Resource(id=10, title="Placement Brochure 2026", type="document", url="https://placement.mars.edu/brochure2026.pdf", department="Placement Cell", description="Campus placement statistics, companies, and packages."),
]


def get_all_courses(department: str = None, semester: int = None):
    results = COURSES
    if department:
        results = [c for c in results if department.lower() in c.department.lower()]
    if semester:
        results = [c for c in results if c.semester == semester]
    return results


def get_course_by_code(code: str):
    for c in COURSES:
        if c.code.upper() == code.upper():
            return c
    return None


def get_schedule(department: str):
    courses = [c for c in COURSES if department.lower() in c.department.lower()]
    schedule = []
    for course in courses:
        for slot in course.schedule:
            schedule.append({
                "course_code": course.code,
                "course_name": course.name,
                "instructor": course.instructor,
                "day": slot.day,
                "time": slot.time,
                "room": slot.room,
                "type": slot.type,
            })
    return sorted(schedule, key=lambda s: (
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(s["day"]),
        s["time"],
    ))


def get_deadlines():
    return sorted(DEADLINES, key=lambda d: d.date)


def get_resources():
    return RESOURCES
