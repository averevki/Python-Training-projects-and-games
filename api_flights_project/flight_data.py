import requests
import os
API_KEY = os.environ["API_KEY"]
FLIGHTS_ENDPOINT = "https://tequila-api.kiwi.com/locations"
HEADERS = {"apikey": API_KEY}


class FlightData:
    def __init__(self):
        self.cities_iata = []

    def get_iata(self, cities: list):
        for city in cities:
            params = {
                "term": city
            }
            response = requests.get(url=f"{FLIGHTS_ENDPOINT}/query", params=params, headers=HEADERS)
            iata_code = response.json()["locations"][0]["code"]
            self.cities_iata.append(iata_code)
