from datetime import datetime
from app.models import URLCreateRequest
from app.database import db
import string
import random
from app.database import url_collection
from pymongo import ReturnDocument
from fastapi import APIRouter, HTTPException


# Generates a random alphanumeric short code
def generate_shortcode(length=6):
    characters = string.ascii_letters + string.digits
    print("Characters used for generating short code:", characters)
    code = ''.join(random.choices(characters, k=length))
    print(code)
    return code


# Creates a short URL if it doesn't already exist
def create_short_url_service(data: URLCreateRequest):
    if url_collection is None:
        raise RuntimeError("Database not initialized. Make sure init_db() has been called.")

    now = datetime.utcnow().isoformat()
    short_code = generate_shortcode()

    # Check if the URL already exists in the DB
    existing_doc = url_collection.find_one({"url": str(data.url)})
    if existing_doc:
        raise HTTPException(status_code=400, detail="Url already exists")

    # Insert new document with URL and generated shortCode
    doc = {
        "url": str(data.url),
        "shortCode": short_code,
        "createdAt": now,
        "updatedAt": now,
        "accessCount": 0
    }

    result = url_collection.insert_one(doc)
    doc["id"] = str(result.inserted_id)  # Convert ObjectId to string
    return doc


# Retrieves the original URL by its shortCode and updates the access count
def get_original_url_service(short_code: str):
    if url_collection is None:
        raise RuntimeError("Database not initialized. Make sure init_db() has been called.")
    
    doc = url_collection.find_one({"shortCode": short_code})
    
    if doc:
        # Increment access count
        url_collection.update_one({"shortCode": short_code}, {"$inc": {"accessCount": 1}})
        doc["id"] = str(doc["_id"])  # Convert ObjectId to string
        return doc
    
    return None


# Deletes a short URL and returns the deleted document
def delete_short_url_service(short_code: str):
    if url_collection is None:
        raise RuntimeError("Database not initialized. Make sure init_db() has been called.")
    
    print("Deleting short URL with code:", short_code)
    doc = url_collection.find_one({"shortCode": short_code})  # Find the doc before deleting
    print("Document found:", doc)

    result = url_collection.delete_one({"shortCode": short_code})

    if result and doc:
        doc["id"] = str(doc["_id"])  # Convert ObjectId to string
        return doc
    else:
        raise HTTPException(status_code=404, detail="Short URL not found")


# Updates the original URL for a given shortCode
def update_short_url_service(short_code: str, data: URLCreateRequest):
    if url_collection is None:
        raise RuntimeError("Database not initialized. Make sure init_db() has been called.")

    now = datetime.utcnow().isoformat()

    # Find and update the document, return the updated document
    result = url_collection.find_one_and_update(
        {"shortCode": short_code},
        {"$set": {"url": str(data.url), "updatedAt": now}},
        return_document=ReturnDocument.AFTER  # Ensures updated doc is returned
    )

    if not result:
        raise HTTPException(status_code=404, detail="Short URL not found")

    result["id"] = str(result["_id"])  # Convert ObjectId to string
    del result["_id"]  # Optional: remove MongoDB's default ID field

    return result
