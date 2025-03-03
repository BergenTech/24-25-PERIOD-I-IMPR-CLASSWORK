# File: main.py
"""Main program that connects all modules"""
from book_list import create_book_list, display_books
from categories import organize_by_category, display_by_category
from search import search_books, display_search_results
from availability import track_availability, show_available_books
import os

def display_menu() -> None:
    print("\n=== 📚 Library Management System 📚 ===")
    print("1. View all books")
    print("2. View books by category")
    print("3. Search for books")
    print("4. Check book availability")
    print("5. Exit")
    print("=" * 37)

def main():
    # Initialize our data
    books = create_book_list()
    categories = organize_by_category()
    availability = track_availability()

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            display_books(books)
        
        elif choice == "2":
            display_by_category(categories)
        
        elif choice == "3":
            search_term = input("\nEnter search term: ")
            results = search_books(books, search_term)
            display_search_results(results)
        
        elif choice == "4":
            show_available_books(availability)
        
        elif choice == "5":
            print("\n👋 Thank you for using the Library Manager! Goodbye!")
            break
        
        else:
            print("\n❌ Invalid choice! Please try again.")
        
        input("\nPress Enter to continue...")
      

if __name__ == "__main__":
    main()
