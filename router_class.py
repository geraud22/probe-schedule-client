import argparse
import os
class Router:
    def __init__(this, client) -> None:
        this.client = client
        
        parser = this.__createParser()
        args = parser.parse_args()
        this.endpoint = args.endpoint
        this.id = args.id
        this.requires_id = False
        this.function_collection = {
            "login": (this.client.login, False),
            "farmlist": (this.client.getFarmList, False),
            "blocklist": (this.client.getBlockList, True),
            "devicelist": (this.client.getDeviceList, True),
            "devicestatus": (this.client.getDeviceStatus, True),
            "devicedata": (this.client.getDeviceData, True)
        }
        
    def __createParser(this) -> object:
        parser = argparse.ArgumentParser(description="ProbeSchedule API Client")
        parser.add_argument('endpoint', 
                        type=str, 
                        help="Choose an API Endpoint to access",
                        choices=[
                            'login',
                            'farmlist',
                            'blocklist',
                            'devicelist',
                            'devicestatus',
                            'devicedata',
                        ])
    
        parser.add_argument('id',
                    nargs='?',
                    type=str,
                    help="ID used for relevant endpoint")
        return parser
    
    def __checkValidCommand(this) -> None:
        if this.endpoint not in this.function_collection:
            raise ValueError(f"Unknown command: {this.endpoint}")
        
    def __checkId(this) -> None:
        if this.requires_id and this.id == None:
            raise ValueError(f"Please provide an ID for '{this.endpoint}'")
        elif not this.requires_id and this.id != None:
            raise ValueError(f"Please call this endpoint without an ID: '{this.endpoint}'") 
        
    def __loginIfNeeded(this) -> None:
        if this.client.shouldLogin and this.endpoint == 'login':
            return
        elif this.client.shouldLogin and this.endpoint != 'login':
            raise ValueError(f"No token available. Please obtain one via the 'login' command.")
                       
    
    def route(this) -> None:
        this.__checkValidCommand()
        (method, this.requires_id) = this.function_collection[this.endpoint]
        this.__checkId()
        this.__loginIfNeeded()
        if this.requires_id:
            method(this.id)
            return 
        method()
            