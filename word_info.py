import requests
from models import WordResponse

def word_info(word: str):
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
         
        phonetic = "Phonetic Not Found."
        for phtic in veri[0].get("phonetics", []):
            if "text" in phtic:
                phonetic = phtic["text"]
                break

        meanings  = []
        for meaning in veri[0].get('meanings', []):
            for definition in meaning.get('definitions', []):
                define = definition.get('definition')
                if define:
                    meanings.append(define)
            
        if not meanings:
                meanings.append("Meanings Not Found.")

        return WordResponse(
            word=word,
            phonetic=phonetic,
            meanings=meanings,
            title = None,
            message = None,
            resolution = None
        )
    
    except Exception:
        return WordResponse(
            word = None,
            phonetic = None,
            meanings = None,
            title="Network Error",
            message="Unable to connect to the dictionary API service.",
            resolution="Please check your internet connection or try again later."
        )
        