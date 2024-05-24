import argparse
from ps_client_class import PS_CLient
import os

def loggedIn():
    if os.path.exists("token.json"):
        with open("token.json", 'r') as json_file:
            if json_file.read():
                return True
    return False

def routeArgs(args, client):
    function_collection = {
        "blocklist": client.getBlockList,
        "devicelist": client.getDeviceList,
        "devicestatus": client.getDeviceStatus,
        "devicedata": client.getDeviceData
    }
    
    positional_arguments = [
        "blocklist",
        "devicelist",
        "devicestatus",
        "devicedata"
    ]
    
    if args.endpoint != 'farmlist':
        for pos_arg in positional_arguments:
            if args.endpoint == pos_arg:
                if args.id:
                    function_collection[pos_arg](args.id)
                    return None
                else:
                    print(f"Error: Please provide a device ID for {pos_arg}.")
                    return None
    
    if args.id:
        print(f"Error: farmlist does not accept any additional arguments.")
        return None
        
    client.getFarmList()
    return None

def main():
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
    args = parser.parse_args()
    client = PS_CLient()
    
    if args.endpoint == 'login':
        if args.id:
            print(f"Error: login does not accept any additional arguments.")
        client.login()
    
    if not loggedIn():
        print("No Token Available, please login...")
        client.login()
    
    routeArgs(args, client)

if __name__ == "__main__":
    main()