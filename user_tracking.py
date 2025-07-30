import uuid
import hashlib
import time
import json
from typing import Dict, List, Optional

class UserTracker:
    def __init__(self):
        self.users_db = {}
        self.search_history = {}
    
    def generate_user_id(self, ip_address: str, user_agent: str) -> str:
        """IP ve User-Agent'dan benzersiz kullanıcı ID'si oluşturur"""
        # IP + User-Agent kombinasyonundan hash oluştur
        combined = f"{ip_address}_{user_agent}"
        user_hash = hashlib.md5(combined.encode()).hexdigest()[:12]
        return f"user_{user_hash}"
    
    def get_or_create_user(self, ip_address: str, user_agent: str) -> str:
        """Kullanıcıyı al veya oluştur"""
        user_id = self.generate_user_id(ip_address, user_agent)
        
        if user_id not in self.users_db:
            self.users_db[user_id] = {
                "ip_address": ip_address,
                "user_agent": user_agent,
                "created_at": time.time(),
                "last_seen": time.time(),
                "search_count": 0
            }
            self.search_history[user_id] = []
        
        # Son görülme zamanını güncelle
        self.users_db[user_id]["last_seen"] = time.time()
        return user_id
    
    def track_search(self, user_id: str, word: str, result: Dict):
        """Kullanıcının arama geçmişini kaydet"""
        search_record = {
            "word": word,
            "timestamp": time.time(),
            "result_success": result.get("title") is None,  # Başarılı arama mı?
            "result_data": result
        }
        
        # Kullanıcının arama geçmişine ekle
        if user_id in self.search_history:
            self.search_history[user_id].append(search_record)
            # Son 100 aramayı tut
            if len(self.search_history[user_id]) > 100:
                self.search_history[user_id] = self.search_history[user_id][-100:]
        
        # Kullanıcı istatistiklerini güncelle
        if user_id in self.users_db:
            self.users_db[user_id]["search_count"] += 1
    
    def get_user_stats(self, user_id: str) -> Dict:
        """Kullanıcı istatistiklerini al"""
        if user_id not in self.users_db:
            return {"error": "User not found"}
        
        user_data = self.users_db[user_id]
        search_history = self.search_history.get(user_id, [])
        
        # Başarılı aramaları say
        successful_searches = sum(1 for search in search_history if search["result_success"])
        
        return {
            "user_id": user_id,
            "total_searches": user_data["search_count"],
            "successful_searches": successful_searches,
            "success_rate": (successful_searches / user_data["search_count"] * 100) if user_data["search_count"] > 0 else 0,
            "created_at": user_data["created_at"],
            "last_seen": user_data["last_seen"],
            "recent_searches": search_history[-10:] if search_history else []  # Son 10 arama
        }
    
    def get_all_users(self) -> List[Dict]:
        """Tüm kullanıcıları listele"""
        return [
            {
                "user_id": user_id,
                "ip_address": data["ip_address"],
                "search_count": data["search_count"],
                "created_at": data["created_at"],
                "last_seen": data["last_seen"]
            }
            for user_id, data in self.users_db.items()
        ]

# Global user tracker instance
user_tracker = UserTracker() 