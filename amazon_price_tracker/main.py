#!/usr/bin/env python3

# Aleksandr Verevkin
# Program scraping data from Amazon.com chosen item price
# And send you a email if price drop under configured price
import smtplib
import requests
from bs4 import BeautifulSoup
ITEM = "https://www.amazon.com/dp/B07VGRJDFY/ref=twister_B07XLGBYM3?_encoding=UTF8&th=1"
MAX_PRICE = 250.0
MAIL_SMTP = "smtp.gmail.com"
EMAIL = "doxxx@gmail.com"
PASSWORD = "qwerty12345"
BROWSER_USER_AGENT = "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"
BROWSER_ACCEPT_LANGUAGE = "en-US,en;q=0.5"
headers = {
    "User-Agent": BROWSER_USER_AGENT,
    "Accept-Language": BROWSER_ACCEPT_LANGUAGE
}


def main():
    content = requests.get(url=ITEM, headers=headers).text

    soup = BeautifulSoup(content, "html.parser")
    current_price = float(soup.find(class_="a-text-price").getText().split("$")[1])

    if current_price < MAX_PRICE:
        product_name = soup.title.getText()
        connection = smtplib.SMTP(MAIL_SMTP)
        connection.starttls()  # Transport Layer Security provide communication security
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{product_name} is now ONLY ${current_price}\n"
                f"{ITEM}"
        )


if __name__ == "__main__":
    main()
