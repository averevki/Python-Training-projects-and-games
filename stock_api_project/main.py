#!/usr/bin/env python3

# Aleksandr Verevkin
# Program get the latest stock changes for chosen stock and if they are significant send you email
import requests
import smtplib
from datetime import datetime, timedelta
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
PERCENTAGE = 5
STOCK_APIKEY = "3AE144SHYVS036K2"
NEWS_APIKEY = "fa802eb6526d4be888fe6ef7ae28e609"
MAIL_SMTP = "smtp.gmail.com"
EMAIL = "doxxx@gmail.com"
PASSWORD = "qwerty12345"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_APIKEY
}

if __name__ == "__main__":
    b_yesterday = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
    bb_yesterday = (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")

    stock_response = requests.get("https://www.alphavantage.co/query", params=stock_params)
    stock_response.raise_for_status()

    b_yesterday_price = float(stock_response.json()["Time Series (Daily)"][b_yesterday]["4. close"])
    bb_yesterday_price = float(stock_response.json()["Time Series (Daily)"][bb_yesterday]["4. close"])

    change = (b_yesterday_price - bb_yesterday_price) / (bb_yesterday_price / 100)
    if abs(change) >= PERCENTAGE:
        news_params = {
            "q": COMPANY_NAME,
            "from": bb_yesterday,
            "to": b_yesterday,
            "apiKey": NEWS_APIKEY
        }

        news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
        news_response.raise_for_status()

        connection = smtplib.SMTP(MAIL_SMTP)
        connection.starttls()  # Transport Layer Security provide communication security
        connection.login(EMAIL, PASSWORD)

        articles = news_response.json()["articles"][:3]
        for article in articles:
            headline = article["title"]
            brief = article["description"]
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:({STOCK}: {change}%){headline}\n\n{brief}"
            )
