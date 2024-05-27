import argparse

class Router:
    def __init__(this, client) -> None:
        this.parser = this.createParser()
        this.args = this.parser.parseArgs()
        this.client = client
        this.function_collection = {
            "login": this.client.login,
            "farmlist": this.client.getFarmList,
            "blocklist": this.client.getBlockList,
            "devicelist": this.client.getDeviceList,
            "devicestatus": this.client.getDeviceStatus,
            "devicedata": this.client.getDeviceData
        }
        this.positional_arguments = [
            "login",
            "farmlist",
            "blocklist",
            "devicelist",
            "devicestatus",
            "devicedata"
        ]
        
    def createParser(this):
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
    
    def go(this):
        if this.client.notLoggedIn():
            print("No Token Available, please login first: ")
            this.client.login()
        this.routeArgs()
        return None
            