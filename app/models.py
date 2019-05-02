from app import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(500))
    original_title = db.Column(db.String(64))
    directors = db.relationship('Director', backref='name', lazy='dynamic')

class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    imdb = db.Column(db.String(56))
