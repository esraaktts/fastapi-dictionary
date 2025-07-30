from fastapi import FastAPI, Request
from word_info import word_info
from word_of_the_day import word_of_the_day
from trending_words import trending_words
from user_tracking import user_tracker

app = FastAPI()

@app.get("/app/healthy")
def health():
    return {"system":"success"}

@app.get("/app/words/{word}")
def get_word(word: str, request: Request):
    # Kullanıcı ID'sini al
    client_ip = request.client.host
    user_agent = request.headers.get("User-Agent", "Unknown")
    user_id = user_tracker.get_or_create_user(client_ip, user_agent)
    
    # Kelime araması yap
    res = word_info(word)
    
    # Kullanıcı aramasını takip et
    user_tracker.track_search(user_id, word, res.dict())
    
    # Response'a kullanıcı ID'sini ekle
    response_data = res.dict()
    response_data["user_id"] = user_id
    
    return response_data

@app.get("/app/trending/{word}")
def trending(word: str):
    res = trending_words(word)
    return res

@app.get("/app/word_of_the_day")
def get_word_of_the_day():
    return word_of_the_day()

@app.get("/app/user/stats/{user_id}")
def get_user_statistics(user_id: str):
    """Kullanıcı istatistiklerini al"""
    stats = user_tracker.get_user_stats(user_id)
    return stats

@app.get("/app/users/all")
def get_all_users():
    """Tüm kullanıcıları listele"""
    users = user_tracker.get_all_users()
    return {"users": users, "total_users": len(users)}

@app.get("/app/user/current")
def get_current_user(request: Request):
    """Mevcut kullanıcının bilgilerini al"""
    client_ip = request.client.host
    user_agent = request.headers.get("User-Agent", "Unknown")
    user_id = user_tracker.get_or_create_user(client_ip, user_agent)
    
    stats = user_tracker.get_user_stats(user_id)
    return {
        "user_id": user_id,
        "ip_address": client_ip,
        "user_agent": user_agent,
        "stats": stats
    }