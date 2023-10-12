from sqlalchemy.orm import validates
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Defining the models
class UserSignup(db.Model):

    __tablename__ = "UserSignup"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    first_name = db.Column(db.String(), nullable=False, unique=True)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)    
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Define the relationship between User and Booking
    bookings = db.relationship('Booking', backref='user', lazy=True)
    # Define the relationship between User and Reviews
    reviews = db.relationship('Review', backref='user', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('UserSignup.id'), nullable=False)
    hike_id = db.Column(db.Integer, db.ForeignKey('Hike.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Hike(db.Model):
   
   __tablename__ = "Hike"
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(), nullable=False)
   image = db.Column(db.String(), nullable=False)
   description = db.Column(db.String(), nullable=False)
   distance = db.Column(db.String(), nullable=False)
   difficulty = db.Column(db.String(), nullable=False)
   
   # Define the relationship between Hike and Booking
   bookings = db.relationship('Booking', backref='hike', lazy=True)
   # Define the relationship between Hike and Reviews
   reviews = db.relationship('Review', backref='hike', lazy=True)

class Review(db.Model):

    __tablename__ ="Reviews"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('UserSignup.id'), nullable=False)
    hike_id = db.Column(db.Integer, db.ForeignKey('Hike.id'), nullable=False)
