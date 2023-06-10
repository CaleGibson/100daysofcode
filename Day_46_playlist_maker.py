from bs4 import BeautifulSoup
import requests
import spotipy
import pprint
from spotipy.oauth2 import SpotifyOAuth
SPOTIFY_ID = ""
SPOTIFY_SEC = ""
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                               client_id=SPOTIFY_ID,
                                               client_secret=SPOTIFY_SEC,
                                               redirect_uri="http://example.com",
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               ))



date = input("What date do you want to listen too? yyyy-mm-dd format: ")
year = date.split("-")[0]

URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(URL)
start = response.text
soup = BeautifulSoup(start, "html.parser")
info = soup.select("li ul h3")

song_names = [song.getText().strip() for song in info]
print(song_names)

id_list = []
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        id_list.append(uri)

    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=sp.current_user()["id"], name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=id_list)
