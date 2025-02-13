def count_vowels_in_words(words: list[str]) -> dict[str, int]:
    return {word: len([letter for letter in word.lower() if letter in "aeiou"]) for word in words}

# Test Case
words = ["apple", "banana", "cherry", "grape"]
print(count_vowels_in_words(words))  