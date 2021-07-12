from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


print("""  __  .__                        ___.                  __           __  .__                          
_/  |_|  |_________  ______  _  _\_ |__ _____    ____ |  | __     _/  |_|  |__  __ _________  ______ 
\   __\  |  \_  __ \/  _ \ \/ \/ /| __ \\__  \ _/ ___\|  |/ /     \   __\  |  \|  |  \_  __ \/  ___/ 
 |  | |   Y  \  | \(  <_> )     / | \_\ \/ __ \\  \___|    <       |  | |   Y  \  |  /|  | \/\___ \  
 |__| |___|  /__|   \____/ \/\_/  |___  (____  /\___  >__|_ \      |__| |___|  /____/ |__|  /____  > 
           \/                         \/     \/     \/     \/                \/                  \/""")
date = input("Pick a date, any date, type in the format YYYY-MM-DD\n")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, "html.parser")
song_names_pull = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_pull]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="",
        client_secret="",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pass

playlist = sp.user_playlist_create(user=user_id, name=f"Throwback Thurs {date}", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)