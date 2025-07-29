import requests
from models import WordResponse
import redis
import json

def word_info(word: str):
    
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    
    cached_word = r.get(word)
    if cached_word:
        return WordResponse(**json.loads(cached_word))

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    try:
        resp = requests.get(url)
        veri = resp.json()

        if not isinstance(veri, list):
            return WordResponse(
                word="Word Not Found",
                phonetic="Phonetic Not Found.",
                meanings=["Meanings Not Found."],
                title="Definition Not Found.",
                message="We couldn't locate a definition for the word you entered.",
                resolution="Please try searching a different word."
            )      
                
        def find_phonetic(data):
            for phtic in data:
                if "text" in phtic:
                    return phtic["text"]
            return "Phonetic Not Found."

        phonetic = find_phonetic(veri[0].get("phonetics", []))

        def find_meanings(data):
            meanings = []
            for meaning in data.get('meanings',[]):
                for defn in meaning.get('definitions', []):
                    definition = defn.get('definition')
                    if definition:
                        meanings.append(definition)
            if not meanings:
                meanings.append("Meanings Not Found.")
            return meanings
        
        meanings = find_meanings(veri[0])

        new_response = WordResponse(
            word=word,
            phonetic=phonetic,
            meanings=meanings,
            title= None,
            message= None,
            resolution= None
        )
        r.set(word,json.dumps(new_response.dict()))
        return new_response
    
    except Exception:
        return WordResponse(
            word =None,
            phonetic = None,
            meanings = None,
            title="Network Error",
            message="Unable to connect to the dictionary API service.",
            resolution="Please check your internet connection or try again later."
        )
