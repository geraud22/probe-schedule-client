import json

def makeJsonFile(jsonData):
    fileName = input("File Name excluding File Extension? ")
    with open(f"{fileName}.json", 'w') as json_file:
        json.dump(jsonData, json_file, indent=4)
    print(f"Received Data has been saved to {fileName}.json")