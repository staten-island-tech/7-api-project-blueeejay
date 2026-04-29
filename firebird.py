# the app.py in code line "python app.py" should mirror the filename #yay 
""" 

import requests """
""" def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}") # requests data from this api... mmm information
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json() # opens the data to make it readable 
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    } # this data opens in a dictionary format 
 """

""" pokemon = getPoke("Bulbasaur")
print(pokemon)


for key, value in pokemon.items(): # using items lets you look through every thing in the box/every pairing in the dictionary 
    print(key, "→", value) """


#MAKING A LIST... NEW WAY TO DO IT! 
""" types = []
for t in data["types"]:
    types.append(t["type"]["name"])"""
# big way
"""types = [t["type"]["name"] for t in data["types"]] """
# little way #installing virtual environment
#convert to json data

""" 

SCIENTIFIC_NAME,COMMON_NAME,SPECIES_CODE,CATEGORY,TAXON_ORDER,COM_NAME_CODES,SCI_NAME_CODES,BANDING_CODES,ORDER,FAMILY_COM_NAME,FAMILY_SCI_NAME,REPORT_AS,EXTINCT,EXTINCT_YEAR
Larus glaucoides thayeri,Iceland Gull (Thayer's),thagul,issf,4349.0,THGU ICGU,LAGL,THGU,Charadriiformes,"Gulls, Terns, and Skimmers",Laridae,y00478,,
Larus glaucoides kumlieni,Iceland Gull (kumlieni),kumgul1,issf,4352.0,THGU ICGU,LAGL,,Charadriiformes,"Gulls, Terns, and Skimmers",Laridae,y00478,,
 """

# API ACTIVITY
# https://api.ebird.org/v2/ref/taxonomy/ebird i  love e bird sm.. 

import requests
def WHATf(genus):
    
    response = requests.get(f"https://www.fruityvice.com/api/fruit/genus/{genus}")
    if response.status_code != 200:
        print ("Error fetching data.")
        return None
    data = response.json
    return  {
        "Common Name": data["name"],
        "Fruit Id": data["id"],
        "Family": data["family"],
        "Order": data["order"],
        "genus": data["genus"],
        "nutrition": { 
            "carbohydrates": data["carbohydrates"], 
            "protein" : data["protein"],
            "fat" : data["fat" ],
            "calories" : ["calories"],
            "sugar" : data["sugar"]
        }
    }
bird = WHATf("Ananas")
print(bird)

# window.title("Message Reverser") # title at the top of the window
# window.geometry("400x250") # set the size (width x height)
# window.resizable(False, False)
# button = tkinter.Button()
    # }
    # return  {
    #     "Common Name": data["name"],
    #     "Fruit Id": data["id"],
    #     "Family": data["family"],
    #     "genus": data["genus"],
    #     "Order": data["order"],
    #     "nutrition": { 
    #         "carbohydrates": data["carbohydrates"], 
    #         "protein" : data["protein"],
    #         "fat" : data["fat" ],
    #         "calories" : ["calories"],
    #         "sugar" : data["sugar"]
    #     }
    # }

""" 




    # return  {
    #     "Scientific Name": data["SCIENTIFIC_NAME"],
    #     "Common Name": data["COMMON_NAME"],
    #     "Species code": data["SPECIES_CODE"],
    #     "Category of bird": data["CATEGORY"],
    #     "Order": data["TAXON_ORDER"],
    #     "Banding Code": data["BANDING_CODES"]
    # }


https://dog.ceo/api/breeds/image/random
import tkinter
import requests
def birdsearch(fruit):
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    if response.status_code != 200:
        print ("Error fetching data.")
        return None
    data = response.json
    return  {
        "Common Name": data("name"),
        "Fruit Id": data("id"),
        "Family": data("family"),
        "genus": data("genus"),
        "Order": data("order"),
        "nutrition": { 
            "carbohydrates": data("carbohydrates"), 
            "protein" : data("protein"),
            "fat" : data("fat"),
            "calories" :("calories"),
            "sugar" : data("sugar")
        }
    } """