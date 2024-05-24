import requests
import json
from makeJsonFile import makeJsonFile
from readToken import readToken

def getAvailableFarmList():
    headers = {
        "authorization": f"Bearer {readToken()}"
        }
    r = requests.get("https://api.probeschedule.co.za/data_api/v3/farms/list", headers=headers)
    response = r.content.decode('utf-8')
    return response

if __name__ == "__main__":
    response = getAvailableFarmList()
    jsonResponse = json.loads(response)
    makeJsonFile(jsonResponse)