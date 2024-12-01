from flask import Flask, render_template, request
from NPS_Api import get_parks_by_state, get_park_details
import os
import requests
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, RadioField, DateField
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'  # Replace with a secure key

# Form to select state and submit
class StateForm(FlaskForm):
    state = SelectField("Select a State", choices=[
        ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'),
        ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'),
        ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'),
        ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'),
        ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
        ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'),
        ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'),
        ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'),
        ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'),
        ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
        ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'),
        ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'), ('WY', 'Wyoming')
    ],
                        render_kw={"id": "state"}
                        )
    submit = SubmitField("Find Parks")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = StateForm()
    parks = None
    parks_details = None
    visit_date = None
    message = None  # To hold the message if no parks are found

    # Process the state selection form
    if form.validate_on_submit():
        selected_state = form.state.data
        parks = get_parks_by_state(selected_state)  # Fetch parks for the selected state

        # Check if no parks were found
        if not parks:
            message = f"Sorry, no National Parks were found in {selected_state}. Please select a different state."

    # Process the radio button submission (if applicable)
    if request.method == "POST" and "selected_park" in request.form:
        selected_park_code = request.form['selected_park']
        parks_details = get_park_details(selected_park_code)
        visit_date = request.form.get('visit_date', None)

    # If a date is selected
    if "visit_date" in request.form:
        visit_date = request.form['visit_date']
        print(f"Selected visit date: {visit_date}")  # Debug or process as needed

    # Render the template with the message
    return render_template(
        'index.html',
        form=form,
        parks=parks,
        parks_details=parks_details,
        visit_date=visit_date,
        message=message
    )

if __name__ == '__main__':
    app.run(debug=True, port=7070)
