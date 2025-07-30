import os
import getpass
import uuid
import hashlib
import platform
import socket

def get_system_user_id():
    """Sistem kullanıcı ID'sini alır"""
    try:
        # Windows için
        if platform.system() == "Windows":
            return os.getenv('USERNAME') or os.getenv('USER')
        # Linux/Mac için
        else:
            return os.getenv('USER') or getpass.getuser()
    except:
        return "unknown_user"

def get_machine_id():
    """Makine ID'sini alır"""
    try:
        # Hostname kullanarak
        hostname = socket.gethostname()
        return hostname
    except:
        return "unknown_machine"

def generate_session_id():
    """Benzersiz session ID oluşturur"""
    return str(uuid.uuid4())

def generate_user_hash(username):
    """Kullanıcı adından hash oluşturur"""
    return hashlib.md5(username.encode()).hexdigest()

def get_comprehensive_user_id():
    """Kapsamlı kullanıcı ID'si oluşturur"""
    user = get_system_user_id()
    machine = get_machine_id()
    session = generate_session_id()
    
    return {
        "user_id": user,
        "machine_id": machine,
        "session_id": session,
        "user_hash": generate_user_hash(user),
        "combined_id": f"{user}_{machine}_{session[:8]}"
    }

# Test
if __name__ == "__main__":
    print("=== Kullanıcı ID Örnekleri ===")
    print(f"Sistem Kullanıcısı: {get_system_user_id()}")
    print(f"Makine ID: {get_machine_id()}")
    print(f"Session ID: {generate_session_id()}")
    print(f"Kapsamlı ID: {get_comprehensive_user_id()}") 