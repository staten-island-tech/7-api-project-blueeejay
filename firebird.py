""" import requests """

""" def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}") # requests data from this 
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json() # opens the data to make it readable 
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

pokemon = getPoke("Bulbasaur")
print(pokemon)

for key, value in pokemon.items(): # using items lets you look through every thing in the box/every pairing in the dictionary 
    print(key, "→", value)
 """
#MAKING A LIST 
""" types = []
for t in data["types"]:
    types.append(t["type"]["name"])"""
# big way
"""types = [t["type"]["name"] for t in data["types"]] """
# little way #installing virtual environment
#convert to json data