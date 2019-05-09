from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField

class SubmitForm(FlaskForm):
    country = SelectField(u'Country', choices=[('US', 'United States'), ('PL', 'Poland'), ('IN', 'India'), ('FI', 'Finland'), ('CN', 'China')])
    submit = SubmitField('Choose Country')
