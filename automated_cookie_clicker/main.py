#!/usr/bin/env python3

# Aleksandr Verevkin
# Script for auto cookie clicking
from time import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
LINK = "http://orteil.dashnet.org/experiments/cookie/"  # Game link
DRIVER_PATH = "/home/Verevkin/bin/chromedriver"  # Chromedriver path
CLICKING_TIME_SEC = 60 * 5


def clicker_start(driver):
    cookie = driver.find_element(By.ID, "cookie")
    items = driver.find_elements(By.CSS_SELECTOR, "#store div")
    item_ids = [item.get_attribute("id") for item in items]

    internal_timer = time() + CLICKING_TIME_SEC
    time_check = time() + 5  # +5 sec
    while time() < internal_timer:
        cookie.click()
        if time() > time_check:
            money = int(driver.find_element(By.ID, "money").text.replace(",", ""))  # Scrap current amount of cookies
            all_prices = [int(item.text.split()[-1].replace(",", "")) for item in driver.find_elements(By.CSS_SELECTOR, "#store b")[:-1]]
            for index, price in reversed(list(enumerate(all_prices))):  # Check for affordable items
                if price <= money:
                    driver.find_element(By.ID, item_ids[index]).click()
                    break
            time_check = time() + 5  # increase counter by 5 sec more
    print(f"Your final cookies amount is: {driver.find_element(By.ID, 'money').text.replace(',', '')}")


def main():
    driver = webdriver.Chrome(service=Service(DRIVER_PATH))
    driver.get(LINK)
    clicker_start(driver)
    driver.quit()


if __name__ == "__main__":
    main()
