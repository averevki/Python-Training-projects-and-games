#!/usr/bin/env python3

# Aleksandr Verevkin
# Script for determining your internet speed with selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
LINK = "https://www.speedtest.net/"              # Speed-test link
DRIVER_PATH = "/home/Verevkin/bin/chromedriver"  # Chromedriver path


def main():
    driver = webdriver.Chrome(service=Service(DRIVER_PATH))
    driver.get(LINK)
    sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[1]/div[5]/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]").click()
    sleep(45)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a").click()
    down_speed = driver.find_element(By.CLASS_NAME, "download-speed").text
    up_speed = driver.find_element(By.CLASS_NAME, "upload-speed").text
    print(f"Your download speed is {down_speed}\nYour upload speed is {up_speed}")
    driver.quit()


if __name__ == "__main__":
    main()
