# import requests

# url = "https://chatgpt-42.p.rapidapi.com/aitohuman"

# payload = { "text": "How are you?" }
# headers = {
# 	"x-rapidapi-key": "80eb60fbffmshf97e3e71a5bd6b3p1df76ejsn5117df608268",
# 	"x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }

# response = requests.post(url, json=payload, headers=headers)
# result = response.json().get('result', [])
# print(result)

import requests

url = "https://google-api31.p.rapidapi.com/map"

payload = {
	"text": "white house",
	"place": "washington DC",
	"street": "",
	"city": "",
	"country": "",
	"state": "",
	"postalcode": "",
	"latitude": "",
	"longitude": "",
	"radius": ""
}
headers = {
	"x-rapidapi-key": "80eb60fbffmshf97e3e71a5bd6b3p1df76ejsn5117df608268",
	"x-rapidapi-host": "google-api31.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())