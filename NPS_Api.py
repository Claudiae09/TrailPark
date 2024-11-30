from dotenv import load_dotenv
import os
import requests
import tkinter as tk
from tkcalendar import Calendar

# Load environment variables from a .env file
load_dotenv(dotenv_path=".gitignore/.env")  # Ensure path is correct

# Access the API key
API_KEY = os.getenv('NPS_API_KEY')
if not API_KEY:
    raise ValueError("NPS_API_KEY environment variable not set!")

BASE_URL = "https://developer.nps.gov/api/v1"

def get_parks_by_state(state_code):
    url = f"{BASE_URL}/parks?stateCode={state_code}&api_key={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP codes >= 400
        return response.json().get('data', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching parks: {e}")
        return []

def get_park_details(park_code):
    url = f"{BASE_URL}/parks?parkCode={park_code}&api_key={API_KEY}"  # Corrected endpoint
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get('data'):
            park = data.get('data')[0]
            address = park.get("addresses", [{}])[0]  # Safely handle addresses
            return {
                "name": park.get("fullName", "Unknown Park"),
                "description": park.get("description", "No description available"),
                "activities": [activity["name"] for activity in park.get("activities", [])],
                "location": f"{address.get('city', 'Unknown city')}, {address.get('stateCode', '')}",
                "image_url": park.get("images", [{}])[0].get("url", None)
            }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching park details: {e}")
    return None

def run_calendar_app():
    def show_selected_date():
        selected_date = calendar.get_date()
        label.config(text=f"You selected: {selected_date}")

# Create the main application window
    root = tk.Tk()
    root.title("Date Picker")

# Create and place the Calendar widget
    calendar = Calendar(root, selectmode='day', year=2024, month=12, day=1)
    calendar.pack(pady=20)

# Button to confirm the selection
    select_button = tk.Button(root, text="Select Date", command=show_selected_date)
    select_button.pack(pady=10)

# Label to display the selected date
    label = tk.Label(root, text="")
    label.pack(pady=10)

# Run the application
    root.mainloop()

if __name__ == '__main__':
    run_calendar_app()
