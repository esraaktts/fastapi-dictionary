from fastapi import FastAPI, Request
from dictionary_api import word_info
from word_day_api import word_of_the_day
from trending_api import trending_words

app = FastAPI()

@app.get("/app/healthy")
def health():
    return {"system":"success"}

@app.get("/app/words/{word}")
def get_word(word: str):
    res = word_info(word)
    return res

@app.get("/app/trending/{word}")
def trending(word: str):
    res = trending_words(word)
    return res

@app.get("/app/word_of_the_day")
def get_word_of_the_day():
    return word_of_the_day()

@app.get("/app/user_id")
def get_user_id(reqst: Request):
  return get_user_id

@app.get("/app/user_history")
def get_history(reqst: Request):
    return get_history