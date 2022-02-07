import smtplib
import os
MAIL_SMTP = "smtp.gmail.com"
EMAIL = os.environ["EMAIL"]  # "doxxx@gmail.com"
PASSWORD = os.environ["PASSWORD"]  # "qwerty12345"


class NotificationManager:
    def __init__(self):
        pass

    def send_msg(self, flight):
        connection = smtplib.SMTP(MAIL_SMTP)
        connection.starttls()  # Transport Layer Security provide communication security
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:New Flight {flight['flyFrom']}->{flight['flyTo']}\n\n"
                f"New flight only for {flight['conversion']}EUR."
                f"Date: {flight['route'][0]['local_arrival']}"
        )
