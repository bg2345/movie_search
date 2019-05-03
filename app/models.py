from app import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(500))
    original_title = db.Column(db.String(64))
    # directors = db.relationship('Director', backref='dir', lazy='dynamic')

class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    # using imdb to hold film title, don't want to rewrite database at the moment
    imdb = db.Column(db.String(56))
    profile = db.Column(db.String(256))
    # movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
