# Find National Park Application

## Overview
The **Find Your Park** application is a Flask-based web app that helps users explore **National Parks** in the United States. Users can select a state, view a list of available parks, choose a visit date using an integrated calendar, and view detailed information about each park, including images, descriptions, activities, and locations.

## Features
- **State Selection**: Users can select a state from a dropdown menu to explore parks.
- **Filtered Results**: Only national parks are displayed, excluding monuments and trails.
- **Park Details**: View detailed information about a selected park, including:
  - Name
  - Description
  - Activities
  - Location
  - Images
- **Calendar Integration**: Choose a visit date using an intuitive calendar.
- **Responsive Design**: Aesthetic and user-friendly interface with a focus on accessibility.

---

## Technologies Used
- **Frontend**:
  - HTML5
  - CSS3 (Custom Styles with `Bebas Neue` font)
- **Backend**:
  - Flask (Python)
  - Flask-WTF (Forms)
- **APIs**:
  - National Park Service (NPS) API
- **Environment Management**:
  - Python `dotenv` for secure API key management
- **Date Picker**:
  - `tkinter` Calendar for date selection (desktop fallback)

---

## Prerequisites
1. Python 3.8+ installed on your machine.
2. `pip` for managing Python packages.
3. An API key for the [National Park Service API](https://www.nps.gov/subjects/developer/get-started.htm).

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url/find-your-park.git
   cd find-your-park
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your API key:
   - Create a `.env` file in the project root with the following content:
     ```
     NPS_API_KEY=your_api_key_here
     ```

5. Run the Flask application:
   ```bash
   python app.py
   ```

6. Open the link provided in the terminal (e.g., `http://127.0.0.1:7070`) in your browser.

---

## Usage
1. Select a state from the dropdown menu.
2. View a list of available National Parks (if any).
3. Select a park to see its details.
4. Use the calendar to choose a visit date.
5. Submit your selection to view tailored park details.

---

## Folder Structure
```
find-your-park/
├── .env                   # Environment variables
├── app.py                 # Main Flask application
├── NPS_Api.py             # Functions for interacting with the NPS API
├── templates/
│   └── index.html         # HTML template
├── static/
│   ├── styles.css         # CSS styles
│   ├── Main-Pic.jpeg      # Background image for landing section
│   └── Logo.png           # Application logo
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## Troubleshooting
### Common Issues:
1. **Missing API Key**: Ensure your `.env` file contains the correct NPS API key.
2. **State with No Parks**: If no parks are available in a selected state, a message is displayed.
3. **Server Not Running**: Ensure you activate the virtual environment and run `python app.py`.

---


## Contributors
- **Claudia Espinosa** - Developer
- [https://github.com/Claudiae09](https://github.com/Claudiae09)
- **Luiciano ** - Developer
- [https://github.com/LucianoDSCAR](https://github.com/LucianoDSCAR)
- **Mauricio Rivas** - Developer
- [https://github.com/mriva077](https://github.com/mriva077)
- **Rafael N** - Developer
- [https://github.com/rniev](https://github.com/rniev)

