import json
from bson.objectid import ObjectId

from pymongo import MongoClient

mongo_user='dishalex'
mongodb_pass='JiAQGB42M7iwRE2J'
db_name='Hw10_django'
domain='cluster0.dxmzxl1.mongodb.net'
uri = f'mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority'

# Create a new client and connect to the server
client = MongoClient(uri)
db = client.Hw10_django

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# with open('utils/quotes.json', 'r', encoding='utf-8') as file:
#     quotes = json.load(file)

# for quote in quotes:
#     author = db.authors.find_one({'fullname': quote['author']})
#     if author:
#         db.quotes.insert_one({
#             'quote': quote['quote'],
#             'tags': quote['tags'],
#             'author': ObjectId(author['_id'])
#         })