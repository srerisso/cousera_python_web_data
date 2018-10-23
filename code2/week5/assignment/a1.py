import xml.etree.ElementTree as ET

while True:
    fileData = input('Enter location: ')
    if len(fileData) < 1: break

    url = urllib.parse.urlencode({'File': fileData})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('comments')

    print(results)
