import os
import django

from pymongo import MongoClient


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_toscrape.settings")
django.setup()

from quotes.models import Quote, Tag, Author


mongo_user='dishalex'
mongodb_pass='JiAQGB42M7iwRE2J'
db_name='Hw10_django'
domain='cluster0.dxmzxl1.mongodb.net'
uri = f'mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority'

# Create a new client and connect to the server
client = MongoClient(uri)
db = client.Hw10_django


authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname = author['fullname'],
        born_date = author['born_date'],
        born_location = author['born_location'],
        description =author['description']
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
    print(tags)


    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))
    if not exist_quote:
        author = db.authors.find_one({'_id': quote['author']})
        a = Author.objects.get(fullname=author['fullname'])
        q = Quote.objects.create(
            quote = quote['quote'],
            author = a
        )

        for tag in tags:
            q.tags.add(tag)