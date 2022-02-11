#!/usr/bin/env python3

# Aleksandr Verevkin
# Program that creating playlist from hot-100 billboard songs for given date
import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
SPOTIFY_ID = os.getenv("SPOTIFY_ID")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")
LINK = "https://www.billboard.com/charts/hot-100"


def main():
    date = input("Input date of 'hot 100' in format: YYYY-MM-DD\nDate: ")
    date_link = f"{LINK}/{date}"

    response = requests.get(date_link)
    response.raise_for_status()
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    # Creating list with song titles
    songs_list = [song.getText().strip() for song in soup.select(selector="li ul li h3", id="title-of-a-story")]

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=SPOTIFY_ID,
            client_secret=SPOTIFY_ID,
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    user_id = sp.current_user()["id"]
    # Songs search
    uris = []
    for song in songs_list:
        try:
            uris.append(sp.search(q=f"track:{song}", type="track")["tracks"]["items"][0]["uri"])
        except Exception:  # Can't find song
            pass

    # Creating playlist and adding songs
    playlist = sp.user_playlist_create(user=user_id, name=f"{date} BILlBOARD HOT 100", public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=uris)


if __name__ == "__main__":
    main()
