# List comprehension and filtering(using ifs)
# [x+1 for x in range(5) if x%2 == 0]
# Do this for this collection in this situation
numbers = [3, -1, 6, 10, 8, 23, 4]
# conventional way - find the halves
half = []
for n in numbers:
    if n % 2 == 0:
        n = n // 2
        half.append(n)
# print(half)
print([n//2 for n in numbers if n%2==0])
divided = [x for x in range(100) if x%2==0 and x%5==0]
print(divided)


grades = [85, 60, 45, 59, 99]
results = ['failed' if x<60 else 'passed' for x in grades]
