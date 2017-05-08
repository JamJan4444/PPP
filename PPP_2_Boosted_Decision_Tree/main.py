import tree
import json
from pprint import pprint

with open('data.json') as data_file:
    data = json.load(data_file)

print(data["data"][0])
print(data["data"][1])
print(data["data"][2])
print(data["data"][3])
print(data["data"][4])
