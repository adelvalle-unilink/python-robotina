import requests
from config.config import load_config

config = load_config(section='api-ninja')
__ENDPOINT = config["zipcode_endpoint"]
__KEY = config["key"]

def get_zipcode(city, state):
    '''
        Returns the zipcode of the first position of the array
        that NINJA API ZIPCODE ENDPOINTS returns.
    '''
    
    params={
        "city": city,
        "state": state, 
    }
    headers={
        'X-Api-Key': __KEY,
    }
    
    try:
        response = requests.get(__ENDPOINT, params=params, headers=headers)
        res_object = response.json()
        return res_object[0]["zip_code"]
    except (Exception) as err:
        print("Something went wrong.")
        print("ERROR", err)