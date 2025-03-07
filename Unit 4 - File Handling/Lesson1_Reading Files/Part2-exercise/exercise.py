file_path = "apcsp_vocabs.txt"
# #open the file for reading
# with open(file_path, 'r') as file:
#     #Read all lines into a list called content
#     content = file.readlines()
#     #Extract words and remove duplicates via set comp
#     words = list({line[0:line.find(":")] for line in content})
#     #Sort the list
#     sorted_words = sorted(words)
#     for word in sorted_words:
#         print(word)
# print(f"\n Total terms: {len(sorted_words)}")

#The extract_sorted_words function encapsulates all the logic for processing the file.
def extract_sorted_words(path: str, delimiter: str = ':') -> list:
    try:
        with open(path, 'r') as file:
            # Process each line with set comprehension to extract unique words
            #partition(delimiter) splits the string at the first occurrence of delimiter, returning a tuple: 
            # (before, delimiter, after).
            words = {line.partition(delimiter)[0].strip() for line in file}
        # Return a new list with the words sorted in ascending order.
        return sorted(words)
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return []
# Example usage:
if __name__ == "__main__":
    path = "apcsp_vocabs.txt"
    sorted_words = extract_sorted_words(path)
    for word in sorted_words:
        print(word)