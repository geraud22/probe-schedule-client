import argparse
class Router:
    def __init__(this, client) -> None:
        this.parser = this.createParser()
        this.args = this.parser.parse_args()
        this.client = client
        this.function_collection = {
            "login": (this.client.login, False),
            "farmlist": (this.client.getFarmList, False),
            "blocklist": (this.client.getBlockList, True),
            "devicelist": (this.client.getDeviceList, True),
            "devicestatus": (this.client.getDeviceStatus, True),
            "devicedata": (this.client.getDeviceData, True)
        }
        
    def createParser(this) -> object:
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
    
    def routeArgs(this) -> None:
        if this.args.endpoint not in this.function_collection:
            raise ValueError(f"Unknown command: {this.args.endpoint}")
        method, requires_id = this.function_collection[this.args.endpoint]
        
        if requires_id and this.args.id == None:
            raise ValueError(f"Please provide an ID for '{this.args.endpoint}'")
        elif not requires_id and this.args.id != None:
            raise ValueError(f"Please call this endpoint without an ID: '{this.args.endpoint}'")
        
        if requires_id:
            method(this.args.id)
            return None
        
        method()
        return None
    
    def go(this):
        if this.client.notLoggedIn():
            print("No Token Available, please login first: ")
            this.client.login()
        this.routeArgs()
        return None
            