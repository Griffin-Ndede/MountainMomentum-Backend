from sqlalchemy.orm import validates
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# defining the models
class UserSignup(db.Model):

    __tablename__ = "UserSignup"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    first_name = db.Column(db.String(), nullable=False, unique=True)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)    
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    user_id = db.Column(db.Integer(), nullable=False, unique=True)
    hike_id = db.Column(db.Integer(), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Hike(db.Model):
   
   __tablename__ = "Hike"
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(), nullable=False, unique=True)
   description = db.Column(db.String(), nullable=False)
   distance = db.Column(db.String(), nullable=False)
   difficulty =db.Column(db.String(), nullable=False)
