filename = "cs_fundamentals.txt"
with open(filename, 'r') as file:
    print(file.read(10)) #get the first 10 character
    print(file.read(20)) #get the next 20 character
    file.seek(0) #go to the beginning of file
    print(file.read(10)) #get the first 10 character
    print(file.read()) #read the whole characters
    print(file.read(10)) #get the first 10 character
    print(file.tell()) # find out where the cursor is
    file.seek(0)
    print(file.tell())
    print(file.readline()) # reads one line at a time
    print(file.readline()) # reads next line 
    