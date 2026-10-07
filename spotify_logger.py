import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyLogger:
    def __init__(self, top_100_songs: list, client_id, client_secret, redirect_url, date):
        self.top_100_songs = top_100_songs
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_url = redirect_url
        self.date = date
        self.song_uri = []
        self.sp_object = self.authenticate_spotify_return_spotipy_object()


    def authenticate_spotify_return_spotipy_object(self):
        """Authenticates spotify and returns a spotipy object"""
        scope = "playlist-modify-private"
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                                       client_id=self.client_id,
                                                       client_secret=self.client_secret,
                                                       redirect_uri=self.redirect_url))
        return sp

    def get_all_song_uri_for_top_100_songs(self):
        """return a list of spotify song URI's of all 100 songs"""
        for item in self.top_100_songs:
            song = item[0]
            artist = item[1]
            if "Featuring" in artist:
                artist = artist.split("Featuring")[0].strip()
            if " x " in artist:
                artist = artist.split(" x ")[0].strip()
            query = f"track:{song} artist:{artist}"
            data = self.sp_object.search(q=query, type="track", limit=1)["tracks"]["items"]
            try:
                data = data[0]["uri"]
                self.song_uri.append(data)
            except IndexError:
                print(f"{song}, {artist}: Skipped")
                continue

    def create_private_playlist_and_add_songs(self):
        playlist_id = self.sp_object.current_user_playlist_create(
            name=f"{self.date} Billboard 100",
            public=False,)["id"]
        response = self.sp_object.playlist_add_items(playlist_id=playlist_id, items=self.song_uri)
        print(response)