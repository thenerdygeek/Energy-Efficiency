#!/usr/bin/python3
import urllib.request
# If you are using Python 2+, import urllib2 instead of urllib

import json

relative= input("\nEnter the Relative Compactness: ")
surface= input("\nEnter the Surface Area: ")
wall = input("\nEnter the Wall Area: ")
roof = input("\nEnter the Roof Area: ")
overall= input("\nEnter the Overall Height: ")
orientation= input("\nEnter Orientation: ")
glazing1= input("\nEnter the Glazing Area: ")
glazing2= input("\nEnter the Glazing Area Distribution: ")
data =  {

        "Inputs": {

                "input2":
                {
                    "ColumnNames": ["Relative Compactness", "Surface Area", "Wall Area", "Roof Area", "Overall Height", "Orientation", "Glazing Area", "Glazing Area Distribution"],
                    "Values": [ [ relative, surface, wall, roof, overall, orientation, glazing1, glazing2 ], ]
                },
                "input1":
                {
                    "ColumnNames": ["Relative Compactness", "Surface Area", "Wall Area", "Roof Area", "Overall Height", "Orientation", "Glazing Area", "Glazing Area Distribution"],
                    "Values": [ [ "0", "0", "0", "0", "0", "0", "0", "0" ], ]
                },        },
            "GlobalParameters": {
}
    }
data["Inputs"]["input1"]=data["Inputs"]["input2"]

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/d40075692ae645bf8c9108f6167c6b90/services/4f7e2a5c09b74bbd9a687cf3c6c8ab53/execute?api-version=2.0&details=true'
api_key = 'e+u07brLqtluLi3UGnEEkHUhUzmspkKHl860TTLF2/Jp9BrAriGsjVcqJPzuXKb47qDKEHYdSZGtZFR8f1anIw=='
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers) 

try:
    response = urllib.request.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    data = json.loads(result)
    print('\nHeating Load: ', data['Results']['output1']['value']['Values'][0][8])
    print('\nCooling Load: ', data['Results']['output1']['value']['Values'][0][17])

    #print(type(result))
    #print(result)
except urllib.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))
