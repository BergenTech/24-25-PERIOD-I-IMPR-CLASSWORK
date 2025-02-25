# Exercise 1: Union of Sets
# The union of two sets combines all unique elements from both sets.
print("Exercise 1: Union of Sets")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
union_result = A | B  # or A.union(B)
print("Union:", union_result)  # Expected output: {1, 2, 3, 4, 5, 6}
print()


# Exercise 2: Intersection of Sets
# The intersection of two sets includes only the elements that are present in both sets.
print("Exercise 2: Intersection of Sets")
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
intersection_result = A & B  # or A.intersection(B)
print("Intersection:", intersection_result)  # Expected output: {30, 40}
print()


# Exercise 3: Difference of Sets
# The difference of two sets returns elements that are in the first set but not in the second.
print("Exercise 3: Difference of Sets")
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
difference_result = A - B  # or A.difference(B)
print("Difference (A - B):", difference_result)  # Expected output: {1, 2}
print()


# Exercise 4: Symmetric Difference
# The symmetric difference returns elements that are in either set, but not in both.
print("Exercise 4: Symmetric Difference")
A = {"apple", "banana", "cherry"}
B = {"banana", "cherry", "date", "fig"}
sym_diff_result = A ^ B  # or A.symmetric_difference(B)
print("Symmetric Difference:", sym_diff_result)  # Expected output: {'apple', 'date', 'fig'}
print()