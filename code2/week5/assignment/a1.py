import urllib.request
import xml.etree.ElementTree as ET

while True:
    fileData = input('Enter file: ')
    if len(fileData) < 1: break

    uh = urllib.request.urlopen(fileData)
    print('Retrieving', fileData)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('comments')
    for child in results:
      print(child.find('count').text
    

    #print(results.get_value)
