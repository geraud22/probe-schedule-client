from probe_schedule_client_class import PS_CLient
from router_class import Router

if __name__ == "__main__":
    try:
        client = PS_CLient()
        router = Router(client)
        router.route()
    except ValueError as v:
        print(f"Error: {v}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        