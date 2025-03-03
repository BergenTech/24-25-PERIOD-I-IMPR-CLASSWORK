# File: book_list.py
"""Handles basic book list operations"""

def create_book_list() -> list[str]:
    return [
        "Harry Potter",
        "Percy Jackson",
        "The Hunger Games",
        "Diary of a Wimpy Kid",
        "Wonder"
    ]

def display_books(books: list[str]) -> None:
    print("\nBooks in Library:")
    for index, book in enumerate(books, 1):
        print(f"{index}. {book}")

if __name__ == "__main__":
    # Test the module
    books = create_book_list()
    display_books(books)