import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from secrets import CLIENT_ID, CLIENT_SECRET
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.search(q='bastille', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print (' ', i, t['name'])
