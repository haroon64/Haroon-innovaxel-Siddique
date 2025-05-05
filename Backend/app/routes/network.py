from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse
import logging
import sys
from app.services import create_short_url_service ,get_original_url_service,delete_short_url_service
import random
import string
from datetime import datetime
from app.database import init_db


from app.models import URLCreateRequest, URLResponse, URLUpdateRequest, URLStatsResponse

router = APIRouter()







logging.basicConfig(level=logging.INFO)



@router.post("create/", response_model=URLResponse, status_code=201)
async def create_short_url(data: URLCreateRequest):
    
    response = create_short_url_service(data)
    
    if response:
        return response
    
  

    else:
        raise HTTPException(status_code=500, detail="Failed to create short URL")
    

@router.get("original_url/{short_code}", response_model=URLResponse)
async def get_orginal_url(short_code: str):
   
    response = get_original_url_service(short_code)
    
    if response:
        return response
        
    else:
        raise HTTPException(status_code=404, detail="Short URL not found")


@router.delete("delete_url/{short_code}",  response_model=URLResponse )
def delete_short_url(short_code: str ):
    response = delete_short_url_service(short_code)
    print(response)
    if response:
        return response
    else:
        raise HTTPException(status_code=404, detail="Short URL not found")
    
  
  
  
  
    result = url_collection.delete_one({"shortCode": short_code})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Short URL not found")
