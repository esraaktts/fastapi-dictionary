import redis

def get_user_ip(user_ip: Request):
    
    ip = user_ip.client.host
    return ip

def get_user_history(user_history: 

try:

    if word:


    else:
        return {"message": "No history found for this user."}




    

except Exception:
    return ("Please check the Redis server connection and ensure it is running.")