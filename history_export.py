import redis
from fastapi import Request

def get_user_ip(ip: Request):
    
    user_ip = ip.headers.get("X-Forwarded-For")

    if user_ip:
        ip = user_ip.split(",")[0].strip()
    else:
        ip = user_ip.client.host
    return ip

def get_user_history(user_history: 

try:

    if word:


    else:
        return {"message": "No history found for this user."}




    

except Exception:
    return ("Please check the Redis server connection and ensure it is running.")