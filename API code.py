from http.client import responses

import requests

base_url="https://pokeapi.co/api/v2/"

def get_name(name):
    url=f"{base_url}/pokemon/{name}"
    response_code = requests.get(url)
    print(response_code) # it gives the response code of URL like 404, 400 , 200 means working
# in IF statement .status.code get the code response
    if response_code.status_code==200:
        print("Data retrieved")
        #.json() gives the python dictionary
        pokemon_data= response_code.json()
        return pokemon_data
    else:
        print("Site unavailable")
pokemon=input("enter the name of Pokemon : ")
Pokemon_info =get_name(pokemon)
if Pokemon_info:
    print(f"Name : {Pokemon_info["name"]}")
    print(f"ID : {Pokemon_info["id"]}")
    print(f"Weight : {Pokemon_info["weight"]}")



