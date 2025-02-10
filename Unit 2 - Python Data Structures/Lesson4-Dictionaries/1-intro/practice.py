def count_words(text: str) -> dict:
    # Split the input text into a list of words
    words = text.split()
    # Initialize an empty dictionary to store word frequencies
    word_count = {}
    for word in words:
        # Update word count or add new word
        word_count[word] = word_count.get(word, 0) + 1
    # Return the final word count dictionary
    return word_count

# Example usage:
input_text = "I like to move it move it"
print(count_words(input_text))

# Using comprehension - made it more complicated
# def count_words(text: str) -> dict:
#     word_count = {}
#     words = text.split()
#     {word_count.update({word:word_count.get(word,0)+1}) for word in words}
#     return word_count

# input_text = "I like to move it move it"
# print(count_words(input_text))
