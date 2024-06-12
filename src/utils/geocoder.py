from geocoder import mapquest
from config.config import load_config

config = load_config(section='geocoder')
key = config["MAPQUEST_KEY"]

def get_geolocation(location):
    response = mapquest(location, key=key)
    
    return response
