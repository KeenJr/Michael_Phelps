# main.py

import json
import requests
from iterateOverADictionaryPackage.iterateOverADictionary import *

response = requests.get('https://developer.nps.gov/api/v1/parks?parkCode=acad&api_key=pfJKDXPzTykVL73ehnPyY8pkDQLjfq5cz5LqCkl3')
json_string = response.content
    
parsed_json = json.loads(json_string) # Now we have a python dictionary

#print(parsed_json)
#print(parsed_json['data'][0]['description'])
#print(parsed_json['data'][0]['directionsInfo'])
    
#total = int(parsed_json['total'])        # The number of parks that were returned
    
#for park in parsed_json['data']:
#    print (park["description"])

iterate_dictionary(parsed_json)
