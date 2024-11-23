from dotenv import load_dotenv
import os
import requests

# Load environment variables from a .env file
load_dotenv(dotenv_path=".gitignore/.env")

# Access the API key
API_KEY = os.getenv('NPS_API_KEY')
if not API_KEY:
    raise ValueError("NPS_API_KEY environment variable not set!")

BASE_URL = "https://developer.nps.gov/api/v1"

def get_parks_by_state(state_code):
    url = f"{BASE_URL}/parks?stateCode={state_code}&api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print(f"Error fetching parks: {response.status_code}")
        return []



