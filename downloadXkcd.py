#! python3
# downloadXkcd.py - downloads every XKCD comic via previous button

import requests
import os
import bs4

url = "https://xkcd.com"

os.makedirs("xkcd", exist_ok=True)

while not url.endswith("#"):
    # download the page.
    print("Downloading page %s..." % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Find the url of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find the comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
