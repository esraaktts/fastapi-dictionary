import redis
import json
import random

def word_of_the_day(word: str):
    try:
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)

        selected_word = r.get("word_of_the_day")

        if selected_word:
            word_redis = json.loads(selected_word)
            return word_redis

        else:
            print("No word of the day found in Redis, generating a new one.")
            
            with open('saved_words.json', 'r') as file:
                word_list = json.load(file)
                
            random_word = random.choice(word_list)
            new_word = {
                "word": random_word["word"],
                "definition": random_word["meaning"],
                "tags": random_word["tags"]
            }

            r.set("word_of_the_day", json.dumps(new_word),ex=86400)
            return new_word

    except Exception:
        print("Please check the Redis server connection and ensure it is running.")
