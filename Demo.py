# demo.py
from operations import Library

def main():
    lib = Library()

    print("=== Add Books ===")
    lib.add_book("111", "Python Basics", "Alice", "Non-Fiction", 3)
    lib.add_book("222", "Star Galaxy", "Bob", "Sci-Fi", 2)

    print("=== Add Members ===")
    lib.add_member("m001", "Ranny", "benbrimaranny@gmail.com")
    lib.add_member("m002", "Tucker", "benbrimartucker@gmail.com")

    print("\n=== Borrow Books ===")
    lib.borrow_book("m001", "111")
    lib.borrow_book("m002", "222")
    print("Borrow successful!")

    print("\n=== List of Books ===")
    for b in lib.list_books():
        print(f"{b.isbn} - {b.title} | Available: {b.available_copies}/{b.total_copies}")

    print("\n=== Return Book ===")
    lib.return_book("m001", "111")
    print("Return successful!")

    print("\n=== Search Books by title 'Python' ===")
    results = lib.search_books("Python")
    for b in results:
        print(f"Found: {b.title} by {b.author}")

if __name__ == "__main__":
    main()