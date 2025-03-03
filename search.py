# File: search.py
"""Handles book search operations"""

def search_books(books: list[str], search_term: str) -> list[str]:
    search_term = search_term.lower()
    matching_books = [book for book in books if search_term in book.lower()]
    return matching_books

def display_search_results(results: list[str]) -> None:
    if results:
        print("\nFound these books:")
        for book in results:
            print(f"- {book}")
    else:
        print("\nNo books found matching your search.")
        
if __name__ == "__main__":
    # Test the module
    test_books = ["Harry Potter", "The Hobbit", "Percy Jackson"]
    results = search_books(test_books, "harry")
    display_search_results(results)
