import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
class APIClient:
    def __init__(self):
        self.base_url = os.getenv("API_BASE_URL")
        print(self.base_url)

    def get(self, endpoint: str, params=None):
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        return response

    def post(self, endpoint: str, json=None):
        # Ensure Content-Type is set to application/json
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f"{self.base_url}{endpoint}", json=json, headers=headers)
        return response

    def put(self, endpoint: str, json=None):
        response = requests.put(f"{self.base_url}{endpoint}", json=json)
        return response

    def delete(self, endpoint: str):
        response = requests.delete(f"{self.base_url}{endpoint}")
        return response
