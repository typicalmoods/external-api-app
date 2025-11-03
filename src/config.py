import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
    DB_NAME = os.getenv('DB_NAME', 'api_data_db')
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://jsonplaceholder.typicode.com')
