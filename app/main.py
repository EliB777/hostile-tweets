from app.connections import DAL_mongo
import os



HOST = os.getenv("HOST", "iranmaldb.gurutam.mongodb.net/")
USER = os.getenv("USER", "IRGC")
PASSWORD = os.getenv("PASSWORD", "iraniraniran")
DB = os.getenv("DATABASE", "IranMalDB")
COLLECTION = os.getenv("COLLECTION", "tweets")


dal = DAL_mongo(HOST, DB, COLLECTION, USER, PASSWORD)

dal.open_connection()
