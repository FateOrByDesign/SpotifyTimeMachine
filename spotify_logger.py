import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyLogger:
    def __init__(self, top_100_songs: dict, client_id, client_secret, redirect_url):
        self.top_100_songs = top_100_songs
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_url = redirect_url


    def authenticate_spotify_return_spotipy_object(self):
        """Authenticates spotify and returns a spotipy object"""
        scope = "playlist-modify-private"
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                                       client_id=self.client_id,
                                                       client_secret=self.client_secret,
                                                       redirect_uri=self.redirect_url))
        return sp
