#! python3
# searchpypi.py - opens search results

import requests
import sys
import webbrowswer
import bs4

print("Searching...")  # display text while downloading the search result page
res = requests.get(
    "https://google.com/search?q="
    "https://pypi.org/search/?q=" + " ".join(sys.argv[1:])
)
res.raise_for_status()
