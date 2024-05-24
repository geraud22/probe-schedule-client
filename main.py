import argparse
import sys
from ps_client import PS_CLient
import os

def loggedIn():
    if os.path.exists("token.json"):
        with open("token.json", 'r') as json_file:
            if json_file.read():
                return True
    return False

def routeArgs(args, client):
    if args.endpoint == 'farmlist':
        client.getFarmList()
    if args.endpoint == 'blocklist':
        client.getBlockList()
    if args.endpoint == 'devicelist':
        client.getDeviceList()
    if args.endpoint == 'devicestatus':
        client.getDeviceStatus()
    if args.endpoint == 'devicedata':
        client.getDeviceData()

def main():
    parser = argparse.ArgumentParser(description="ProbeSchedule API Client")
    parser.add_argument('endpoint', 
                        type=str, 
                        help="The API Endpoint to access",
                        choices=[
                            'farmlist',
                            'login',
                            'blocklist',
                            'devicelist',
                            'devicestatus',
                            'devicedata',
                        ])
    args = parser.parse_args()
    client = PS_CLient()
    
    if args.endpoint == 'login':
        client.login()
    
    if not loggedIn():
        print("No Token Available, please login...")
        client.login()
    
    routeArgs(args, client)

if __name__ == "__main__":
    main()