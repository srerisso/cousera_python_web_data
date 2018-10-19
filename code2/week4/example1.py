import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#URL = "http://www.espn.com/nba/statistics"
URL = "example1.html"

with open("example1.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# Give me a list of all the anchor tags
anchorTags = soup('a')
for tag in anchorTags:
    print(tag.get('href', None))
