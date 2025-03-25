def main():
    while True:
        print("\n=== File Format Converter ===")
        print("1. Convert JSON to CSV")
        print("2. Convert CSV to JSON")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ")
        
        if choice == "1":
            filename = input("Enter the JSON filename: ")
            #json_to_csv_converter(filename)
        elif choice == "2":
            filename = input("Enter the CSV filename: ")
            #csv_to_json_converter(filename)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()