from dotenv import load_dotenv
import os
from song_scraper import SongScraper
from spotify_logger import SpotifyLogger

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URL = os.getenv("SPOTIFY_REDIRECT_URL")
if not SPOTIFY_CLIENT_ID: raise ValueError("Error: Something went wrong loading the SPOTIFY_CLIENT_ID.")
if not SPOTIFY_CLIENT_SECRET: raise ValueError("Error: Something went wrong loading the SPOTIFY_CLIENT_SECRET.")
if not SPOTIFY_REDIRECT_URL: raise ValueError("Error: Something went wrong loading the SPOTIFY_REDIRECT_URL.")


def main():
    # Get the date from the user to search on billboard | test date : 2020-08-15
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

    song_scraper = SongScraper(date)
    # get the top 100 songs of the given date
    top_100_songs = song_scraper.scrape_billboard_to_get_top_100()
    spotify_logger = SpotifyLogger(top_100_songs, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URL, date)
    spotify_logger.get_all_song_uri_for_top_100_songs()
    spotify_logger.create_private_playlist_and_add_songs()

if __name__ == "__main__":
    main()
