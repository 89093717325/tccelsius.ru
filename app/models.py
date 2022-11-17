from app import db
from datetime import datetime


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.Text())
    price = db.Column(db.Integer)
    transmission = db.Column(db.String(128))
    img = db.Column(db.String(128))
    img1 = db.Column(db.String(128))
    img2 = db.Column(db.String(128))
    img3 =db.Column(db.String(128))
    available = db.Column(db.Boolean, default=True)

class Rent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer)
    date_and_time_rent_start = db.Column(db.DateTime, default=None)
    date_and_time_rent_end = db.Column(db.DateTime, default=None)