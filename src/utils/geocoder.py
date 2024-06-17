import requests
from  config.generic_config import load_config 

__config = load_config(section='geocoder')

def get_distance(origin, destination):
    '''
        Origin and Destination should be formatted as:
        address(optional), City, State, Zipcode(optional).  
    '''

    try:
        directions_string = __config["mapquest_endpoint_directions"]
        endpoint = directions_string + "&from={origin}&to={destination}&unit=m".format(origin=origin, destination=destination)
        response= requests.get(endpoint)
        distance_json = response.json()
        distance = distance_json["route"]["distance"]
        return distance
    except (Exception) as err:
        print("ERROR ==>", err)
        return None

