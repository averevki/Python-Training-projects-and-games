#!/usr/bin/env python3

# Aleksandr Verevkin
# Exercise input to google sheets project
# Program take your exercises as string and translate it into google sheets as information
# sing nutrionix and their APIs
import requests
from datetime import datetime as dt
import os
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
AUTH_DETAILS = os.environ["AUTH_DETAILS"]
request_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/copyOfMyWorkouts/workouts"

if __name__ == "__main__":
    request_body = {
        "query": input("What you did today?: "),
        "gender": "male",
        "weight_kg": 72.5,
        "height_cm": 187.0,
        "age": 20
    }

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY
    }

    response = requests.post(url=request_endpoint, json=request_body, headers=headers)
    # print(response.json())
    exercise_data = response.json()["exercises"][0]
    date = dt.now().date().strftime("%d/%m/%Y")
    time = dt.now().time().strftime("%H:%M:%S")

    sheety_body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_data["user_input"].title(),
            "duration": round(exercise_data["duration_min"]),
            "calories": round(exercise_data["nf_calories"])
        }
    }

    auth = {
        "Authorization": AUTH_DETAILS
    }

    response = requests.post(url=sheety_endpoint, json=sheety_body, headers=auth)
    # print(response.text)
