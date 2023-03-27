import json

milesFromSun = {"Mercury": 35000000,
                "Venus": 67000000,
                "Earth": 93000000,
                "Mars": 142000000,
                "Jupiter": 484000000,
                "Saturn": 889000000,
                "Uranus": 1790000000,
                "Neptune": 2880000000}
jsonObj = json.dumps(milesFromSun, indent=4)
print(jsonObj)
