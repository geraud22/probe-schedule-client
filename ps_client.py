import requests
import json

class PS_CLient:
    def __init__(this):
        pass

    def __str__(this):
        pass
    
    def __readToken(this, filename):
        # Returns String
        with open(f"{filename}.json", 'r') as json_file:
            jsonObject = json.load(json_file)
            token = jsonObject['token']
        return token
    
    def __makeJsonFile(this, jsonData, fileName):
        # Returns None
        with open(f"{fileName}.json", 'w') as json_file:
            json.dump(jsonData, json_file, indent=4)
        print(f"Received Data has been saved to {fileName}.json")
        
    def __requestUserDetails(this):
        # Returns a Dictionary
        userDetails = {}
        userDetails['username'] = input("Please enter your username: ")
        userDetails['password'] = input("Please enter your password: ")
        return userDetails
    
    def returnAvailableEndpoints(this):
        pass
    
    def retrieveBearerToken(this):
        filename = "token"
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
        this.__makeJsonFile(token, filename)
        return None
    
    def getAvailableFarmList(this):
        filename = "farmlist"
        headers = {
            "authorization": f"Bearer {this.__readToken(filename)}"
            }
        r = requests.get("https://api.probeschedule.co.za/data_api/v3/farms/list", headers=headers)
        response = r.content.decode('utf-8')
        this.__makeJsonFile(response, filename)
        return None