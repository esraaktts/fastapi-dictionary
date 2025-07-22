import requests

def get_word_info(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        phonetics = [item.get('text') for item in data[0].get('phonetics', []) if item.get('text')]
        phonetic_str = phonetics[0] if phonetics else "Telaffuz bulunamadi."

        meanings = data[0].get('meanings', [])
        definitions = []
        for meaning in meanings:
            part_of_speech = meaning.get('partOfSpeech', 'N/A')
            for definition in meaning.get('definitions', []):
                def_text = definition.get('definition')
                definitions.append(f"{part_of_speech}: {def_text}")

        print(f"\nKelime: {word}")
        print(f"Telaffuz: {phonetic_str}")
        print("Anlamlar:")
        for i, d in enumerate(definitions, 1):
            print(f"{i}. {d}")

    except requests.exceptions.HTTPError:
        print("Kelime bulunamadi.")

    except Exception as e:
        print(f"Hata olustu: {e}")

if __name__ == "__main__":
    kelime = input("Bir kelime giriniz (EN): ").strip()
    get_word_info(kelime)
