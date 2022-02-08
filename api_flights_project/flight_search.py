import requests
from datetime import datetime as dt, timedelta
import os
API_KEY = os.environ["API_KEY"]
FLIGHTS_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
HEADERS = {"apikey": API_KEY}
TOMORROW_DATE = (dt.now() + timedelta(days=1)).strftime("%d/%m/%Y")
AFTER6MONTH_DATE = (dt.now() + timedelta(days=30*6)).strftime("%d/%m/%Y")


class FlightSearch:
    def __init__(self):
        self.flights_list = []
        self.origin_city = "PRG"

    def search_flights(self, cities_iata: list):
        for iata in cities_iata:
            params = {
                "fly_from": self.origin_city,
                "fly_to": iata,
                "date_from": TOMORROW_DATE,
                "date_to": AFTER6MONTH_DATE
            }
            response = requests.get(url=FLIGHTS_ENDPOINT, params=params, headers=HEADERS)
            cheapest_flight = response.json()["data"][0]
            self.flights_list.append(cheapest_flight)


