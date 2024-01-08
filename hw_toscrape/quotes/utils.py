from pymongo import MongoClient
import os
api_key = os.environ.get('API_KEY')

mongo_user='dishalex'
mongodb_pass='JiAQGB42M7iwRE2J'
db_name='Hw10_django'
domain='cluster0.dxmzxl1.mongodb.net'
uri = f'mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority'

# Create a new client and connect to the server


def get_mongodb():
    client = MongoClient(uri)
    db = client.Hw10_django
    return db

    # try:
    #     client.admin.command('ping')
    #     print("Pinged your deployment. You successfully connected to MongoDB!")
    # except Exception as e:
    #     print(e)
