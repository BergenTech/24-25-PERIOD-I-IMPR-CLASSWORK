# File: availability.py
"""Handles book availability tracking"""

def track_availability() -> dict[str, bool]:
    return {
        "Harry Potter": True,
        "Percy Jackson": True,
        "The Hunger Games": False,
        "Diary of a Wimpy Kid": True,
        "Wonder": False
    }

def show_available_books(availability: dict[str, bool]) -> None:
    print("\nBook Availability:")
    for book, is_available in availability.items():
        status = "✅ Available" if is_available else "❌ Borrowed"
        print(f"{book}: {status}")

if __name__ == "__main__":
    # Test the module
    availability = track_availability()
    show_available_books(availability)