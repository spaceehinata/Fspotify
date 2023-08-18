from . import db, fav_songs
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    number = db.Column(db.Integer)
    favorite_songs = db.relationship('Song', secondary=fav_songs, backref=db.backref('users', lazy='dynamic'))

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    artist = db.Column(db.String(150))
