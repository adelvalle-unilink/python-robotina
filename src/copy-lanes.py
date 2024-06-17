import json
# import requests
# import pandas as pd
from config.db_connection import connect
from config.generic_config import load_config
from utils.geocoder import get_distance
# from utils.api_ninja import get_zipcode

# from src.config import db_connection
from repositories.lane import Lane
from utils.functions import copy_excel_template

# DB CONNECTION
conn_config = load_config(section='postgresql')
conn = connect(config=conn_config)
conn.autocommit = True

# df = pd.read_csv("lanes.csv")
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

#2.-
# CREATE LANES OBJECT.
## ADD ZIPCODE AND EQUIPMENT_ID = 3 TO ALL LANES
# GET ZIPCODES
# lanes = []
# zipcodes_json = open("zipcodes.json")
# zipcodes = json.load(zipcodes_json)
# for indx in range(200):
#     origin = df.at[indx, "Origin"]
#     destination = df.at[indx, "Destination"]
    
#     origin_zipcode = zipcodes[origin]
#     destination_zipcode = zipcodes[destination]
#     lane = {
#         "origin_zipcode": origin_zipcode,
#         "destination_zipcode": destination_zipcode,
#         "equipment_id": 3,
#     }
#     lanes.append(lane)
    
# # SAVE LANES IN A JSON FILE ==>
# json_object = json.dumps(lanes, indent=4)
# with open("lanes.json", "w") as outfile:
#     outfile.write(json_object)    

# 3.-
# CREATE LANE IN DATABASE ==>
# DID IT FORM MY LOCAL. CHANGE THE URL TO USO PRODUCTION OR DEV ENVIRONMENT.
# READT LANE JSON
# errors = []
# ok = []
# lanes_json = open("lanes.json")
# lanes_array = json.load(lanes_json)
# user = "989f91c0-557b-4da0-901c-e47f9c8ca27c"
# for lane in lanes_array:
#     print("LANE ==>", lane)
#     res = requests.get(
#         "http://127.0.0.1:5055/api/v1/consults?equipment={equipment}&origin_zipcode={o_zip}&destination_zipcode={d_zip}"
#             .format(
#                 equipment=lane["equipment_id"], 
#                 o_zip=lane["origin_zipcode"], 
#                 d_zip=lane["destination_zipcode"],
#             )
#     )
#     print("RESPONSE ==>", res)
#     res_json = res.json()
#     is_success = res_json["success"]
    
#     if is_success: ok.append(res_json["data"]["lane_id"])

# # SAVE RESPONSES
# errors_json_object = json.dumps(errors, indent=4)
# with open("errors.json", "w") as outfile:
#     outfile.write(errors_json_object)    
    
# ok_json_object = json.dumps(ok, indent=4)
# with open("ok.json", "w") as outfile:
#     outfile.write(ok_json_object)    


# 4.-
# ADD DISTANCES TO LANES ==>
# READ THE JSON FILE WITH ALL THE LANES.
# print("RUNNING SCRIPT ==>")
# ok_lanes_json = open("ok.json")
# ids = json.load(ok_lanes_json) # AN ARRAY OF ids
# lane_repo = Lane(conn)
# lanes = lane_repo.get_all(ids)

# distances = []
# # FOR EACH LANE GET THE DISTANCE AND SAVE IT IN AN OBJECT:
# for lane in lanes:
#     lane_id=lane[0]
#     origin = ",{city},{state}".format(city=lane[5], state=lane[7])
#     destination = ",{city},{state}".format(city=lane[6], state=lane[8])
#     distance = get_distance(origin=origin, destination=destination)
#     obj = {
#         "lane_id": lane_id,
#         "origin": origin,
#         "destination": destination,
#         "miles": distance,
#     }
#     distances.append(obj)

# # Save lines with distances in a JSON file.
# distances_obj = json.dumps(distances, indent=4)
# with open("lanes_with_distances.json", "w") as outfile:
#     outfile.write(distances_obj)
# print("FINISH SCRIPT.")

# SAVE THE DISTANCES OF THE LANES FROM lanes_with_distances JSON file.
# Get Json File.
# lanes_with_distances_json = open("lanes_with_distances.json")
# lanes_with_distances = json.load(lanes_with_distances_json) # As an array
# lane_repo = Lane(conn)

# for lane in lanes_with_distances:
#     lane_id = lane["lane_id"]
#     miles = lane["miles"]
#     lane_repo.add_distance(lane_id=lane_id, distance=miles)


# 5.-
# CREATE THE EXCEL FILE TO UPLOAD TO BENCHMARK PAGE.
# print("START STEP 5:")
# ok_lanes_json = open("ok.json")
# ids = json.load(ok_lanes_json) # AN ARRAY OF ids
# # GET LANE REPOSITORY METHODS WITH CONNECTION.
# lane = Lane(conn)

# lanes = lane.get_all(ids)
# copy_excel_template(lanes) # MISSING ADD DISTANCES.

# conn.close()
# print("FINISH STEP 5.")


# CREATE THE CONSULTS FOR BENCHMARK


# GET BENCHMARK EXCEL WITH ALL THE INFORMATION.

# SAVE BENCHMARK INFORMATION FOR EACH LANE IN DATABASE.