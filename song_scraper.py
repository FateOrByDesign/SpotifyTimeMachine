import requests
import lxml
from bs4 import BeautifulSoup

class SongScraper:
    def __init__(self, date):
        self.date = date

    def scrape_billboard_to_get_top_100(self):
        """Class scrpes the billboards website and returns top 100 songs"""
        url = f"https://appbrewery.github.io/bakeboard-hot-100/{self.date}/"
        response = requests.get(url=url)

        soup = BeautifulSoup(response.text, "lxml")
        songs = soup.find_all(name="h3", class_="chart-entry__title")
        artists = soup.find_all(name="span", class_="chart-entry__artist")
        top_100_songs = {}

        for rank in range(len(songs)):
            song = songs[rank].get_text().strip()
            artist = artists[rank].get_text().strip()
            top_100_songs[song] = artist

        return top_100_songs

