# def find_first_book_by_author(books, author):
#     for book in books:
#         if book.author == author:
#             return book
#     return None
# ```

def find_first_book_by_author(xs, condition):
    for x in xs:
        if condition():
            return x
    return None