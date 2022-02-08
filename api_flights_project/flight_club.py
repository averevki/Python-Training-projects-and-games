import requests
import os
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/flightDeals/users"


class FlightClub:
    def __init__(self):
        pass

    def add_user(self):
        print("Welcome to the Flight Club.\n"
              "We find the best flights deals and email you.")
        params = {
            "user": {
                "firstName": input("What is your first name?\n"),
                "lastName": input("What is your last name?\n"),
                "email": input("What is your email?\n")
            }
        }
        if input("Type your email again.\n") == params["user"]["email"]:
            response = requests.post(url=SHEETY_ENDPOINT, json=params)
            response.raise_for_status()
            print("You're in the club!")
        else:
            print("Emails are not the same")
