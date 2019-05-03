from flask_wtf import FlaskForm
from wtforms import SubmitField

class SubmitForm(FlaskForm):
    submit = SubmitField('See Movie Info')

class ShowDirector(FlaskForm):
    submit = SubmitField('See Director Info')

class GetDirectorLink(FlaskForm):
    submit = SubmitField('Get Director IMDB Link')
