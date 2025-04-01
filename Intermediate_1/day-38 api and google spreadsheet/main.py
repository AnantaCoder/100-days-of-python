import requests
from datetime import datetime
import os

# Nutritionix API credentials
NUTRITIONIX_API_KEY = 'fe37b1bce7ff4c13301079662b7c4e05'
NUTRITIONIX_APPLICATION_ID = '54743d06'

# User parameters
GENDER = "male"
WEIGHT_KG = 70  # Example weight in kg
HEIGHT_CM = 188  # Example height in cm
AGE = 20  # Example age in years

# API endpoints
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Check if SHEET_ENDPOINT environment variable is set
if 'SHEET_ENDPOINT' not in os.environ:
    raise Exception("Environment variable SHEET_ENDPOINT is not set.")
else:
    print("SHEET_ENDPOINT is set to:", os.environ['SHEET_ENDPOINT'])

sheety_endpoint = os.environ['SHEET_ENDPOINT']

# Request headers for Nutritionix API
headers = {
    "x-app-id": NUTRITIONIX_APPLICATION_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

# Collect exercise input from user
exercise_query = input("Which exercise did you do today? ")

# Create the Nutritionix request payload
nutritionix_post_request = {
    "query": exercise_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# Send POST request to Nutritionix API
response = requests.post(nutritionix_endpoint, json=nutritionix_post_request, headers=headers)

# Check response status
if response.status_code == 200:
    result = response.json()
    print("Nutritionix API call successful!")
else:
    print(f"Error calling Nutritionix API: {response.status_code}")
    print(response.text)
    exit()

# Get current date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Loop through exercises returned from Nutritionix
for exercise in result.get("exercises", []):
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Send data to Sheety API
    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, auth=(os.environ['SHEET_USER'], os.environ['SHEET_PW']))
    
    # Check the response from Sheety
    if sheet_response.status_code == 200:
        print(f"Data for {exercise['name']} added to Google Sheet!")
    else:
        print(f"Error adding data to sheet: {sheet_response.status_code}")
        print(sheet_response.text)
#    raise Exception("Environment variable SHEET_ENDPOINT is not set.")
#Exception: Environment variable SHEET_ENDPOINT is not set.