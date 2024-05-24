import argparse
import sys
from ps_client import PS_CLient

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
                            'devicestatus'
                        ])
    args = parser.parse_args()
    client = PS_CLient()
    
    if args.endpoint == 'farmlist':
        client.getFarmList()
    if args.endpoint == 'login':
        client.login()
    if args.endpoint == 'blocklist':
        client.getBlockList()
    if args.endpoint == 'devicelist':
        client.getDeviceList()
    if args.endpoint == 'devicestatus':
        client.getDeviceStatus()

if __name__ == "__main__":
    main()