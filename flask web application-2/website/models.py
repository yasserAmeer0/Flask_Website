from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func, update


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))
    quantity = db.Column(db.Integer)
    details = db.Column(db.String(10000))
    price1 = db.Column(db.Integer)
    price2 = db.Column(db.Integer)
    price3 = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    user_status = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')