import csv
data_list = []
data_dict = []
with open("students_roster.csv", "r") as file:
    csv_reader = csv.reader(file)
    data_list = list(csv_reader)
    # Reset file pointer(cursor) to the beginning to reuse DictReader
    file.seek(0)
    data_dict = list(csv.DictReader(file))
    
# print(data_list)
# print(data_dict)

# Writing a simple CSV file
# 1 - Writing Row by Row from a List of Lists
# Open or create a file
with open("data.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    # Hardcoded 
    # writer.writerow(['Id', 'Name', 'etc.'])
    # writer.writerow(data_list[0])
    writer.writerow(['Name', 'Grade', 'Email'])
    for row in data_list:
        writer.writerow([row[1],row[4],row[5]])

# 2 - Writing Row by Row from a List of Dictionaries
fieldNames = ['Name', 'Birthday']
#Open file to write
with open("birthdays.csv", 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldNames)
    
    #Write the header row with column names(fieldNames)
    writer.writeheader()
    
    #Write all data rows
    # writer.writerows(data_dict) #Raises value error data includes all the columns from the original CSV file
    
    # Filter out unwanted fields
    # Write only the specified fields
    writer.writerows({key:row[key] for key in fieldNames} for row in data_dict)

new_students = [
    ['David', "03/12/09"],
    ['Alice', "12/03/09"],
]   
#3 Appending to Existing CSV File
with open("birthdays.csv", 'a', newline="") as file:
    writer = csv.writer(file)
    writer.writerows(new_students)