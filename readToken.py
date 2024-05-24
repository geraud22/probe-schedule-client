import json

def readToken():
    with open(f"token.json", 'r') as json_file:
        jsonObject = json.load(json_file)
        token = jsonObject['token']
    return token