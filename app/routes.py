from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import SubmitForm

@app.route('/')
@app.route('/index')
def index():
    form = SubmitForm()

    return render_template('index.html', title='Home', form=form)
