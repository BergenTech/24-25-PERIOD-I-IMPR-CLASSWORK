import json, csv
def json_to_csv_converter(json_filename):
    # Step 1 - Try to read JSON file
    try:
        with open(json_filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: File not found!")
        return
    
    # Step 2 - Check if JSON is empty
    if not data:
        print("Error: Empty or Invalid JSON!")
        return
    
    # Step 3 - Extract available fields
    # print(data) # List of dictionaries
    fields = list(data[0].keys()) 
    # print(fields) # List of keys of first dict
    print("Available Fields:")
    for i, field in enumerate(fields, start=1):
        print(f"{i}. {field}")
    
    # Step 4: Ask the user which fields they want
    selected_indices = input("Enter the numbers of the fields:")
    selected_fields = [fields[int(i)-1] for i in selected_indices.split(',') if i.strip().isdigit() and 0 < int(i) <= len(fields)]
    
    # Step 5 - Define CSV File Name
    # csv_filename = json_filename.replace(".json", ".csv")
    csv_filename = input("Name your CSV File:") + ".csv"
    
    # Step 6 - Write data to CSV file
    with open(csv_filename, 'w', newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=selected_fields)
        writer.writeheader()
        for row in data:
            writer.writerow({field:row.get(field,"") for field in selected_fields})
    # Step 7 - Notify the User
    print(f"CSV file created: {csv_filename}")
        
    
if __name__ == "__main__":
    json_to_csv_converter("nba-players.json")