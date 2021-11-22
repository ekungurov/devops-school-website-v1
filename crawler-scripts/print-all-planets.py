import requests
import json
import pickle
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
planets_json = requests.get("https://swapi.dev/api/planets/", verify=False).json()

planets_amount = planets_json['count']
i = 1
while True:
  for planet in planets_json['results']:
    print("= = = ", i,  "= = =")
    print(json.dumps(planet, indent=4))
    i += 1
  if not planets_json['next'] or i > planets_amount:
    break
  planets_json = requests.get(planets_json['next'], verify=False).json()
