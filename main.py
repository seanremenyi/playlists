from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=xx,
        client_secret=xx,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

print("Welcome to the time travelling playlist app")
date = input("Pick a date, any date, type in the format YYYY-MM-DD")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, "html.parser")
song_names_pull = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_pull]

print(song_names)