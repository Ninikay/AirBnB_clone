#!/usr/bin/python3

import json

json_str = '''
		{ "people":
			[
			{"username":"Boloo", "email":"boloo@gmail.com", "reg":"False"}, 
			{"username":"Katoon", "email":"ogeekaton@gmail.com", "reg":"True"}

			]}'''

data = json.loads(json_str)
print(data)
print(type(data))
print("*" * 20)
list1 = data["people"]
print(list1)
print(type(list1))
for person in list1:
    print(person["username"])
    del person["reg"]

new_json = json.dumps(data, indent=2, sort_keys=True)
print(new_json)
