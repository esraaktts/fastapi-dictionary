from fastapi import FastAPI
from word_info import word_info

app = FastAPI()

@app.get("/app/healthy")
def health():
    return {"system":"success"}


@app.get("/app/words/{word}")
def get_word(word: str):
    res = word_info(word)
    return res