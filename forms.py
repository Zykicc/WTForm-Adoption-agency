from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, url, Length, NumberRange



class AddPetForm(FlaskForm):
  """Form for adding pets."""

  name = StringField("Pet Name",
        validators=[InputRequired()],)
  
  species = StringField("Species")
  
  photo_url = StringField("Photo URL",
        validators=[Optional(), url()],)
  
  age = FloatField("Age",
        validators=[Optional(), NumberRange(min=0, max=30)],)
  
  notes = TextAreaField("Notes",
        validators=[Optional(), Length(min=10)],)


class EditPetForm(FlaskForm):
  """Form for editing and existing pet"""

  photo_url = StringField(
        "Photo URL",
        validators=[Optional(), url()],
    )

  notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

  available = StringField("Available?")
