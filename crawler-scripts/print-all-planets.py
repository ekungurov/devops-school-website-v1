import requests
import json
import pickle
import urllib3

def get_some_planets(url):
  return requests.get(url, verify=False).json()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
next_url = "https://swapi.dev/api/planets/"

requests_limit = 2
requests_counter = 0
while next_url and requests_counter < requests_limit:
  planets_json = get_some_planets(next_url)
  requests_counter += 1
  for planet in planets_json['results']:
    print("= = = ", "= = =")
    print(json.dumps(planet, indent=4))
  next_url = planets_json['next']

  
