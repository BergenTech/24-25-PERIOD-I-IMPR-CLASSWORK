import requests  # HTTP library for making requests
import json  # For JSON manipulation and pretty printing

# Base URL for all requests
BASE_URL = "https://jsonplaceholder.typicode.com"  # Free fake API for testing

#================================================
# Part 1: Making a request and examining all response components
#================================================
response = requests.get(f"{BASE_URL}/users/1")

# 1. Status Code - numeric code indicating success/failure
print(f"Status Code:{response.status_code}")
# 2. Headers - metadata about the response
# print(f'Response Headers: {type(response.headers)}')
# print(f'Response Headers: {response.headers}')
for key,value in response.headers.items():
    print(f" {key}: {value}")

# 3. Cookies - any cookies set by the server
print(f"\nCookies: {dict(response.cookies)}")
# 4. Encoding - character encoding of the response
print(f"\nEncoding: {response.encoding}")
# 5. URL - the final URL of the response (useful for redirects)
print(f"\nFinal URL: {response.url}")
# 6. Elapsed Time - how long the request took
print(f"\nRequest Time: {response.elapsed.total_seconds()} seconds")
# 7. Raw content (bytes) - the raw binary response
print(f"{response.content}") # binary string
print(f"{response.content[:10]}")
# 8. Text content - decoded from bytes using the encoding
print(f"Text Content: {response.text}") # string
# 9. JSON content - parsed from text into Python objects
json_data = response.json()
print(f"Type: {json_data}")
print(json.dumps(json_data, indent=2))
#================================================
# Part 2: Accessing data from the JSON response
#================================================
print("\n\n=== Accessing Data from the Response ===")

# Store the response data for easy access
user = json_data
# Display all available top-level keys
print(f"Top-Level Keys: {list(user.keys())}")
# 1. Basic field access - direct dictionary indexing
print(f"User Name: {user['name']}")
print(f"Email: {user['email']}")

# 2. Nested field access - dealing with objects within objects
print(f"City: {user['address']['city']}")

# 3. Deep nested access - multiple levels of nesting
print(f"Lat: {user['address']['geo']['lat']}")
# 4. Safe access with .get() to handle missing keys
address = user.get('address', "Not Found!")
print(address)
country = address.get("country", "No Country Found!")
print(country)

# 5. Checking if keys exist
print(f" Has 'phone': {'phone' in user}") # True
print(f" Has 'age: {'age' in user}") # False

