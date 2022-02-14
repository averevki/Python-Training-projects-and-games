#!/usr/bin/env python3

# Aleksandr Verevkin
# Bot for automated scraping data from estate website and put data into google forms
# Using python beautiful soup and selenium
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from typing import List

DRIVER_PATH = "/home/Verevkin/bin/chromedriver"  # Chromedriver path
FORM_LINK = "https://forms.gle/rScaK8WfWaC1Wbhd8"
ZILLOW_LINK = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22users" \
              "SearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.303896" \
              "32177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3" \
              "Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afals" \
              "e%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B" \
              "%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D" \
              "%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%" \
              "22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isList" \
              "Visible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
BROWSER_USER_AGENT = "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"
BROWSER_ACCEPT_LANGUAGE = "en-US,en;q=0.5"
HEADERS = {
    "User-Agent": BROWSER_USER_AGENT,
    "Accept-Language": BROWSER_ACCEPT_LANGUAGE
}


class ZillowScraping:
    def __init__(self) -> None:
        self.links = None
        self.prices = None
        self.addresses = None
        content = requests.get(url=ZILLOW_LINK, headers=HEADERS).text
        self.soup = BeautifulSoup(content, "html.parser")

    def scrap_links(self) -> None:
        links = [link['href'] for link in self.soup.find_all(class_="list-card-link", href=True)]
        self.links = [f"https://www.zillow.com{link}" if link[0] == '/' else link for link in links]

    def scrap_prices(self) -> None:
        self.prices = [price.text for price in self.soup.find_all(class_="list-card-price")]

    def scrap_addresses(self) -> None:
        self.addresses = [address.text for address in self.soup.find_all("address")]


class FormFilling:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(DRIVER_PATH))
        self.driver.get(FORM_LINK)
        self.driver.maximize_window()

    def fill_forms(self, addresses: List, prices: List, links: List) -> None:
        for address, price, link in zip(addresses, prices, links):
            address_field = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH,
                                                                                             "/html/body/div/div["
                                                                                             "2]/form/div[2]/div/div["
                                                                                             "2]/div[1]/div/div/div["
                                                                                             "2]/div/div[1]/div/div["
                                                                                             "1]/input")))
            address_field.send_keys(address)
            price_field = self.driver.find_element(By.XPATH,
                                                   "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div["
                                                   "2]/div/div[1]/div/div[1]/input")
            price_field.send_keys(price)
            link_field = self.driver.find_element(By.XPATH,
                                                  "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div["
                                                  "2]/div/div[1]/div/div[1]/input")
            link_field.send_keys(link)
            self.driver.find_element(By.XPATH,
                                     "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span").click()
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Odeslat dal"))).click()


def main():
    scrapping = ZillowScraping()
    scrapping.scrap_addresses()
    scrapping.scrap_prices()
    scrapping.scrap_links()
    forms = FormFilling()
    forms.fill_forms(scrapping.addresses, scrapping.prices, scrapping.links)
    forms.driver.quit()


if __name__ == "__main__":
    main()
