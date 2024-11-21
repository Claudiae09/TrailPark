from dotenv import load_dotenv
import os
import requests

# Load environment variables from a .env file
load_dotenv()

# Access the API key
API_KEY = os.getenv('NPS_API_KEY')

if not API_KEY:
    raise ValueError("NPS_API_KEY environment variable not set!")

# Use the API key in your request
url = f"https://developer.nps.gov/api/v1/activities/parks?api_key={API_KEY}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Data retrieved successfully:", data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
