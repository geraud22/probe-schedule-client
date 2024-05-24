import requests
import json

class PS_CLient:
    def __init__(this):
        this.farm_id = 0
        this.filename = ''
        this.device_id = ''

    def __str__(this):
        pass
    
    def __readToken(this):
        # Returns String
        with open("token.json", 'r') as json_file:
            jsonObject = json.load(json_file)
            token = jsonObject['token']
        return token
    
    def __makeJsonFile(this, response):
        # Returns None
        jsonData = json.loads(response)
        with open(f"{this.filename}.json", 'w') as json_file:
            json.dump(jsonData, json_file, indent=4)
        print(f"Received Data has been saved to {this.filename}.json")
        
    def __requestUserDetails(this):
        # Returns a Dictionary
        userDetails = {}
        userDetails['username'] = input("Please enter your username: ")
        userDetails['password'] = input("Please enter your password: ")
        return userDetails
    
    def __returnAvailableEndpoints(this):
        pass
    
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
        jsonResponse = json.loads(response)
        token = {
            "token": jsonResponse['data']['token']
        }
        this.__makeJsonFile(token)
        return None
    
    def getFarmList(this):
        this.filename = "farmlist"
        headers = {
            "authorization": f"Bearer {this.__readToken()}"
            }
        r = requests.get("https://api.probeschedule.co.za/data_api/v3/farms/list", headers=headers)
        response = r.content.decode('utf-8')
        this.__makeJsonFile(response)
        return None
    
    def getBlockList(this):
        this.filename = "blocklist"
        this.farm_id = input("Enter Farm ID: ")
        headers = {"authorization": f"Bearer {this.__readToken()}"}
        r = requests.get(f"https://api.probeschedule.co.za/data_api/v3/farms/{this.farm_id}/blocks", headers=headers)
        response = r.content.decode('utf-8')
        this.__makeJsonFile(response)
        return None
    
    def getDeviceList(this):
        this.filename = "devicelist"
        this.farm_id = input("Enter Farm ID: ")
        headers = {"authorization": f"Bearer {this.__readToken()}"}
        r = requests.get(f"https://api.probeschedule.co.za/data_api/v3/farms/{this.farm_id}/devices", headers=headers)
        response = r.content.decode('utf-8')
        this.__makeJsonFile(response)
        return None
    
    def getDeviceStatus(this):
        this.filename = "devicestatus"
        this.device_id = input("Enter Device ID: ")
        headers = {"authorization": f"Bearer {this.__readToken()}"}
        r = requests.get(f"https://api.probeschedule.co.za/data_api/v3/devices/{this.device_id}/status", headers=headers)
        response = r.content.decode('utf-8')
        this.__makeJsonFile(response)
        return None