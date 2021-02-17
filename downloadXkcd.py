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
