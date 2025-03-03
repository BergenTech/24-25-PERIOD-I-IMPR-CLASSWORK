# File: categories.py
"""Handles book category operations"""

def organize_by_category() -> dict[str, list[str]]:
    return {
        "Fantasy": ["Harry Potter", "Percy Jackson"],
        "Science Fiction": ["The Hunger Games"],
        "Realistic Fiction": ["Diary of a Wimpy Kid", "Wonder"]
    }

def display_by_category(categories: dict[str, list[str]]) -> None:
    print("\nBooks by Category:")
    for category, books in categories.items():
        print(f"\n{category}:")
        for book in books:
            print(f"- {book}")

if __name__ == "__main__":
    # Test the module
    categories = organize_by_category()
    display_by_category(categories)