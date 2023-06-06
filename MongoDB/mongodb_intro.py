import pymongo

# Create a connection:
# If we wanted to connect to an external database, changing ports..., they would be added in the brackets
client = pymongo.MongoClient()

db = client['starwars']

# Equivalent is ' select * from characters' in sql
#characters = db.characters.find()

# # the find method can be used alongside filters.
# characters = db.characters.find({ "name" : "Luke Skywalker"})

# # printing certain fields, 1=give the field, 0=don't show field (id)
# characters = db.characters.find({"name": "Luke Skywalker"}, {'gender':1, "_id":0})

# #printing fields from embedded documents, pay close attention to the 'homeworld.name'
# characters = db.characters.find({"name": "Luke Skywalker"}, {"_id":0, "name":1, "homeworld.name":1})

# # Names and homwworld name where species is human - needs some work
# characters = db.characters.find({"species.name":"Human"}, {"_id":0, "name":1, "homeworld.name":1})

# # comparison operators: - require $ infront of operators
# characters = db.characters.find({'eye_color': {'$in':['blue', 'yellow']}}, {'_id':0, 'name':1, 'eye_color':1})
# # 2 different conditional statments: and - eye_color needs to be yellow and gender female
# # or works the same
# characters = db.characters.find({"$and":[{'eye_color':'yellow'}, {'gender':'female'}]}, {'_id':0, 'name':1, 'eye_color':1})

# characters = db.characters.find({'height':{'$gt':200}}, {'name':1, 'height':1})

# # aggregation pipelines:
# characters = db.characters.aggregate([{'$match': {'gender':'female'}}, 
#                                     {"$group":{'_id':'$gender', 'avg_height': {'$avg': '$height'}}}])

# # tallest character
# characters = db.characters.aggregate([{'$group' : {'_id':'name', 'max_height': {'$max': '$height' }}}])

# # average height and count per species. Filter out null values and sort by average height ascending.
# characters = db.characters.find({ "species": { '$ne': None }}, {"_id":0, "species.name":1, "species.average_height":1})

characters = db.characters.find({})

for character in characters:
    print(character)