import json
import requests
import typing

'''
Given a String of Location, returns [longitude, latitude]. Returns None if place not found.
'''
def get_coordinate(location: str) -> typing.Optional[typing.List]:
    result = None
    url = 'https://nominatim.openstreetmap.org/search?q=' + location + '&format=geocodejson'
    response = requests.get(url).text
    data = json.loads(response)
    if len(data['features']) == 0:
        print("No coordinates data.")
    else:
        result = data['features'][0]['geometry']['coordinates']
        
    return result
