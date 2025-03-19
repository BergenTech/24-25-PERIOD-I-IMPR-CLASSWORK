# Python JSON Starter
import json
# ------------------------------------------------------
# Exercise 1: Parse a simple JSON string (json.loads)
# ------------------------------------------------------
print("\nExercise 1: Parse a JSON string")

# A JSON string containing information about a state
state_json = '{"name": "California", "abbreviation": "CA", "area_codes": ["209", "213", "310"]}'

# TODO: Use json.loads() to parse the JSON string into a Python dictionary
state_dict = json.loads(state_json)
# print(type(state_dict))
# TODO: Print the state name
print(f"State name: {state_dict['name']}")
# TODO: Print the abbreviation
print(f"Abbreviation: {state_dict['abbreviation']}")
# TODO: Print the first area code in the list # 209
print(f"First area code: {state_dict['area_codes'][0]}")

# ------------------------------------------------------
# Exercise 2: Convert Python to JSON (json.dumps)
# ------------------------------------------------------
print("\nExercise 2: Convert Python to JSON")

# A Python dictionary with state information
state_dict = {
    "name": "Texas",
    "abbreviation": "TX",
    "area_codes": ["210", "214", "254", "281"],
    "is_big": True,
    "population": 29145505
}

# TODO: Use json.dumps() to convert the dictionary to a JSON string
json_string = json.dumps(state_dict)
# TODO: Print the JSON string
print(f"JSON String: {json_string}")
print(type(json_string))
# TODO: Use json.dumps() again, but this time with indentation of 4 spaces
pretty_json = json.dumps(state_dict, indent=4)
# TODO: Print the formatted JSON string
print("Formatted JSON String")
print(pretty_json)
# ------------------------------------------------------
# Exercise 3: Load JSON from a file (json.load)
# ------------------------------------------------------
print("\nExercise 3: Load JSON from a file")

# TODO: Use json.load() to read data from 'states.json'
with open("states.json", 'r') as file:
    states_data = json.load(file)
    # Access data from the file
    states_list = states_data["states"]
# TODO: Print how many states are in the file
    print(f"Number of states: {len(states_list)}")
# TODO: Print the name of the first state
    print(f"First state: {states_list[0]['name']}")
    print(f"Last state: {states_list[-1]['name']}")

# TODO: Print the abbreviation of the last state in the list
    print(f"Last state Abbreviation: {states_list[-1]['abbreviation']}")


# ------------------------------------------------------
# Exercise 4: Write JSON to a file (json.dump)
# ------------------------------------------------------
print("\nExercise 4: Write JSON to a file")

# Create a dictionary for Florida
florida = {
    "name": "Florida",
    "abbreviation": "FL",
    "area_codes": ["239", "305", "321", "352"],
    "info": {
        "capital": "Tallahassee",
        "population": 21538187,
        "is_sunny": True
    }
}

# TODO: Use json.dump() to write the florida dictionary to a file named 'florida.json'
with open('florida.json', 'w') as file:
# TODO: Make sure to use indentation of 4 spaces to make the file readable
    json.dump(florida, file, indent=4)
    print("Successfully wrote Florida data to florida.json!")
# ------------------------------------------------------
# Exercise 5: Working with nested JSON
# ------------------------------------------------------
print("\nExercise 5: Working with nested JSON")

# Try to read the file you created in Exercise 4
# TODO: Use json.load() to read the 'florida.json' file
# TODO: Print the state's capital
# TODO: Print the state's population
# TODO: Print whether the state is sunny or not