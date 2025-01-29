def idk(t):
    # Find minimum value and its index
    min_val = min(t)
    min_idx = t.index(min_val)
    # Create new tuple by slicing and concatenating
    return t[min_idx:] + t[:min_idx]

def check_consecutive(tup: tuple) -> bool:
    for i in range(len(tup) - 1):
        if tup[i] == tup[i + 1]:
            return True
    return False



def rotate_tuple(tup: tuple, n: int) -> tuple:  
    return tup[-n:] + tup[:-n]
#tup[-2:] gets last 2 elements: (4, 5) 
#tup[:-2] gets everything except last 2: (1, 2, 3)
#Concatenate: (4, 5) + (1, 2, 3) = (4, 5, 1, 2, 3)
#Positive n rotates to right, negative n rotates to left
