import requests
req=requests.get("https://jsonplaceholder.typicode.com/users")
if req.status_code==200:
    for user in req.json():
        print(user["name"])
        print(user["email"])
        print(user["phone"])
        print("\n\n")