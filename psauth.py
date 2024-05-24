import requests
import json

def requestUserDetails():
    userDetails = {}
    userDetails['username'] = input("Please enter your username: ")
    userDetails['password'] = input("Please enter your password: ")
    return userDetails

def returnBearerToken():
    userDetails = requestUserDetails()
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
    return response
    
if __name__ == "__main__":
    response = returnBearerToken()
    jsonResponse = json.loads(response)
    print("Token: ", jsonResponse['data']['token'])