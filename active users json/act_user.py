# Implement a function called filter_active_users(), which will load the included users.json file and extract all active users (the value for the key is_active -> true):
# "is_active": true



import json

def filter_active_users():
    users= []
    with open ("users.json", "r") as file:
        data = json.load(file)
    for i in data:
        if i["is_active"] == True:
            users.append(i)
    with open('active_users.json', 'w') as file:
        json.dump(users, file, indent=2)


filter_active_users()