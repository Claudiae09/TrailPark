import os
import requests

# Step 1: Access the API key from the environment variable
API_KEY = os.environ.get('NPS_API_KEY')

if not API_KEY:
    raise ValueError("NPS_API_KEY environment variable not set!")

# Step 2: Define the URL
url = f"https://developer.nps.gov/api/v1/activities/parks?api_key={API_KEY}"

# Step 3: Make the API request
response = requests.get(url)

# Step 4: Check the response and print the data
if response.status_code == 200:
    data = response.json()
    print("Data retrieved successfully:")
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print(response.text)
