# Python Requests Library
## Working with Headers and Parameters

---

## Introduction

- Building on basic GET requests
- Why parameters and headers matter
- Real-world API interaction requires both

---

## Lesson Objectives

By the end of this lesson, you will be able to:
- Use query parameters to filter API responses
- Add custom headers to HTTP requests
- Understand how headers affect API behavior
- Combine parameters and headers effectively

---

## Review: Basic GET Request

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # 200
print(response.json())       # content of the post
```

---

# PART 1: WORKING WITH PARAMETERS

---

## What Are Query Parameters?

- Key-value pairs that appear after `?` in a URL
- Used to filter, sort, or modify API responses
- Format: `?key1=value1&key2=value2`
- Tell the API exactly what you want

---

## Adding Parameters: Method 1
### Manual URL Construction

```python
# Manually adding parameters to URL
response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")

print(f"Status code: {response.status_code}")
print(f"Number of posts: {len(response.json())}")
```

⚠️ Less recommended - requires manual URL encoding

---

## Adding Parameters: Method 2
### Using the params Parameter (Recommended)

```python
# Using the params parameter
params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts", 
                       params=params)

print(f"Status code: {response.status_code}")
print(f"Final URL: {response.url}")
```

✅ Handles URL encoding automatically

---

## Multiple Parameters

```python
params = {
    "userId": 1,
    "id": 5
}

response = requests.get("https://jsonplaceholder.typicode.com/posts", 
                       params=params)

print(f"Status code: {response.status_code}")
print("Post found:")
print(response.json())
```

---

## List Parameters (Multiple Values)

```python
params = {
    "id": [1, 2, 3]  # Multiple IDs
}

response = requests.get("https://jsonplaceholder.typicode.com/posts", 
                       params=params)

print(f"Final URL: {response.url}")
print(f"Number of posts: {len(response.json())}")
```

Becomes: `?id=1&id=2&id=3` in the URL

---

## Parameters: Practice Exercise

1. Make a request to get comments for a specific post
2. Try filtering posts by both userId and title
3. What happens if you use a parameter the API doesn't support?

---

# PART 2: WORKING WITH HEADERS

---

## What Are HTTP Headers?

- Metadata about the request or response
- Key-value pairs sent with every HTTP transaction
- Provide instructions to servers and clients
- Common headers: `User-Agent`, `Accept`, `Content-Type`, `Authorization`

---

## Setting Request Headers

```python
headers = {
    "User-Agent": "Python Requests Tutorial",
    "Accept": "application/json"
}

response = requests.get("https://jsonplaceholder.typicode.com/posts/1", 
                       headers=headers)

print(f"Status code: {response.status_code}")
```

---

## Common Request Headers

- `User-Agent`: Identifies your client/application
- `Accept`: What content types you can process
- `Content-Type`: What type of data you're sending
- `Authorization`: Authentication credentials
- `Accept-Language`: Preferred language for response

---

## Viewing Response Headers

```python
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print("Response headers received:")
for key, value in response.headers.items():
    print(f"{key}: {value}")
```

---

## Content Negotiation with Headers

```python
# Request JSON
headers = {"Accept": "application/json"}
response = requests.get("https://jsonplaceholder.typicode.com/posts/1", 
                       headers=headers)

print(f"Content-Type: {response.headers.get('Content-Type')}")
```

Tell the server what format you want data in

---

## API Authentication with Headers

```python
# Most APIs require authentication tokens in headers
api_key = "your_api_key_here"  # Placeholder
auth_headers = {
    "Authorization": f"Bearer {api_key}",
    "User-Agent": "Python Requests Tutorial"
}

response = requests.get("https://api.example.com/data", 
                       headers=auth_headers)
```

---

## Headers: Practice Exercise

1. Make a request with a custom User-Agent
2. Check what Content-Type is returned
3. Compare how different Accept headers affect responses (if at all)

---

## Combining Headers and Parameters

```python
headers = {"Accept": "application/json"}
params = {"userId": 1}

response = requests.get("https://jsonplaceholder.typicode.com/posts", 
                       headers=headers, 
                       params=params)

print(f"Status code: {response.status_code}")
print(f"Final URL: {response.url}")
```

---

## POST with Headers and JSON Body

```python
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Python Requests Tutorial"
}

data = {
    "title": "Python Requests",
    "body": "Learning about headers and parameters",
    "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", 
                        headers=headers, 
                        json=data)
```

---

## Common Errors & Solutions

- **401/403**: Authentication issues (check Authorization header)
- **415**: Unsupported media type (check Content-Type header)
- **406**: Not acceptable (check Accept header)
- **400**: Bad request (check parameters format)

---

## Quick Review

- Parameters filter and customize API requests
- Headers provide metadata and instructions
- Use `params` parameter instead of manual URL construction
- Headers often required for authentication and content negotiation

---

## Challenge Exercise

Create a function that:
1. Makes a request to JSONPlaceholder API
2. Uses at least two different parameters
3. Sets appropriate headers
4. Handles common errors
5. Returns formatted data

---

## Additional Resources

- [Requests Library Documentation](https://docs.python-requests.org/)
- [HTTP Headers Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
- [JSONPlaceholder API Documentation](https://jsonplaceholder.typicode.com/)

---
