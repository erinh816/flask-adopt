"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL


class AddPetForm(FlaskForm):
    """Form for adding pets to adoption list"""

    name = StringField("Pet's name", validators=[InputRequired()])

    species = SelectField("Species", choices=[
        ('cat', 'Cat'),
        ('dog', 'Dog'),
        ('porcupine', 'Porcupine')
    ], validators=[InputRequired()])

    photo_url = StringField("Photo URL", validators=[URL()])

    age = SelectField('Age', choices=[
        ('baby', 'Baby'),
        ('young', 'Young'),
        ('adult', 'Adult'),
        ('senior', 'Senior')
    ], validators=[InputRequired()])

    notes = TextAreaField(
        "Notes",
        validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing pet"""

    photo_url = StringField("Photo URL", validators=[URL()])

    notes = TextAreaField(
        "Notes",
        validators=[Optional()])

    available = BooleanField("Available")
