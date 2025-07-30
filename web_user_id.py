from fastapi import FastAPI, Request, HTTPException
from fastapi.security import HTTPBearer
import jwt
import uuid
import time
from typing import Optional

app = FastAPI()
security = HTTPBearer()

# Basit kullanıcı veritabanı (gerçek uygulamada database kullanın)
users_db = {}

def create_user_id():
    """Yeni kullanıcı ID'si oluşturur"""
    return str(uuid.uuid4())

def create_session_token(user_id: str):
    """Kullanıcı için session token oluşturur"""
    payload = {
        "user_id": user_id,
        "exp": time.time() + 3600,  # 1 saat geçerli
        "iat": time.time()
    }
    # Gerçek uygulamada SECRET_KEY kullanın
    return jwt.encode(payload, "your-secret-key", algorithm="HS256")

def get_user_from_token(token: str) -> Optional[str]:
    """Token'dan kullanıcı ID'sini alır"""
    try:
        payload = jwt.decode(token, "your-secret-key", algorithms=["HS256"])
        return payload.get("user_id")
    except:
        return None

@app.post("/register")
async def register_user(request: Request):
    """Yeni kullanıcı kaydı"""
    user_id = create_user_id()
    users_db[user_id] = {
        "created_at": time.time(),
        "last_login": time.time()
    }
    
    token = create_session_token(user_id)
    
    return {
        "user_id": user_id,
        "token": token,
        "message": "User registered successfully"
    }

@app.get("/user/profile")
async def get_user_profile(request: Request):
    """Kullanıcı profilini alır"""
    # Header'dan token al
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    token = auth_header.split(" ")[1]
    user_id = get_user_from_token(token)
    
    if not user_id or user_id not in users_db:
        raise HTTPException(status_code=401, detail="User not found")
    
    return {
        "user_id": user_id,
        "profile": users_db[user_id]
    }

@app.get("/user/ip")
async def get_user_ip(request: Request):
    """Kullanıcının IP adresini alır"""
    client_ip = request.client.host
    user_agent = request.headers.get("User-Agent", "Unknown")
    
    return {
        "ip_address": client_ip,
        "user_agent": user_agent,
        "headers": dict(request.headers)
    } 