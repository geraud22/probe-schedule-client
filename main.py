import argparse
import sys
import ps_client

print("Welcome to the Probe Schedule API Client.")

if __name__ == "__main__":
    quit = False
    while not quit:
        user_input = input("Your choice: ")
            
        if user_input.lower() != 'q':
            pass    
        
        quit = True
        print("Goodbye.")
