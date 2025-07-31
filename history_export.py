import redis
from fastapi import Request
from datetime import datetime
import json
from fastapi.responses import JSONResponse
from enum import Enum

r = redis.Redis(host="localhost", port=6379, decode_responses=True)
def get_user_ip(request: Request):
    if request.client:
        return request.client.host
    else:
        return None
    
def get_current_timestamp():
    get_time = datetime.now()
    iso_time = get_time.isoformat()
    return {"timestamp": iso_time}

def get_user_history(ip: str):
        user_history = r.hget("history", ip)
        if user_history:
            return json.loads(user_history)
        else:
            return []

def save_word_to_history(ip: str, word: str):
    history = get_user_history(ip)
    history.append({
        "word": word,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    r.hset("history", ip, json.dumps(history))

try:


except Exception:
    print("please check your redis connection or redis server is running properly")