#!/usr/bin/env python3

# Aleksandr Verevkin
# ISS is near you project
# Program every minute check if International Space Station is above you :)
import smtplib
import time
import requests
from datetime import datetime
LAT = 49.195061
LNG = 16.606836
MAIL_SMTP = "smtp.gmail.com"
EMAIL = "doxxx@gmail.com"
PASSWORD = "qwerty12345"


def check_position(position):
    """Check if position is near mine position"""
    return LAT - 5 <= position[0] <= LAT + 5 and LNG - 5 <= iss_position[1] <= LNG + 5


def check_dark():
    """Check if it's dark"""
    return sunrise >= datetime.now().hour or sunset <= datetime.now().hour


def request_iss_position():
    """Return ISS current position"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    iss_data = response.json()
    position = (float(iss_data["iss_position"]["latitude"]), float(iss_data["iss_position"]["longitude"]))
    return position


def request_sun_data():
    """Return sunrise, sunset in set region"""
    params = {
        "lat": LAT,
        "lng": LNG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()

    data = response.json()
    temp_sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    temp_sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
    return temp_sunrise, temp_sunset


if __name__ == "__main__":
    sunrise, sunset = request_sun_data()
    while True:
        time.sleep(60)
        if check_position(request_iss_position()) and check_dark():
            connection = smtplib.SMTP(MAIL_SMTP)
            connection.starttls()  # Transport Layer Security provide communication security
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg="Subject:Look UP\n\nThe ISS is above you in the sky."
            )
