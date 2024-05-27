from router_class import Router
from ps_client_class import PS_CLient

def routeArgs(args, client):
        
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
    
    args = parser.parse_args()
    client = PS_CLient() 
    routeArgs(args, client)
    return None

if __name__ == "__main__":
    main()