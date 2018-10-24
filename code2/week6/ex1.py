import json

data = '''{
    "name" : "Jose",
    "phone" : {
        "type" : "intl",
        "number" : "+34 666 112 233"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name: ', info["name"])
print('Hide: ', info["email"]["hide"])
