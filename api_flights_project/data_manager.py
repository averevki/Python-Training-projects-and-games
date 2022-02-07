import requests
import os
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.new_flights = []
        self.prices_updated = False
        self.data = None
        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()

        self.cities = []
        for line in response.json()["prices"]:
            self.cities.append(line["city"])

    def add_iata(self, iata_codes: list):
        for index, code in enumerate(iata_codes):
            body = {
                "price": {
                    "iataCode": code
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{index + 2}", json=body)
            response.raise_for_status()

    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        self.data = response.json()["prices"]

    def update_prices(self, flights: list):
        self.new_flights.clear()
        self.prices_updated = False
        self.get_data()
        prices = [flight["price"] for flight in flights]
        for index, (position, new_price) in enumerate(zip(self.data, prices)):
            if position["lowestPrice"] > new_price:
                body = {
                    "price": {
                        "lowestPrice": new_price
                    }
                }
                response = requests.put(url=f"{SHEETY_ENDPOINT}/{index + 2}", json=body)
                response.raise_for_status()
                self.prices_updated = True
                self.new_flights.append(flights[index])

