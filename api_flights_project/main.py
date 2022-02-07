#!/usr/bin/env python3

# Aleksandr Verevkin
# Cheapest flights project
# Program search for cheapest flight on given by google sheets information and send email if found new cheap flight
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager


if __name__ == "__main__":
    data = DataManager()
    flight_data = FlightData()
    search = FlightSearch()

    print("Getting IATA's...")
    flight_data.get_iata(data.cities)
    print("Updating IATA's...")
    data.add_iata(flight_data.cities_iata)
    print("Searching cheapest flights...")
    search.search_flights(flight_data.cities_iata)
    print("Updating prices...")

    data.update_prices(search.flights_list)
    if data.prices_updated:
        notification = NotificationManager()
        for flight in data.new_flights:
            notification.send_msg(flight)
