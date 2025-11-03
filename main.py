import sys
from typing import Dict, Any
from datetime import datetime, UTC
from pymongo import UpdateOne

from api_client import APIClient
from database import Database

def fetch_data_from_api(endpoint: str, query_params: Dict[str, Any] = None) -> Any:
    """
    Fetch data from the specified API endpoint
    
    Args:
        endpoint: API endpoint to fetch data from
        query_params: Optional query parameters for the API request
        
    Returns:
        dict or list: The data returned from the API, or None if an error occurred
    """
    api_client = APIClient()
    print(f"Fetching data from {endpoint}...")
    data = api_client.get_data(endpoint, query_params)
    
    if not data:
        print("No data received from the API.")
        return None
        
    # Add timestamp to each document
    current_time = datetime.now(UTC)
    if isinstance(data, list):
        for item in data:
            item['_last_updated'] = current_time
    else:
        data['_last_updated'] = current_time
    
    return data

def store_data_in_db(collection_name: str, data: Any) -> None:
    """
    Store data in MongoDB
    
    Args:
        collection_name: Name of the MongoDB collection to store data in
        data: Data to store (can be a single document or a list of documents)
    """
    if data is None:
        return
        
    db = Database.get_database()
    collection = db[collection_name]
    
    # Prepare bulk operations for upsert
    if isinstance(data, list):
        operations = [
            UpdateOne(
                {'id': item['id']},
                {'$set': item},
                upsert=True
            )
            for item in data
        ]
        
        if operations:
            result = collection.bulk_write(operations)
            print(f"Upserted {result.upserted_count} new documents.")
            print(f"Modified {result.modified_count} existing documents.")
    else:
        # Handle single document
        result = collection.update_one(
            {'id': data['id']},
            {'$set': data},
            upsert=True
        )
        print(f"Upserted document with id: {data['id']}")
    
    print(f"Data successfully stored in '{collection_name}' collection.")

def main():
    try:
        posts_data = fetch_data_from_api(
            endpoint='posts',
            query_params={'_limit': 10}
        )
        store_data_in_db('posts', posts_data)
        
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        Database.close_connection()

if __name__ == "__main__":
    main()
