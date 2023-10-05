from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import User, Hike, Booking, Review, db

app = Flask(__name__)

# Configure your database URI here (SQLite example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hikes.db'
db.init_app(app)#initialize db with app

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Define routes for your API

# Welcome endpoint
@app.route('/')
def hello():
    return 'Hello, World!'

#************************HIKES ROUTES************************

# Route to create a new hike
@app.route('/hikes', methods=['POST'])
def create_hike():
    data = request.json
    new_hike = Hike(
        name=data['name'],
        description=data['description'],
        distance=data['distance'],
        difficulty=data['difficulty'],
        location=data['location']
    )
    db.session.add(new_hike)
    db.session.commit()
    return jsonify({'message': 'Hike created successfully'}), 201

# Route to get all hikes
@app.route('/hikes', methods=['GET'])
def get_hikes():
    hikes = Hike.query.all()
    hike_list = []
    for hike in hikes:
        hike_data = {
            'id': hike.id,
            'name': hike.name,
            'description': hike.description,
            'distance': hike.distance,
            'difficulty': hike.difficulty,
            'location': hike.location
        }
        hike_list.append(hike_data)
    return jsonify({'hikes': hike_list})

# Route to get a specific hike by ID
@app.route('/hikes/<int:hike_id>', methods=['GET'])
def get_hike(hike_id):
    hike = Hike.query.get(hike_id)
    if hike is None:
        return jsonify({'message': 'Hike not found'}), 404
    hike_data = {
        'id': hike.id,
        'name': hike.name,
        'description': hike.description,
        'distance': hike.distance,
        'difficulty': hike.difficulty,
        'location': hike.location
    }
    return jsonify({'hike': hike_data})

#**************************USER ROUTES**************************

# # Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            # You may choose to omit the password field from the response for security reasons.
        }
        user_list.append(user_data)
    return jsonify({'users': user_list})

# # Route to get a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    user_data = {
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        # You may choose to omit the password field from the response for security reasons.
    }
    return jsonify({'user': user_data})

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        username=data['username'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=data['password']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201



#********************BOOKING ROUTES************************

# # Route to get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = Booking.query.all()
    booking_list = []
    for booking in bookings:
        booking_data = {
            'id': booking.id,
            'user_id': booking.user_id,
            'hike_id': booking.hike_id,
        }
        booking_list.append(booking_data)
    return jsonify({'bookings': booking_list})

# Route to create a new booking
@app.route('/bookings', methods=['POST'])
def create_booking():
    data = request.json
    new_booking = Booking(
        user_id=data['user_id'],
        hike_id=data['hike_id']
    )
    db.session.add(new_booking)
    db.session.commit()
    return jsonify({'message': 'Booking created successfully'}), 201



#*************************REVIEWS ROUTES*****************************
# Route to get all reviews
@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    review_list = []
    for review in reviews:
        review_data = {
            'id': review.id,
            'description': review.description,
            'user_id': review.user_id,
            'hike_id': review.hike_id,
        }
        review_list.append(review_data)
    return jsonify({'reviews': review_list})

# Route to create a new review
@app.route('/reviews', methods=['POST'])
def create_review():
    data = request.json
    new_review = Review(
        description=data['description'],
        user_id=data['user_id'],
        hike_id=data['hike_id']
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review created successfully'}), 201

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()

    app.run(debug=True)
