# def find_first_unique(numbers: list[int]) -> int:
#     for num in numbers:
#         # Check if the number appears exactly once
#         if numbers.count(num) == 1:  
#             return num
#     return -1  # if no unique number is found

# print(find_first_unique([4, 5, 1, 2, 2, 5, 4, 6]))  # Output: 1
# print(find_first_unique([7, 7, 8, 8]))             # Output: -1
# print(find_first_unique([10, 20, 30, 10, 20]))     # Output: 30


# def square_numbers_from_string(numbers_string: str) -> list[int]:
#     # Split the string into individual numbers
#     numbers = numbers_string.split('-')
#     squared_numbers = []
#     for num in numbers:
#         squared_numbers.append(int(num)**2)
#     return squared_numbers

# result = square_numbers_from_string('1-2-3-4')
# print(result)  
# # Output: [1, 4, 9, 16]


# def func():
#     prog_langs = []
#     for _ in range(3):
#         lang = input('Programming Language: ')
#         prog_langs.append(lang)
#     result = '-'.join(prog_langs)
#     return result

# output = func()
# print(output)