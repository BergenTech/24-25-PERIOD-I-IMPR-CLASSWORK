#1 Function to read entire file content
def read_entire_file(filename):
    """Reads the entire content of a file and returns it as a string."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
        

#2 Function to read file line by line
def read_file_line_by_line(filename):
    """Reads a file line by line and prints each line without extra whitespace."""
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())


#3 Function to store lines as a list
def read_file_as_list(filename):
    """Reads all lines of a file and returns them as a list."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file]
            

#3-2 Function to store lines as a list readlines() includes \n
def read_file_as_list2(filename):
    """Reads all lines of a file and returns them as a list."""
    with open(filename, 'r') as file:
        return file.readlines()


#4 Function to count lines in a file
def count_lines(filename):
    """Counts the number of lines in a file."""
    with open(filename, "r") as file:
        return sum(1 for _ in file)
        


#5 Function to search for a keyword in a file
def search_keyword(filename, keyword):
    """Finds and prints lines that contain a specific keyword."""
    pass



# Usage
if __name__ == "__main__":
    filename = "cs_fundamentals.txt"
    #1 Read the entire file content as a string
    # content = read_entire_file(filename)
    # print(type(content))
    # print(content)
    
    #2 Read file line by line
    # read_file_line_by_line(filename)
    
    #3 Store lines as a list
    # print(read_file_as_list(filename)[-1]) # last line
    # print(read_file_as_list2(filename)) 
    # for line in read_file_as_list2(filename):
    #     print(line)
    # print(read_file_as_list2(filename)[0]) 