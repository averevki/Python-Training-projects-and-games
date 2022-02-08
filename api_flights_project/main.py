#!/usr/bin/env python3

# Aleksandr Verevkin
# Cheapest flights project using flight search API
# Program search for cheapest flight on given by google sheets information and send email if found new cheap flight
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_club import FlightClub


def main():
    data = DataManager()
    flight_data = FlightData()
    search = FlightSearch()
    club = FlightClub()
    # Adding new users
    while input("Add new user?(yes/no):") == "yes":
        club.add_user()
    # Refresh cities codes
    print("Getting IATA's...")
    flight_data.get_iata(data.cities)
    print("Updating IATA's...")
    data.add_iata(flight_data.cities_iata)
    print("Searching cheapest flights...")
    search.search_flights(flight_data.cities_iata)
    print("Updating prices...")

    data.update_prices(search.flights_list)
    # Send notifications if new flight found
    if data.prices_updated:
        notification = NotificationManager()
        for flight in data.new_flights:
            notification.send_msg(flight)  # For you
            notification.send_emails(flight)  # For club members


if __name__ == "__main__":
    main()
