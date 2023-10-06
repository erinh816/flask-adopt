"""Flask app for adopt app."""

import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get("/")
def list_pets_home_page():
    """get all pets and render them to home page"""

    pets = Pet.query.all()
    return render_template('list-pets.html', pets=pets)
