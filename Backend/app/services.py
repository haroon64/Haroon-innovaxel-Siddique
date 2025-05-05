from datetime import datetime
from app.models import URLCreateRequest
from app.database import db
import string
import random
from app.database import url_collection
from fastapi import APIRouter, HTTPException


def generate_shortcode(length=6):
    characters = string.ascii_letters + string.digits
    print("Characters used for generating short code:", characters)
  
    print(1)
    code = ''.join(random.choices(characters, k=length))
    print(code)
    return code


def create_short_url_service(data: URLCreateRequest):
    if url_collection is None:
        raise RuntimeError("Database not initialized. Make sure init_db() has been called.")

    now = datetime.utcnow().isoformat()
    short_code = generate_shortcode()

    # Check if the URL already exists
    existing_doc = url_collection.find_one({"url": str(data.url)})

    if existing_doc :
      
        raise HTTPException(status_code=400 ,detail="Url already exists")
               

    # Create new document if not found
    doc = {
        "url": str(data.url),
        "shortCode": short_code,
        "createdAt": now,
        "updatedAt": now,
        "accessCount": 0
    }

    result = url_collection.insert_one(doc)
    doc["id"] = str(result.inserted_id)
    return doc


def get_original_url_service(short_code: str):
    if url_collection is None:
        raise RuntimeError("Database not initialized. Make sure init_db() has been called.")
    
    doc = url_collection.find_one({"shortCode": short_code})
    
    if doc:
        # Increment access count
        url_collection.update_one({"shortCode": short_code}, {"$inc": {"accessCount": 1}})
        
        # Convert ObjectId to string for JSON serialization
        doc["id"] = str(doc["_id"])
        return doc
    
    return None

def delete_short_url_service(short_code: str):
    if url_collection is None:
        raise RuntimeError("Database not initialized. Make sure init_db() has been called.")
    print("Deleting short URL with code:", short_code)
    doc = url_collection.find_one({"shortCode": short_code})
    
    print("Document found:", doc)
    result = url_collection.delete_one({"shortCode": short_code})
  
    if result and doc  :
        doc["id"] = str(doc["_id"])
        return doc
    
    else:
        raise HTTPException(status_code=404, detail="Short URL not found")