import requests

url = "https://the-one-api.dev/v2/movie"
headers = {
    "Authorization": "Bearer 5oGG3JzveKgdoZCshwtB"
}

response = requests.get(url, headers=headers)
print(response.json())
