#!/usr/bin/env python3

# Aleksandr Verevkin
# Bot for automated following all followers of given page
# Using python selenium
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv      # load variables from local environment
DRIVER_PATH = "/home/Verevkin/bin/chromedriver"  # Chromedriver path
LINK = "https://www.instagram.com/dababy/"  # instagram user page link
load_dotenv()       # load variables from local environment
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


class InstaFollower:
    def __init__(self):
        """Initialize chromedriver path and open chrome browser"""
        self.driver = webdriver.Chrome(service=Service(DRIVER_PATH))
        self.driver.get(LINK)
        self.driver.maximize_window()
        self.pop_up_window = None
        try:
            self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]").click()
        except NoSuchElementException:
            pass

    def login(self):
        """Login into your instagram account"""
        email_field = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        email_field.send_keys(EMAIL)
        password_field = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        password_field.send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button").click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div/section/div/button"))).click()

    def find_followers(self):
        """Find and click on the 'following'"""
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "follower"))).click()
        self.pop_up_window = WebDriverWait(self.driver, 2).until(ec.element_to_be_clickable((By.XPATH, "//div[@class='isgrP']")))

    def follow(self):
        """Follow every user in the pop-up 'following'"""
        index = 1
        div = 3
        while True:
            try:
                self.driver.find_element(By.XPATH, f"/html/body/div[6]/div/div/div/div[2]/ul/div/li[{index}]/div/div[{div}]/button/div").click()
                print(f"{index} follow")
                index += 1
                sleep(1)
            except NoSuchElementException:      # Scrolling popup down
                for _ in range(2):
                    self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', self.pop_up_window)
                sleep(3)
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', self.pop_up_window)
                div = 2
            except ElementClickInterceptedException:    # Cancel if already following
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


def main():
    bot = InstaFollower()
    bot.login()
    bot.find_followers()
    bot.follow()
    bot.driver.quit()


if __name__ == "__main__":
    main()
