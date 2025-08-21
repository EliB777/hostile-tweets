from pymongo import MongoClient

class DAL_mongo:

    def __init__(self, host= "iranmaldb.gurutam.mongodb.net/", database= "IranMalDB", collection= "tweets", user= "IRGC", password= "iraniraniran"):
        self.host = host
        self.database = database
        self.collection = collection
        self.user = user
        self.password = password
        self.URI = self.get_URI()
        self.client = None


    def get_URI(self):
        if self.user and self.password:
            URI = f"mongodb+srv://{self.user}:{self.password}@{self.host}"
        else:
            URI = f"mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/"

        return URI

    def open_connection(self):
        try:
            self.client = MongoClient(self.URI)
            print("Connection established")
            return True
        except Exception as e:
            print("Error: ", e)
            return False




    def close_connection(self):
        if self.client:
            self.client.close()

    def get_all_tweets(self):
        if not self.client:
            self.open_connection()
        db = self.client[self.database]
        collection = db[self.collection]
        return collection.find()