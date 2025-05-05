from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse
import logging
import sys
from app.services import create_short_url_service 
import random
import string
from datetime import datetime
from app.database import init_db


from app.models import URLCreateRequest, URLResponse, URLUpdateRequest, URLStatsResponse

router = APIRouter()







logging.basicConfig(level=logging.INFO)


# Helper to generate unique short codes


@router.post("/", response_model=URLResponse, status_code=201)
async def create_short_url(data: URLCreateRequest):
    
    response = create_short_url_service(data)
    
    if response:
        return response
    else:
        raise HTTPException(status_code=500, detail="Failed to create short URL")
    

