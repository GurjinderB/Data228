import pymongo
import requests

client = pymongo.MongoClient()

db = client['starwars']
starships = db['starships']
characters = db['characters']

starship_ids = [2, 3, 5, 9, 10, 11, 12, 13, 15, 17, 21, 22, 23, 27, 28, 29, 
                31, 32, 39, 40, 41, 43, 47, 48, 49, 52, 58, 59, 61, 63, 64, 
                65, 66, 68, 74, 75]


def create_starship_documents(starship_ids):
        try:
            for starship_id in starship_ids:
                response = requests.get(f"https://swapi.dev/api/starships/{starship_id}").json()
                db.starships.insert_one(response)
        except:
            return 'error'
    

def assign_pilot_id(starship_ids):
    for starship_id in starship_ids:
        response = requests.get(f"https://swapi.dev/api/starships/{starship_id}").json()
        if response['pilots']:
            pilot_ids = []
            for i, pilot in enumerate(response['pilots']):
                response_pilot = requests.get(pilot).json()
                name = response_pilot['name']
                character = db.characters.find({'name': name})
                for details in character:
                    id = details['_id']
                    pilot_ids.append(id)
            db.starships.update_one({'pilots': response['pilots']}, {"$set" : {'pilots': pilot_ids}})


create_starship_documents(starship_ids)
assign_pilot_id(starship_ids)