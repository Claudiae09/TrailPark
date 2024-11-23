from flask import Flask, render_template
from NPS_Api import get_parks_by_state
import os
import mainfunctions
import requests
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'  # Replace with a secure key

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
    ])
    submit = SubmitField("Find Parks")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = StateForm()
    parks = None
    if form.validate_on_submit():
        selected_state = form.state.data
        # Fetch parks for the selected state using nps_api
        parks = get_parks_by_state(selected_state)

        # Render the form and parks data in the template
    return render_template('index.html', form=form, parks=parks)

if __name__ == '__main__':
    app.run(debug=True, port=7070)