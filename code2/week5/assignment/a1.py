import urllib.request
import xml.etree.ElementTree as ET

while True:
    fileData = input('Enter file: ')
    if len(fileData) < 1: break

    uh = urllib.request.urlopen(fileData)
    print('Retrieving', fileData)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    tree = ET.fromstring(data)
    comments = tree.findall('comments')
    #  find count for all comments
    countTotal = 0
    i = 0
    for comentario in comments:
        for comentarioData in comentario.findall('comment'):
            count = comentarioData.find('count').text
            name = comentarioData.find('name').text
            # print(name, count)
            countTotal = countTotal + int(count)
            i = i+1
        print('Count: ', i)
        print('Sum: ', countTotal)
