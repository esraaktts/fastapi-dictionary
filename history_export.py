import redis
from fastapi import Request
from datetime import datetime
import json
from fastapi.responses import JSONResponse
from enum import Enum


r = redis.Redis(host="localhost", port=6379, decode_responses=True)

try:
    def get_user_ip(reqst: Request):
        
        user_ip = reqst.headers.get("X-Forwarded-For")
        if user_ip:
            ip = user_ip.split(",")[0].strip()
        else:
            ip = ip.client.host
        return ip
    #ip yi bulmus olayım

    def get_user_history(ip: str):
        user_history = r.hget("history", ip)
        if user_history:
            return json.loads(user_history)
        else:
            return []
    
    if format == ExportFormat.json:
    if format == ExportFormat.csv:
    if format == ExportFormat.csv:
                 
   # CSV format handling
        pass        

except Exception:
        return {"message": "No history found for this user."}