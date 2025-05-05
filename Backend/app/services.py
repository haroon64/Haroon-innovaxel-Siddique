from datetime import datetime
from app.models import URLCreateRequest
from app.database import db
import string
import random
from app.database import url_collection

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
    print(1)
    now = datetime.utcnow().isoformat()
    print(2)
    short_code = generate_shortcode()
    print(3)
    doc = {
        "url": str(data.url),
        "shortCode": short_code,
        "createdAt": now,
        "updatedAt": now,
        "accessCount": 0
    }
    print
    result = url_collection.insert_one(doc)
    print(5)
    doc["id"] = str(result.inserted_id)
    
    return doc