from pymongo import MongoClient

# Global variables to store the MongoDB client, database, and collection references
client = None
db = None
url_collection = None

# Initializes the MongoDB connection and sets up the database and collection
def init_db():
    global client, db, url_collection

    # Connect to the local MongoDB server
    client = MongoClient("mongodb://localhost:27017/")
    
    # Select the database named 'URL_storage'
    db = client["URL_storage"]
    print("Database initialized:", db)
   
    # Select the collection named 'url_db' within the database
    url_collection = db["url_db"]
    print("Collection initialized:", url_collection)

    return url_collection

# Automatically initialize the database and collection when the module is imported
url_collection = init_db()
