# operations.py
"""
Mini Library Management System (OOP Version)
--------------------------------------------
Classes:
 - Book
 - Member
 - Library

Each class handles its own data and methods.
"""

# --- Allowed genres (tuple as assignment required) ---
GENRES = ("Fiction", "Non-Fiction", "Sci-Fi", "Fantasy", "Biography", "History")


class Book:
    def __init__(self, isbn, title, author, genre, total_copies):
        if genre not in GENRES:
            raise ValueError(f"Invalid genre: {genre}")
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self):
        if self.available_copies <= 0:
            raise ValueError("No copies available to borrow.")
        self.available_copies -= 1

    def return_copy(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1

    def update(self, title=None, author=None, genre=None, total_copies=None):
        if genre and genre not in GENRES:
            raise ValueError("Invalid genre.")
        if total_copies is not None:
            borrowed = self.total_copies - self.available_copies
            if total_copies < borrowed:
                raise ValueError("New total less than borrowed copies.")
            diff = total_copies - self.total_copies
            self.available_copies += diff
            self.total_copies = total_copies
        if title:
            self.title = title
        if author:
            self.author = author
        if genre:
            self.genre = genre


class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if len(self.borrowed_books) >= 3:
            raise ValueError("Borrow limit reached (3).")
        book.borrow()
        self.borrowed_books.append(book.isbn)

    def return_book(self, book: Book):
        if book.isbn not in self.borrowed_books:
            raise ValueError("This member did not borrow that book.")
        book.return_copy()
        self.borrowed_books.remove(book.isbn)


class Library:
    def __init__(self):
        self.books = {}     # isbn -> Book
        self.members = {}   # id -> Member

    # --- CRUD for books ---
    def add_book(self, isbn, title, author, genre, total_copies):
        if isbn in self.books:
            raise ValueError("ISBN already exists.")
        self.books[isbn] = Book(isbn, title, author, genre, total_copies)
        return True

    def update_book(self, isbn, **kwargs):
        if isbn not in self.books:
            raise ValueError("Book not found.")
        self.books[isbn].update(**kwargs)

    def delete_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not found.")
        book = self.books[isbn]
        borrowed = book.total_copies - book.available_copies
        if borrowed > 0:
            raise ValueError("Cannot delete; some copies are borrowed.")
        del self.books[isbn]

    def search_books(self, query, by="title"):
        query = query.lower()
        results = []
        for b in self.books.values():
            field = getattr(b, by, "").lower()
            if query in field:
                results.append(b)
        return results

    # --- CRUD for members ---
    def add_member(self, member_id, name, email):
        if member_id in self.members:
            raise ValueError("Member ID already exists.")
        self.members[member_id] = Member(member_id, name, email)
        return True

    def update_member(self, member_id, **kwargs):
        if member_id not in self.members:
            raise ValueError("Member not found.")
        m = self.members[member_id]
        if "name" in kwargs:
            m.name = kwargs["name"]
        if "email" in kwargs:
            m.email = kwargs["email"]

    def delete_member(self, member_id):
        if member_id not in self.members:
            raise ValueError("Member not found.")
        m = self.members[member_id]
        if m.borrowed_books:
            raise ValueError("Member still has borrowed books.")
        del self.members[member_id]

    # --- Borrow / Return ---
    def borrow_book(self, member_id, isbn):
        if member_id not in self.members:
            raise ValueError("Member not found.")
        if isbn not in self.books:
            raise ValueError("Book not found.")
        m = self.members[member_id]
        b = self.books[isbn]
        m.borrow_book(b)
        return True

    def return_book(self, member_id, isbn):
        if member_id not in self.members:
            raise ValueError("Member not found.")
        if isbn not in self.books:
            raise ValueError("Book not found.")
        m = self.members[member_id]
        b = self.books[isbn]
        m.return_book(b)
        return True

    # --- Helpers ---
    def list_books(self):
        return list(self.books.values())

    def list_members(self):
        return list(self.members.values())