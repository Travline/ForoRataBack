from core.config import get_api_key, get_api_key_name
from main import app
from fastapi import HTTPException, Request
"""
@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    api_key = request.headers.get(await get_api_key_name())
    if api_key != await get_api_key():
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")
    return await call_next(request)"""