import requests

def word_info(word: str):
    dictionary = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    try:
        result = requests.get(dictionary)
        veri = result.json()

        if not isinstance(veri, list):
            return {"error": "Kelime bulunamadi."}
    
        try:
            phonetic = veri[0]['phonetics'][0]['text']
        
        except :
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

if __name__ == "__main__":
    word = input("Kelime: ").strip()
    result = word_info(word)

    if "error" in result:
        print(result["error"])
    else:
        print(f"\nWord: {result['word']}")
        print(f"Phonetic: {result['phonetic']}")
        print("Meanings:")
        sayac = 1

        for mean in result ['meanings']:
            print(f"{sayac}. {mean}")
            sayac += 1