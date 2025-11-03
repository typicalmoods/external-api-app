import requests
from requests.exceptions import RequestException
from config import Config

class APIClient:
    def __init__(self, base_url=None):
        self.base_url = base_url or Config.API_BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def get_data(self, endpoint, params=None):
        """
        Make a GET request to the specified endpoint
        
        Args:
            endpoint (str): API endpoint (e.g., 'posts', 'users')
            params (dict, optional): Query parameters
            
        Returns:
            dict or list: Parsed JSON response
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error fetching data from {url}: {e}")
            return None

    def __del__(self):
        self.session.close()
