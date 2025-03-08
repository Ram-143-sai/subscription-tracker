from . import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(128))
    subscriptions = db.relationship('Subscription', backref='user', lazy=True)
    is_admin = db.Column(db.Boolean, default=False)

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    price = db.Column(db.Float)
    trial_end = db.Column(db.DateTime)
    cancellation_link = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))