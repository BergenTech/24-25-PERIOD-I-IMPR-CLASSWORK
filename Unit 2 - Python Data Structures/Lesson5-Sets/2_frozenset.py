# Sets are mutable
numbers = {1, 2, 3}

# Can’t used as a key in a dict
frozen ={numbers:1}

# Create immutable set
frozen = frozenset([1, 2, 3])

# Can be used as dictionary key
d = {frozen: 'value'}
# Frozen sets are just like normal sets, but they cannot be modified after creation.
frozen_A = frozenset([1, 2, 3, 4])
frozen_B = frozenset([3, 4, 5, 6])
print("Frozen Set A:", frozen_A)  # Expected output: frozenset({1, 2, 3, 4})
print("Frozen Set B:", frozen_B)  # Expected output: frozenset({3, 4, 5, 6})
print()
