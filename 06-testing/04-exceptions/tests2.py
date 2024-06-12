# In `tests.py`, write three parametrized tests:

# * `test_valid_creation` that create books with valid `title` and `isbn`.
# * `test_creation_with_invalid_title` that create books with an invalid `title`.
# * `test_creation_with_invalid_isbn` that create books with an invalid `isbn`.

# But how does one assert that an exception is thrown?
# Pytest offers the following construct:

# ```python
# import pytest


# def test_raises_exception():
#     with pytest.raises(ExceptionClass):
#         # code that should throw an ExceptionClass
# ```
import pytest
from book import Book

@pytest.mark.parametrize('title', [
    'John Wick', 
    'U moeder',
    'lol'
])
@pytest.mark.parametrize('isbn', [
    '978-1779501127',
    '978-1-77-950112-7',
    '978 1 77 950112 7',
    '9780735611313'
])
def test_valid_creation(title, isbn):
    book = Book(title, isbn)
    
    assert book.title == title
    assert book.isbn == isbn
    
@pytest.mark.parametrize('title', [
    ' ', 
    '',
    'B'
])
@pytest.mark.parametrize('isbn', [
    '978-1779501127',
    '978-1-77-950112-7',
    '978 1 77 950112 7',
    '9780735611313'
])
def test_creation_with_invalid_title(title, isbn):
    with pytest.raises(RuntimeError):
        Book(title, isbn)
    

@pytest.mark.parametrize('isbn', [
    '978-17701127',
    '',
    ' ',
    '696969420'
])
def test_creation_with_invalid_isbn(title, isbn):
    with pytest.raises(RuntimeError):
        Book(title, isbn)