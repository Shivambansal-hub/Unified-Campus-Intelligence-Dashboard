from datetime import date, timedelta
from models import Book

BOOKS = [
    Book(id=1, title="Introduction to Algorithms", author="Thomas H. Cormen", isbn="978-0262033848", category="Computer Science", available=True, shelf_location="CS-A3-12", total_copies=5, available_copies=3, cover_color="#6C63FF"),
    Book(id=2, title="Clean Code", author="Robert C. Martin", isbn="978-0132350884", category="Computer Science", available=True, shelf_location="CS-A2-07", total_copies=4, available_copies=2, cover_color="#FF6B6B"),
    Book(id=3, title="Design Patterns", author="Erich Gamma et al.", isbn="978-0201633610", category="Computer Science", available=False, shelf_location="CS-A1-15", total_copies=3, available_copies=0, due_date=date.today() + timedelta(days=5), cover_color="#4ECDC4"),
    Book(id=4, title="The Pragmatic Programmer", author="David Thomas & Andrew Hunt", isbn="978-0135957059", category="Computer Science", available=True, shelf_location="CS-B1-03", total_copies=3, available_copies=1, cover_color="#45B7D1"),
    Book(id=5, title="Structure and Interpretation of Computer Programs", author="Harold Abelson", isbn="978-0262510875", category="Computer Science", available=True, shelf_location="CS-B2-11", total_copies=2, available_copies=2, cover_color="#96CEB4"),
    Book(id=6, title="Artificial Intelligence: A Modern Approach", author="Stuart Russell & Peter Norvig", isbn="978-0134610993", category="Computer Science", available=False, shelf_location="CS-C1-01", total_copies=4, available_copies=0, due_date=date.today() + timedelta(days=12), cover_color="#FFEAA7"),
    Book(id=7, title="Computer Networking: A Top-Down Approach", author="James Kurose", isbn="978-0133594140", category="Computer Science", available=True, shelf_location="CS-C2-08", total_copies=3, available_copies=2, cover_color="#DDA0DD"),
    Book(id=8, title="Fundamentals of Physics", author="David Halliday & Robert Resnick", isbn="978-1118230718", category="Physics", available=True, shelf_location="PH-A1-04", total_copies=6, available_copies=4, cover_color="#FF8A5C"),
    Book(id=9, title="Concepts of Modern Physics", author="Arthur Beiser", isbn="978-0072448481", category="Physics", available=True, shelf_location="PH-A2-09", total_copies=3, available_copies=1, cover_color="#A8E6CF"),
    Book(id=10, title="Classical Mechanics", author="Herbert Goldstein", isbn="978-0201657029", category="Physics", available=False, shelf_location="PH-B1-06", total_copies=2, available_copies=0, due_date=date.today() + timedelta(days=3), cover_color="#FFD93D"),
    Book(id=11, title="Linear Algebra Done Right", author="Sheldon Axler", isbn="978-3319110790", category="Mathematics", available=True, shelf_location="MA-A1-02", total_copies=4, available_copies=3, cover_color="#6C5CE7"),
    Book(id=12, title="Calculus", author="James Stewart", isbn="978-1285740621", category="Mathematics", available=True, shelf_location="MA-A2-10", total_copies=5, available_copies=4, cover_color="#00CEC9"),
    Book(id=13, title="Probability and Statistics for Engineering", author="Jay Devore", isbn="978-1305251809", category="Mathematics", available=True, shelf_location="MA-B1-05", total_copies=3, available_copies=2, cover_color="#E17055"),
    Book(id=14, title="Discrete Mathematics and Its Applications", author="Kenneth Rosen", isbn="978-0073383095", category="Mathematics", available=False, shelf_location="MA-B2-14", total_copies=3, available_copies=0, due_date=date.today() + timedelta(days=8), cover_color="#FDCB6E"),
    Book(id=15, title="To Kill a Mockingbird", author="Harper Lee", isbn="978-0061120084", category="Literature", available=True, shelf_location="LT-A1-01", total_copies=4, available_copies=3, cover_color="#E84393"),
    Book(id=16, title="1984", author="George Orwell", isbn="978-0451524935", category="Literature", available=True, shelf_location="LT-A1-03", total_copies=3, available_copies=2, cover_color="#636E72"),
    Book(id=17, title="The Great Gatsby", author="F. Scott Fitzgerald", isbn="978-0743273565", category="Literature", available=True, shelf_location="LT-A2-07", total_copies=2, available_copies=1, cover_color="#00B894"),
    Book(id=18, title="Sapiens: A Brief History of Humankind", author="Yuval Noah Harari", isbn="978-0062316097", category="Literature", available=False, shelf_location="LT-B1-02", total_copies=3, available_copies=0, due_date=date.today() + timedelta(days=15), cover_color="#0984E3"),
    Book(id=19, title="Engineering Mechanics: Statics", author="J.L. Meriam", isbn="978-1119392620", category="Engineering", available=True, shelf_location="EN-A1-06", total_copies=4, available_copies=2, cover_color="#F39C12"),
    Book(id=20, title="Thermodynamics: An Engineering Approach", author="Yunus Cengel", isbn="978-0073398174", category="Engineering", available=True, shelf_location="EN-A2-11", total_copies=3, available_copies=1, cover_color="#2ECC71"),
    Book(id=21, title="Digital Design", author="M. Morris Mano", isbn="978-0134549897", category="Engineering", available=True, shelf_location="EN-B1-04", total_copies=3, available_copies=2, cover_color="#9B59B6"),
    Book(id=22, title="Signals and Systems", author="Alan V. Oppenheim", isbn="978-0138147570", category="Engineering", available=False, shelf_location="EN-B2-13", total_copies=2, available_copies=0, due_date=date.today() + timedelta(days=6), cover_color="#1ABC9C"),
    Book(id=23, title="Operating System Concepts", author="Abraham Silberschatz", isbn="978-1119800361", category="Computer Science", available=True, shelf_location="CS-D1-02", total_copies=4, available_copies=3, cover_color="#E74C3C"),
    Book(id=24, title="Database System Concepts", author="Abraham Silberschatz", isbn="978-0078022159", category="Computer Science", available=True, shelf_location="CS-D2-09", total_copies=3, available_copies=1, cover_color="#3498DB"),
    Book(id=25, title="Computer Organization and Design", author="David Patterson", isbn="978-0124077263", category="Computer Science", available=True, shelf_location="CS-D3-15", total_copies=3, available_copies=2, cover_color="#F1C40F"),
    Book(id=26, title="Machine Learning", author="Tom M. Mitchell", isbn="978-0070428072", category="Computer Science", available=False, shelf_location="CS-E1-01", total_copies=2, available_copies=0, due_date=date.today() + timedelta(days=10), cover_color="#8E44AD"),
    Book(id=27, title="Deep Learning", author="Ian Goodfellow", isbn="978-0262035613", category="Computer Science", available=True, shelf_location="CS-E2-06", total_copies=3, available_copies=2, cover_color="#2C3E50"),
    Book(id=28, title="The Art of Electronics", author="Paul Horowitz", isbn="978-0521809269", category="Engineering", available=True, shelf_location="EN-C1-08", total_copies=2, available_copies=1, cover_color="#D35400"),
    Book(id=29, title="Quantum Mechanics", author="David J. Griffiths", isbn="978-1107189638", category="Physics", available=True, shelf_location="PH-C1-03", total_copies=3, available_copies=2, cover_color="#16A085"),
    Book(id=30, title="Introduction to Electrodynamics", author="David J. Griffiths", isbn="978-1108420419", category="Physics", available=True, shelf_location="PH-C2-10", total_copies=4, available_copies=3, cover_color="#C0392B"),
]


def get_all_books():
    return BOOKS


def search_books(query: str):
    q = query.lower()
    return [b for b in BOOKS if q in b.title.lower() or q in b.author.lower() or q in b.category.lower()]


def get_book_by_id(book_id: int):
    for b in BOOKS:
        if b.id == book_id:
            return b
    return None


def get_available_books():
    return [b for b in BOOKS if b.available]


def get_stats():
    total = len(BOOKS)
    available = len([b for b in BOOKS if b.available])
    categories = len(set(b.category for b in BOOKS))
    return {
        "total_books": total,
        "available_books": available,
        "checked_out": total - available,
        "categories": categories,
    }
