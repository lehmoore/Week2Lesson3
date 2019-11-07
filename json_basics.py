import json

car_data = {"name":"Tesla", "engine":"electric"} #dictionary

# print(type(car_data))

# 2 Methods in JSON
# json.dumps() - serialises json to a formatted string
# json.dump() - create a stream object and expects a file object to write to

car_data = {"name":"Tesla", "engine":"electric"}

car_data_json_string = json.dumps(car_data)

# print(car_data_json_string)
# print(type(car_data_json_string))

car_data = {"name":"Tesla", "engine":"electric"}

with open("new_json_file.json","w") as jsonfile:
    json.dump(car_data, jsonfile)


# Using json.load

with open("new_json_file.json") as jsonfile:
    car = json.load(jsonfile)
    # print(type(car))
    # print(car["name"])
    # print(car["engine"])


