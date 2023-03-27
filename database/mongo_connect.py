from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.python
collection = db.items
# print(collection.find_one())
# new_item = collection.insert_one({'engine':2.0, 'hp':200})
# print(new_item)
items = collection.find()
for i in items:
    if 'name' in i:
        print(i['name'])
