import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# this makes the host think the requests are coming from a browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}


def get_content(address):
    # getting content from an url
    req = requests.get(address, headers=headers)
    page = BeautifulSoup(req.text, "html.parser")
    return page


artist = input("artist: ").replace(" ", "").lower()
url = 'https://www.azlyrics.com/'

# getting the artist page
artist_url = urljoin(url, '/b/%s.html' % artist)

soup = get_content(artist_url)
# get all href links that match the 'lyrics/someartist' path
songs = soup.select("a[href*=lyrics/%s]" % artist)

# now we can iterate through all their songs and get the lyrics
all_lyrics = ''
for song in songs:
    song_url = urljoin(url, song['href'])
    soup = get_content(song_url)
    for lyrics in soup.find_all("div", class_=None):
        all_lyrics += lyrics.text

# starting and showing the wordcloud
wordcloud = WordCloud(width=800, height=600).generate(''.join(all_lyrics))
plt.figure(figsize=(15, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
