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

# retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")
# open a browser tab for each result.
linkElems = soup.select(".package-snippet")
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = "https://pypi.org" + linkElems[i].get("href")
    print("Opening", urlToOpen)
    webbrowser.open(urlToOpen)
