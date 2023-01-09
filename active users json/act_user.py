# Implement a function called filter_active_users(), which will load the included users.json file and extract all active users (the value for the key is_active -> true):
# "is_active": true



import json

def filter_active_users():
    with open ("users.json", "r") as file:
        data = json.load(file)
    users = [user for user in data if user["is_active"]]
    with open('active_users.json', 'w') as file:
        json.dump(users, file, indent=2)


filter_active_users()