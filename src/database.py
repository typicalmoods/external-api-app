from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from config import Config

class Database:
    _instance = None
    _client = None
    _db = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            try:
                cls._client = MongoClient(Config.MONGODB_URI)
                # The ismaster command is cheap and does not require auth
                cls._client.admin.command('ismaster')
                cls._db = cls._client[Config.DB_NAME]
                print("Connected to MongoDB successfully!")
            except ConnectionFailure as e:
                print(f"Failed to connect to MongoDB: {e}")
                raise
        return cls._instance

    @classmethod
    def get_database(cls):
        if cls._db is None:
            cls()
        return cls._db

    @classmethod
    def close_connection(cls):
        if cls._client:
            cls._client.close()
            cls._client = None
            cls._db = None
            print("MongoDB connection closed.")
