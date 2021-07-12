from bs4 import BeautifulSoup
import requests

print("Welcome to the time travelling playlist app")
date = input("Pick a date, any date, type in the format YYYY-MM-DD")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, "html.parser")
song_names_pull = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_pull]

print(song_names)