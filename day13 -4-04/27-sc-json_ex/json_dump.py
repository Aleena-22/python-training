import json

person_dict = {"name": "Bob",
"languages": ["English", "Fench"],
"married": True,
"age": 32
}

with open(r'D:\py_training\python-training\day13 -4-04\27-sc-json_ex\person.json', 'w') as json_file:
  json.dump(person_dict, json_file)
