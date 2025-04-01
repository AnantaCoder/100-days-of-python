import requests
from datetime import datetime

TOKEN = 'askhh8srehs95'
USERNAME = 'anirban123'  # Corrected username to follow the rules
PIXXELA_ENDPOINT = 'https://pixe.la/v1/users'
GRAPH_ID = 'graph2'


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# POST
response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Study Graph",
    "unit": "Hour",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "5"
}

# PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

# Corrected the last part to use 'pixela_endpoint' instead of 'PIXXELA_ENDPOINT'
pixel_creation_end = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
print(f"{pixel_creation_end}")
pixel_data = {
    'date': "20241003",  # Corrected date format
    'quantity': "9.74"
}
pixel_response = requests.post(url=pixel_creation_end, json=pixel_data, headers=headers)
print(pixel_response.text)  # Ensure the response text is printed
