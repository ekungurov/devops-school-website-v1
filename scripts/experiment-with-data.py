import json
import pickle

with open("response.json.serialized", "rb") as f:
  data_json = pickle.load(f)

#with open("response.json", "r") as f:
#  data_json = json.load(f)

print("Decoded JSON Data From File")
for key, value in data_json.items():
  print(key, ":", value)
print()

print("Print 'count' field:", data_json['count'])