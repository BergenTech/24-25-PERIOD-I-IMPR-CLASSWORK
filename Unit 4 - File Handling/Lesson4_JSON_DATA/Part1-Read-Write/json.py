# Python JSON Starter
import json
# ------------------------------------------------------
# Exercise 1: Parse a simple JSON string (json.loads)
# ------------------------------------------------------
print("\nExercise 1: Parse a JSON string")

# A JSON string containing information about a state
state_json = '{"name": "California", "abbreviation": "CA", "area_codes": ["209", "213", "310"]}'

# TODO: Use json.loads() to parse the JSON string into a Python dictionary
# TODO: Print the state name
# TODO: Print the abbreviation
# TODO: Print the first area code in the list


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
# TODO: Print the JSON string

# TODO: Use json.dumps() again, but this time with indentation of 4 spaces
# TODO: Print the formatted JSON string


# ------------------------------------------------------
# Exercise 3: Load JSON from a file (json.load)
# ------------------------------------------------------
print("\nExercise 3: Load JSON from a file")

# TODO: Use json.load() to read data from 'states.json'
# TODO: Print how many states are in the file
# TODO: Print the name of the first state
# TODO: Print the abbreviation of the last state in the list


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
# TODO: Make sure to use indentation of 4 spaces to make the file readable


# ------------------------------------------------------
# Exercise 5: Working with nested JSON
# ------------------------------------------------------
print("\nExercise 5: Working with nested JSON")

# Try to read the file you created in Exercise 4
# TODO: Use json.load() to read the 'florida.json' file
# TODO: Print the state's capital
# TODO: Print the state's population
# TODO: Print whether the state is sunny or not