def cutInHalf(text:str):
    mid = (len(text)+1)//2
    newText = text[mid:]+text[:mid]
    return newText

print(cutInHalf("Teterboro"))
print(cutInHalf("Bergen"))
