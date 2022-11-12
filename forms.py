from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField


class AddPetForm(FlaskForm):
    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo")
    age = IntegerField("Age")
    notes = TextAreaField("Notes")
    available = BooleanField("Available")
