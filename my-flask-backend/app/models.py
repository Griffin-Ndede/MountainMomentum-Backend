from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
	
#Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(50))

# Define the relationship between User and Booking
bookings = db.relationship('Booking', backref='user', lazy=True)
# Define the relationship between User and Reviews
reviews = db.relationship('Review', backref='user', lazy=True)
#Define the Hike model
class Hike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    distance = db.Column(db.Integer)
    difficulty = db.Column(db.String)
    location = db.Column(db.String)

# Define the relationship between Hike and Booking
bookings = db.relationship('Booking', backref='hike', lazy=True)
# Define the relationship between Hike and Reviews
reviews = db.relationship('Review', backref='hike', lazy=True)
#Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    hike_id = db.Column(db.Integer, db.ForeignKey('hike.id'), nullable=False)

#Define the Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    hike_id = db.Column(db.Integer, db.ForeignKey('hike.id'), nullable=False)


