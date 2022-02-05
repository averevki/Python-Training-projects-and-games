#!/usr/bin/env python3

# Aleksandr Verevkin
# Program check if in nearest 12 hours will rain using api of weather website
# And send you email if you'll need to bring umbrella
import requests
import smtplib
import os
LAT = -21.462610
LON = 47.080200
APPID = os.environ.get("APPID")  # Your openweathermap.org API key
MAIL_SMTP = "smtp.gmail.com"
EMAIL = "doxxx@gmail.com"
PASSWORD = "qwerty12345"

if __name__ == "__main__":
    params = {
        "lat": LAT,
        "lon": LON,
        "exclude": "current,minutely,daily",
        "appid": APPID
    }

    response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=params)
    response.raise_for_status()

    first_twelve_hours = response.json()["hourly"][:12]
    first_twelve_hours_codes = []
    for hour in first_twelve_hours:
        if hour["weather"][0]["id"] < 700:
            connection = smtplib.SMTP(MAIL_SMTP)
            connection.starttls()  # Transport Layer Security provide communication security
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg="Subject:Rain soon\n\nYou'll need to bring an umbrella."
            )

            print("You'll need to bring an umbrella")
            break
