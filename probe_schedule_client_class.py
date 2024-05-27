import requests
import json
import os

class PS_CLient:
    def __init__(this) -> None:
        this.shouldLogin = this.__shouldLogin()
        this.id = 0
        this.filename = ''
        this.url = ''
        this.response = ''
        
    def __shouldLogin(this) -> bool:
        if os.path.exists("token.json"):
            with open("token.json", 'r') as json_file:
                if json_file.read():
                    return False
        return True
    
    def __readToken(this) -> str:
        with open("token.json", 'r') as json_file:
            jsonObject = json.load(json_file)
            token = jsonObject['data']['token']
        return token
    
    def __makeJsonFile(this) -> None:
        jsonData = json.loads(this.response)
        if not jsonData['success']:
                raise ValueError(f"Authentication Failed.")
        with open(f"{this.filename}.json", 'w') as json_file:
            json.dump(jsonData, json_file, indent=4)
        print(f"Received Data has been saved to {this.filename}.json")
        
    def __requestUserDetails(this) -> dict:
        userDetails = {}
        userDetails['username'] = input("Please enter your Probe Schedule username: ")
        userDetails['password'] = input("Please enter your Probe Schedule password: ")
        return userDetails
    
    def __makeRequest(this) -> None:
        headers = {"authorization": f"Bearer {this.__readToken()}"}
        r = requests.get(f"{this.url}", headers=headers)
        this.response = r.content.decode('utf-8')
        this.__makeJsonFile()
    
    def login(this) -> None:
        this.filename = "token"
        userDetails = this.__requestUserDetails()
        dataObject = {
            "type": "login",
            "data": {
                "username": f"{userDetails['username']}",
                "password": f"{userDetails['password']}"
            }
        } 
        headers = {"content-type": "application/json"}
        r = requests.post("https://api.probeschedule.co.za/data_api/v3/token", 
                        headers=headers, 
                        json=dataObject
                        )
        this.response = r.content.decode('utf-8')
        this.__makeJsonFile()
    
    def getFarmList(this) -> None:
        this.filename = "farmlist"
        this.url = "https://api.probeschedule.co.za/data_api/v3/farms/list"
        this.__makeRequest()
    
    def getBlockList(this, farmId) -> None:
        this.id = farmId
        this.filename = f"{farmId}-blocklist"
        this.url = f"https://api.probeschedule.co.za/data_api/v3/farms/{this.id}/blocks"
        this.__makeRequest()
    
    def getDeviceList(this, farmId) -> None:
        this.id = farmId
        this.filename = f"{farmId}-devicelist"
        this.url = f"https://api.probeschedule.co.za/data_api/v3/farms/{this.id}/devices"
        this.__makeRequest()
    
    def getDeviceStatus(this, deviceId) -> None:
        this.id = deviceId
        this.filename = f"{deviceId}-devicestatus"
        this.url = f"https://api.probeschedule.co.za/data_api/v3/devices/{this.id}/status"
        this.__makeRequest()
    
    def getDeviceData(this, deviceId) -> None:
        this.id = deviceId
        this.filename = f"{deviceId}-devicedata"
        this.url = f"https://api.probeschedule.co.za/data_api/v3/devices/{this.id}/data"
        this.__makeRequest()