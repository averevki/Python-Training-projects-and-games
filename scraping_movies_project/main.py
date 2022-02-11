#!/usr/bin/env python3

# Aleksandr Verevkin
# Scraping movies from the empire article and putting names in the separate .txt
from bs4 import BeautifulSoup
import requests
ARTICLE = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


def main():
    content = requests.get(ARTICLE).text
    soup = BeautifulSoup(content, "html.parser")

    titles = [title.getText() for title in soup.find_all("h3", class_="title")]
    titles.reverse()
    titles_str = "\n".join(titles)
    with open("movies.txt", "w") as f:
        f.write(titles_str)


if __name__ == "__main__":
    main()
