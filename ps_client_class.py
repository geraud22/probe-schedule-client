import requests
import json

class PS_CLient:
    def __init__(this):
        this.farm_id = 0
        this.device_id = 0
        this.filename = ''
        this.url = ''
        this.response = ''
    
    def __readToken(this):
        with open("token.json", 'r') as json_file:
            jsonObject = json.load(json_file)
            token = jsonObject['data']['token']
        return token
    
    def __makeJsonFile(this):
        jsonData = json.loads(this.response)
        with open(f"{this.filename}.json", 'w') as json_file:
            json.dump(jsonData, json_file, indent=4)
        print(f"Received Data has been saved to {this.filename}.json")
        return None
        
    def __requestUserDetails(this):
        userDetails = {}
        userDetails['username'] = input("Please enter your username: ")
        userDetails['password'] = input("Please enter your password: ")
        return userDetails
    
    def __makeRequest(this):
        headers = {"authorization": f"Bearer {this.__readToken()}"}
        r = requests.get(f"{this.url}", headers=headers)
        this.response = r.content.decode('utf-8')
        this.__makeJsonFile()
        return None
    
    def login(this):
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
        response = r.content.decode('utf-8')
        this.__makeJsonFile(response)
        return None
    
    def getFarmList(this):
        this.filename = "farmlist"
        this.url = "https://api.probeschedule.co.za/data_api/v3/farms/list"
        this.__makeRequest()
        return None
    
    def getBlockList(this):
        this.filename = "blocklist"
        this.farm_id = input("Enter Farm ID: ")
        this.url = f"https://api.probeschedule.co.za/data_api/v3/farms/{this.farm_id}/blocks"
        this.__makeRequest()
        return None
    
    def getDeviceList(this):
        this.filename = "devicelist"
        this.farm_id = input("Enter Farm ID: ")
        this.url = f"https://api.probeschedule.co.za/data_api/v3/farms/{this.farm_id}/devices"
        this.__makeRequest()
        return None
    
    def getDeviceStatus(this, deviceId):
        this.filename = "devicestatus"
        this.device_id = deviceId
        this.url = f"https://api.probeschedule.co.za/data_api/v3/devices/{this.device_id}/status"
        this.__makeRequest()
        return None
    
    def getDeviceData(this):
        this.filename = "devicedata"
        this.device_id = input("Enter Device ID: ")
        this.url = f"https://api.probeschedule.co.za/data_api/v3/devices/{this.device_id}/data"
        this.__makeRequest()
        return None