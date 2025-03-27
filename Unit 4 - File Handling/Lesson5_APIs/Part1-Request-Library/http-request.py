import requests  # HTTP library for making requests
import json  # For JSON manipulation and pretty printing

# Base URL for all requests
BASE_URL = "https://jsonplaceholder.typicode.com"  # Free fake API for testing

#================================================
# Part 1: Making a request and examining all response components
#================================================

# 1. Status Code - numeric code indicating success/failure


# 2. Headers - metadata about the response


# 3. Cookies - any cookies set by the server

# 4. Encoding - character encoding of the response

# 5. URL - the final URL of the response (useful for redirects)

# 6. Elapsed Time - how long the request took

# 7. Raw content (bytes) - the raw binary response

# 8. Text content - decoded from bytes using the encoding

# 9. JSON content - parsed from text into Python objects

#================================================
# Part 2: Accessing data from the JSON response
#================================================
print("\n\n=== Accessing Data from the Response ===")

# Store the response data for easy access

# Display all available top-level keys

# 1. Basic field access - direct dictionary indexing


# 2. Nested field access - dealing with objects within objects


# 3. Deep nested access - multiple levels of nesting

# 4. Safe access with .get() to handle missing keys


# 5. Checking if keys exist

