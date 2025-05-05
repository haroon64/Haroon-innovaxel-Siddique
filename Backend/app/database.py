from pymongo import MongoClient

client = None
db = None
url_collection = None

def init_db():
    global client, db, url_collection
    client = MongoClient("mongodb://localhost:27017/")
    db = client["URL_storage"]
    print("Database initialized:", db)
   
    url_collection = db["url_db"]
    print("Collection initialized:", url_collection)
    return url_collection

url_collection = init_db()  # Initialize the database and collection when this module is imported