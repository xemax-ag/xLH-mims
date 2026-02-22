# https://www.ionos.de/digitalguide/websites/web-entwicklung/mongodb-python/
# https://pymongo.readthedocs.io/en/4.11/tutorial.html

from pymongo import MongoClient
import datetime
from rich import print


client = MongoClient("localhost", 27017)
db = client.test_database  # db = client["test-database"]
collection = db.test_collection  # collection = db["test-collection"]

post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

print(posts.find_one())