import requests; import random; import json
choice = input("Type in the name of the pokemon you want: ").lower()
response = requests.get("https://pokeapi.co/api/v2/pokemon/"+choice+"/encounters")
print(response.status_code)
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
jprint(response.json())