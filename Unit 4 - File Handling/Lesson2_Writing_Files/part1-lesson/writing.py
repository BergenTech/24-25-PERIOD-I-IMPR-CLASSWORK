#Open and write using "w" access mode
with open("test.txt",'w') as file:
    file.write("This is the first line.\n")
    file.write("This is the second line")
    
#This will overwrite the existing file    
with open("test.txt",'w') as file:
    file.write("This is the third line.\n")
    file.write("This is the fourth line")

lines = [
    "Line 1:\n",
    "Line 2:\n",
    "Line 3:\n",
]

with open("lines.txt", "a") as file:
    file.writelines(lines)