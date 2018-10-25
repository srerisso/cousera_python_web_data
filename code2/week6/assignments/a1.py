import urllib.request
import json

# promot for a file
while True:
    file = input('Enter location: ')

    if (len(file) < 1): break

    # read the JSON data using urllib
    uh = urllib.request.urlopen(file)
    print('Retrieving', file)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    jdata = json.loads(data)
    # parse and extract the comment counts from the JSON cousera_python_web_data
    count = 0
    sum = 0

    for commentInfo in jdata["comments"]:
        # print('Name: ', commentInfo["name"])
        # print('Count: ', commentInfo["count"])
        # compute the sum of numbers and print Count and Sum.
        sum = sum + commentInfo["count"]
        count = count +1

    print('Total: ', count)
    print('Sum: ', sum)
