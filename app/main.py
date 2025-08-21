from app.connections import DAL_mongo
import os
from find_min_word import min_word


HOST = os.getenv("HOST", "iranmaldb.gurutam.mongodb.net/")
USER = os.getenv("USER", "IRGC")
PASSWORD = os.getenv("PASSWORD", "iraniraniran")
DB = os.getenv("DATABASE", "IranMalDB")
COLLECTION = os.getenv("COLLECTION", "tweets")


dal = DAL_mongo(HOST, DB, COLLECTION, USER, PASSWORD)

dal.open_connection()

mw = min_word()


tweets = dal.get_all_tweets()


for tweet in tweets:
    text = tweet.get("Text")
    if text:
        rare_word = mw.get_min_word(text)
        print(f"הציוץ: {text}")
        print(f": המילה {rare_word}")
        print("---")