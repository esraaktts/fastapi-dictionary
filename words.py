from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/app/words/{word}")

def get_word(word: str):
    dictionary = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    sonuc = requests.get(dictionary)
  
    if sonuc.status_code == 200:
        return {"Sonuc": "Bulundu."}
    
    else:
        return {"ERROR": "Kelime bulunamadi."}    