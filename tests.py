# tests.py
from operations import Library

lib = Library()

# Test 1: Add book
lib.add_book("101", "Book One", "Author A", "Fiction", 2)
assert "101" in lib.books
print("Test1 passed")

# Test 2: Add member
lib.add_member("m1", "Alice", "a@example.com")
assert "m1" in lib.members
print("Test2 passed")

# Test 3: Borrow and return
lib.borrow_book("m1", "101")
assert lib.books["101"].available_copies == 1
lib.return_book("m1", "101")
assert lib.books["101"].available_copies == 2
print("Test3 passed")

# Test 4: Cannot borrow more than 3
lib.add_book("102", "B2", "A2", "Fiction", 1)
lib.add_book("103", "B3", "A3", "Fiction", 1)
lib.add_book("104", "B4", "A4", "Fiction", 1)
lib.borrow_book("m1", "101")
lib.borrow_book("m1", "102")
lib.borrow_book("m1", "103")
try:
    lib.borrow_book("m1", "104")
    assert False, "Borrowed more than 3!"
except ValueError:
    print("Test4 passed")

# Test 5: Delete member only when no borrowed books
try:
    lib.delete_member("m1")
    assert False, "Deleted member with borrowed books!"
except ValueError:
    print("Test5 passed")

print("All tests passed.")