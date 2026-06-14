from datetime import date, timedelta
from models import Event, Club

_today = date.today()

EVENTS = [
    Event(id=1, title="HackMars 2026 — 36-Hour Hackathon", club="CodeCraft Club", date=(_today + timedelta(days=3)).isoformat(), time="10:00 AM – (next day) 10:00 PM", venue="Main Auditorium & CS Labs", description="Annual flagship hackathon. Build innovative solutions in 36 hours. Prizes worth ₹50,000. Teams of 2-4.", category="tech", registration_link="https://hackmars2026.devfolio.co", is_free=True, max_participants=200, current_registrations=142, tags=["hackathon", "coding", "prizes"]),
    Event(id=2, title="AI/ML Workshop: Intro to Transformers", club="AI Society", date=(_today + timedelta(days=1)).isoformat(), time="2:00 PM – 5:00 PM", venue="Seminar Hall B", description="Hands-on workshop on transformer architectures. Bring your laptop. Prerequisites: basic Python and linear algebra.", category="tech", registration_link="https://forms.google.com/ai-workshop", is_free=True, max_participants=60, current_registrations=48, tags=["AI", "ML", "workshop", "transformers"]),
    Event(id=3, title="Open Mic Night", club="Dramatics Society", date=(_today + timedelta(days=2)).isoformat(), time="7:00 PM – 10:00 PM", venue="Open Air Theatre", description="Poetry, standup comedy, music — anything goes! Sign up at the venue or pre-register. Snacks provided.", category="cultural", is_free=True, tags=["open mic", "poetry", "comedy", "music"]),
    Event(id=4, title="Inter-Department Cricket Tournament", club="Sports Committee", date=(_today + timedelta(days=5)).isoformat(), time="8:00 AM – 6:00 PM", venue="Cricket Ground", description="T20 format. All departments invited. Register your team of 11+3 subs by Thursday.", category="sports", registration_link="https://forms.google.com/cricket-tourney", is_free=True, max_participants=120, current_registrations=88, tags=["cricket", "sports", "tournament"]),
    Event(id=5, title="Guest Lecture: Future of Quantum Computing", club="Physics Society", date=(_today + timedelta(days=4)).isoformat(), time="3:00 PM – 4:30 PM", venue="LH-301", description="Dr. Priya Sharma from IISc Bangalore discusses the current state and future of quantum computing. Open to all.", category="academic", is_free=True, tags=["quantum computing", "guest lecture", "physics"]),
    Event(id=6, title="Photography Walk: Campus Golden Hour", club="Shutterbugs Club", date=(_today + timedelta(days=1)).isoformat(), time="5:00 PM – 7:00 PM", venue="Meet at Library Entrance", description="Capture the campus during golden hour. All skill levels welcome. Bring any camera or smartphone.", category="cultural", is_free=True, tags=["photography", "outdoor", "creative"]),
    Event(id=7, title="Web Dev Bootcamp: React + FastAPI", club="CodeCraft Club", date=(_today + timedelta(days=6)).isoformat(), time="10:00 AM – 4:00 PM", venue="CS Lab 2", description="Full-day bootcamp on building full-stack apps with React frontend and FastAPI backend. Lunch provided.", category="tech", registration_link="https://forms.google.com/webdev-bootcamp", is_free=False, fee=100, max_participants=40, current_registrations=35, tags=["web dev", "React", "FastAPI", "bootcamp"]),
    Event(id=8, title="Book Club: 'Sapiens' Discussion", club="Literary Circle", date=(_today + timedelta(days=2)).isoformat(), time="5:00 PM – 6:30 PM", venue="Library Reading Room", description="Monthly book club discussion. This month: Sapiens by Yuval Noah Harari. Read at least the first 100 pages.", category="cultural", is_free=True, tags=["book club", "reading", "discussion"]),
    Event(id=9, title="Resume Building Workshop", club="Placement Cell", date=(_today + timedelta(days=7)).isoformat(), time="11:00 AM – 1:00 PM", venue="Seminar Hall A", description="Learn to build ATS-friendly resumes. Bring your laptop with your current resume draft.", category="academic", is_free=True, tags=["placement", "resume", "career"]),
    Event(id=10, title="Startup Pitch Night", club="E-Cell", date=(_today + timedelta(days=8)).isoformat(), time="6:00 PM – 9:00 PM", venue="Innovation Hub", description="5 student startups pitch to a panel of investors and mentors. Networking dinner after. Open to audience.", category="tech", is_free=True, tags=["startup", "entrepreneurship", "pitch"]),
    Event(id=11, title="Yoga & Meditation Session", club="Wellness Committee", date=(_today).isoformat(), time="6:30 AM – 7:30 AM", venue="Sports Complex Lawn", description="Start your day with guided yoga and meditation. Mats provided. All fitness levels welcome.", category="sports", is_free=True, tags=["yoga", "meditation", "wellness"]),
    Event(id=12, title="Robotics Demo Day", club="Robotics Club", date=(_today + timedelta(days=4)).isoformat(), time="10:00 AM – 1:00 PM", venue="Mechanical Workshop", description="See student-built robots in action! Line-followers, drones, and a new humanoid prototype.", category="tech", is_free=True, tags=["robotics", "demo", "engineering"]),
    Event(id=13, title="Classical Music Evening: Raga Night", club="Music Society", date=(_today + timedelta(days=3)).isoformat(), time="7:30 PM – 9:30 PM", venue="Open Air Theatre", description="An evening of Indian classical music featuring sitar, tabla, and vocal performances by students.", category="cultural", is_free=True, tags=["music", "classical", "performance"]),
    Event(id=14, title="Competitive Programming Contest", club="CodeCraft Club", date=(_today + timedelta(days=5)).isoformat(), time="3:00 PM – 6:00 PM", venue="CS Lab 1", description="Solve algorithmic challenges on Codeforces. Individual contest. Prizes for top 3.", category="tech", registration_link="https://codeforces.com/gym/mars-cp", is_free=True, max_participants=80, current_registrations=52, tags=["competitive programming", "algorithms", "contest"]),
    Event(id=15, title="Blood Donation Camp", club="NSS Unit", date=(_today + timedelta(days=6)).isoformat(), time="9:00 AM – 3:00 PM", venue="Health Center", description="Annual blood donation drive in collaboration with Red Cross. Refreshments provided for donors.", category="social", is_free=True, tags=["blood donation", "social", "health"]),
    Event(id=16, title="Film Screening: Interstellar", club="Film Society", date=(_today + timedelta(days=2)).isoformat(), time="8:00 PM – 11:00 PM", venue="LH-101 (Big Screen)", description="Monthly movie night. This month: Interstellar (2014). Popcorn and drinks on sale.", category="cultural", is_free=True, tags=["movie", "screening", "sci-fi"]),
    Event(id=17, title="Arduino Workshop for Beginners", club="Electronics Club", date=(_today + timedelta(days=7)).isoformat(), time="2:00 PM – 5:00 PM", venue="ECE Lab 3", description="Learn the basics of Arduino programming and circuit design. Components provided.", category="tech", registration_link="https://forms.google.com/arduino-ws", is_free=False, fee=50, max_participants=30, current_registrations=22, tags=["Arduino", "electronics", "workshop"]),
    Event(id=18, title="Debate: AI Ethics in Education", club="Debating Society", date=(_today + timedelta(days=3)).isoformat(), time="4:00 PM – 6:00 PM", venue="Seminar Hall A", description="Formal parliamentary debate on the use of AI tools in academic assessment. Spectators welcome.", category="academic", is_free=True, tags=["debate", "AI", "ethics", "education"]),
    Event(id=19, title="Basketball 3v3 Tournament", club="Sports Committee", date=(_today + timedelta(days=9)).isoformat(), time="4:00 PM – 8:00 PM", venue="Basketball Court", description="3v3 streetball tournament. Register teams of 3+1 sub.", category="sports", registration_link="https://forms.google.com/bball-3v3", is_free=True, max_participants=48, current_registrations=32, tags=["basketball", "tournament", "3v3"]),
    Event(id=20, title="Annual Cultural Fest: Spectrum 2026", club="Cultural Committee", date=(_today + timedelta(days=14)).isoformat(), time="All Day", venue="Entire Campus", description="3-day cultural extravaganza with music, dance, art, fashion show, and pro-night headliner. Get ready!", category="cultural", registration_link="https://spectrum2026.mars.edu", is_free=False, fee=200, max_participants=2000, current_registrations=856, tags=["cultural fest", "music", "dance", "fashion"]),
]

CLUBS = [
    Club(id=1, name="CodeCraft Club", category="tech", description="Competitive programming, hackathons, and software development", member_count=180, contact_email="codecraft@mars.edu"),
    Club(id=2, name="AI Society", category="tech", description="Artificial intelligence, machine learning, and data science", member_count=120, contact_email="ai.society@mars.edu"),
    Club(id=3, name="Robotics Club", category="tech", description="Building robots, drones, and autonomous systems", member_count=75, contact_email="robotics@mars.edu"),
    Club(id=4, name="Electronics Club", category="tech", description="Circuit design, IoT, embedded systems, and Arduino projects", member_count=65, contact_email="electronics@mars.edu"),
    Club(id=5, name="Dramatics Society", category="cultural", description="Theatre, street plays, and creative performances", member_count=90, contact_email="drama@mars.edu"),
    Club(id=6, name="Music Society", category="cultural", description="Band, choir, classical music, and jam sessions", member_count=110, contact_email="music@mars.edu"),
    Club(id=7, name="Shutterbugs Club", category="cultural", description="Photography, videography, and visual storytelling", member_count=85, contact_email="shutterbugs@mars.edu"),
    Club(id=8, name="Literary Circle", category="cultural", description="Book clubs, creative writing, poetry, and spoken word", member_count=50, contact_email="literary@mars.edu"),
    Club(id=9, name="Film Society", category="cultural", description="Filmmaking, screenings, and cinema appreciation", member_count=70, contact_email="films@mars.edu"),
    Club(id=10, name="Sports Committee", category="sports", description="Organizing inter-department and inter-college sports events", member_count=60, contact_email="sports@mars.edu"),
    Club(id=11, name="E-Cell", category="tech", description="Entrepreneurship, startups, and business plan competitions", member_count=95, contact_email="ecell@mars.edu"),
    Club(id=12, name="Debating Society", category="academic", description="Parliamentary debates, MUNs, and public speaking", member_count=55, contact_email="debate@mars.edu"),
    Club(id=13, name="NSS Unit", category="social", description="National Service Scheme — community service and social work", member_count=150, contact_email="nss@mars.edu"),
    Club(id=14, name="Wellness Committee", category="sports", description="Yoga, meditation, mental health awareness, and fitness", member_count=40, contact_email="wellness@mars.edu"),
    Club(id=15, name="Placement Cell", category="academic", description="Career guidance, mock interviews, and placement preparation", member_count=30, contact_email="placement@mars.edu"),
]


def get_all_events(club: str = None, category: str = None):
    results = EVENTS
    if club:
        results = [e for e in results if club.lower() in e.club.lower()]
    if category:
        results = [e for e in results if e.category.lower() == category.lower()]
    return sorted(results, key=lambda e: e.date)


def get_event_by_id(event_id: int):
    for e in EVENTS:
        if e.id == event_id:
            return e
    return None


def get_today_events():
    today_str = _today.isoformat()
    return [e for e in EVENTS if e.date == today_str]


def get_this_week_events():
    week_end = _today + timedelta(days=7)
    return sorted(
        [e for e in EVENTS if _today.isoformat() <= e.date <= week_end.isoformat()],
        key=lambda e: e.date,
    )


def get_all_clubs():
    return CLUBS
