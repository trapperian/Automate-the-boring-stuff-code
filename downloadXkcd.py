#! python3
# downloadXkcd.py - downloads every XKCD comic via previous button

import requests
import os
import bs4

url = "https://xkcd.com"

os.makedirs("xkcd", exist_ok=True)

while not url.endswith("#"):
    pass
