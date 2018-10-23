# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count - ')
position = input('Enter position - ')
#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
#url = "http://py4e-data.dr-chuck.net/known_by_Savin.html"
# Retrieve all of the anchor tags
i = 0
# print("Tags ", tags[2])
# print("URL: ", tags[2]['href']) # url
# print("Contents: ", str(tags[2].contents))

# Go fetch the 2nd, 3rd and 4th urls and extract the name
i = 0
nameList = []
count2 = int(count)
pos = int(position)

while i< count2:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    nameList.append(str(tags[pos-1].contents))
    url = tags[pos-1]['href']
    i=i+1

print(nameList)
