from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/app/healthy")
def health():
    system = True
    if system:
        return {"system": "success"}
    else:
        return {"system": "fail"}

def word_info(word: str):
    dictionary = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    try:
        result = requests.get(dictionary)
        veri = result.json()

        if not isinstance(veri, list):
            return {"error": "Kelime bulunamadi."}
    
        try:
            phonetic = veri[0]['phonetics'][0]['text']
        except:
            phonetic = "Telaffuz bilgisi yok."
            
        meanings = []
        for mean in veri[0].get('meanings', []):
            
            for tanim in mean.get('definitions', []):
                tanimlar = tanim.get('definition')
                if tanimlar:
                    meanings.append(tanimlar)
        
        if not meanings:
            meanings.append("Anlam bulunamadi.")

        return {
            "word": word,
            "phonetic": phonetic,
            "meanings": meanings
        }   
    except:
        return {"error": "Kelime bulunamadi"}
    
@app.get("/app/words/{word}")

def get_word_definition(word: str):
    info = word_info(word)
    return info