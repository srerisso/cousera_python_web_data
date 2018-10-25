import urllib.request, urllib.parse, urllib.error
import json

# contact web service and retrieve json
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    # prompt for a location
    address = input('Enter location: ')
    if len(address) < 1: break

    # parse the JSON data
    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # print(json.dumps(js, indent=4))

    # retrieve the first place_id from the JSON
    print('Place id ', js["results"][0]["place_id"])
