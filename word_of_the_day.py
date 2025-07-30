import redis
import json
import random

def word_of_the_day(word: str):
    try:
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)

        word_list= [ #ornek liste sadece test etmek icin anlam eklemedim
            "resilient", "serendipity", "ephemeral", "ubiquitous", 
            "mellifluous", "serene", "eloquent", "profound"
        ]
        word = r.get("word_of_the_day")

        if word:
            word_redis = json.loads(word)
            return word_redis

        else:
            print("No word of the day found in Redis, generating a new one.")
            random_word = random.choice(word_list)
            new_word = {
                "word": random_word,
                "definition": f"This is a definition for the word '{random_word}'."
            }

        r.set("word_of_the_day", json.dumps(new_word),ex=86400)
        return new_word

    except Exception:
        print("Please check the Redis server connection and ensure it is running.")
