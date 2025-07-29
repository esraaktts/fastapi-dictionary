import redis
import json

def word_of_the_day(word: str):
    try:
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        word = r.get("word_of_the_day") #redisten gelen kelime
        word_list = r.get("word_list")
        word_list = json.loads(word_list)

        new_word = {
            "word": word,
            "definition": "This is the word of the day definition."
        }

        if word:
            new_word = json.loads(word)
        else:   
            r.set("word_of_the_day", json.dumps(new_word),ex=86400)

    except Exception as e:
        print("Please check the Redis server connection and ensure it is running.")
