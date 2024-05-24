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

    if not loggedIn():
        print("No Token Available, please login...")
        client.login()
        
    for pos_arg in positional_arguments:
        if pos_arg == args.endpoint:
            if args.id:
                function_collection[pos_arg](args.id)
                return None
            print(f"Error: Please provide a device ID for {pos_arg}.")
            return None
        if args.endpoint == 'farmlist':
            if args.id:
                print(f"Error: farmlist does not accept any additional arguments.")
                return None
            client.getFarmList()
        if args.endpoint == 'login':
            if args.id:
                print(f"Error: login does not accept any additional arguments.")
                return None
            client.login()
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
    routeArgs(args, client)
    return None

if __name__ == "__main__":
    main()