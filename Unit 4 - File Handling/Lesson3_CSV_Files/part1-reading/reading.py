path = "students_roster.csv"
import csv
# Basic Reading
with open(path, 'r') as file:
    #create a csv reader object
    csv_reader = csv.reader(file)
    # skip the header row(if present)
    header = next(csv_reader) # assigns the first row
    print(f"Column Names: {header}")
    # prints object's memory location as Hex (Base 16) 0x...
    print(csv_reader) # it's also iterable
    
    #Process the data rows
    # for row in csv_reader:
    #     print(row)
        
    #reader object to list conversion
    data = list(csv_reader)
    # print(data)
      
emails = []
with open(path, 'r') as file:
    #create a DictReader object
    csv_to_dict = csv.DictReader(file)
    
    #process the rows
    for row in csv_to_dict:
        #Access the values by the column name
        Id = row['Id']
        Name = row['Name']
        Course = row['Course']
        Birthday = row['Birthday']
        Grade = row['Grade']
        Email = row['Email']
        
        #print name and email of each student
        # print(f"{Name} - {Email}")
        emails.append((Name, Email))
print(emails)