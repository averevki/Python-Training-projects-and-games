import smtplib
import requests
import os
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/flightDeals/users"
MAIL_SMTP = "smtp.gmail.com"
EMAIL = "doxxx@gmail.com"
PASSWORD = "qwerty12345"


class NotificationManager:
    def __init__(self):
        self.connection = smtplib.SMTP(MAIL_SMTP)
        self.connection.starttls()  # Transport Layer Security provide communication security
        self.connection.login(EMAIL, PASSWORD)

    def send_msg(self, flight):
        """Send mail to yourself"""
        self.connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:New Flight {flight['flyFrom']}->{flight['flyTo']}\n\n"
                f"New flight only for {flight['conversion']}EUR."
                f"Date: {flight['route'][0]['local_arrival']}"
        )

    def send_emails(self, flight):
        """Send mails to the club members"""
        sheet_data = requests.get(url=SHEETY_ENDPOINT)
        sheet_data.raise_for_status()
        users = sheet_data["users"]

        for user in users:
            self.connection.sendmail(
                from_addr=EMAIL,
                to_addrs=user["email"],
                msg=f"Subject:New Flight {flight['flyFrom']}->{flight['flyTo']}\n\n"
                    f"New flight only for {flight['conversion']}EUR."
                    f"Date: {flight['route'][0]['local_arrival']}"
            )
