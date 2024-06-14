import json
import requests
import pandas as pd
from utils.api_ninja import get_zipcode

df = pd.read_csv("lanes.csv")
#1.-
# CREATE JSON OF ZIPCODES FROM CSV.
# cities = set()
# for indx in range(200): # FILL SET OF CITIES
#     origin = df.at[indx, "Origin"]
#     destination = df.at[indx, "Destination"]
#     # GET THE COUNTRIES TO GET ZIPCODES.
#     cities.add(origin.strip())
#     cities.add(destination.strip())

# zip_codes = dict()
# for location in cities:
#     loc_splitted = location.split(",")
#     city = loc_splitted[0].strip()
#     state = loc_splitted[1].strip()
#     zipcode = get_zipcode(city.title(), state)
#     zip_codes[location] = zipcode
    
# json_object = json.dumps(zip_codes, indent=4)
# with open("zipcodes.json", "w") as outfile:
#     outfile.write(json_object)

#1.-
# CREATE LANES OBJECT.
## ADD ZIPCODE AND EQUIPMENT_ID = 3 TO ALL LANES
# GET ZIPCODES
lanes = []
zipcodes_json = open("zipcodes.json")
zipcodes = json.load(zipcodes_json)
for indx in range(200):
    origin = df.at[indx, "Origin"]
    destination = df.at[indx, "Destination"]
    
    origin_zipcode = zipcodes[origin]
    destination_zipcode = zipcodes[destination]
    lane = {
        "origin_zipcode": origin_zipcode,
        "destination_zipcode": destination_zipcode,
        "equipment_id": 3,
    }
    lanes.append(lane)
    
# SAVE LANES IN A JSON FILE ==>
json_object = json.dumps(lanes, indent=4)
with open("lanes.json", "w") as outfile:
    outfile.write(json_object)    

# CREATE LANE IN DATABASE ==>
# READT LANE JSON
# lanes_json = open("lanes.json")
# lanes_array = json.load(lanes_json)
# user = "989f91c0-557b-4da0-901c-e47f9c8ca27c"
# for lane in lanes_array:
#     print("LANE ==>", lane)
#     res = requests.get(
#         "http://127.0.0.1:5055/api/v1/consults?equipment={equipment}&origin_zipcode={o_zip}&destination_zipcode={d_zip}".format(equipment=lane["equipment_id"], o_zip=lane["origin_zipcode"], d_zip=lane["destination_zipcode"])
#     )
#     print("response ==>", res)
    