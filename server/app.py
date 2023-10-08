# from flask import Flask, request, jsonify ,session, flash, redirect, url_for
# from models import db
# import re
# from flask_migrate import Migrate, migrate
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_cors import CORS
# from models import UserSignup, Hike, Review

# # creating a flask application instance
# def create_app():
#     app = Flask(__name__)

# # secret key for sessions
#     app.secret_key = "mountainmomentum"

# # specifying database file name
#     app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mountainmomentum.db"

# # initializing the database with flask application
#     db.init_app(app)
#     return app

# app = create_app()
# # creating the database tables with flask application context
# with app.app_context():
#     db.create_all()
# # Setting up the migrations
# migrate = Migrate(app, db)

# CORS(app)
# # defining the routes
# @app.route('/')
# def home():
#     return 'Flask is working'

# @app.route("/hikes", methods=["GET", 'POST'])
# def hikes():
#     if request.method == 'POST':
#         name = request.form['name']
#         image = request.form["image"]
#         description = request.form['description']
#         distance = request.form['distance']
#         difficulty = request.form['difficulty']

#         # saving new hiking trails to the database
#         new_hike = Hike(name=name, image=image, description=description, distance=distance, difficulty=difficulty)
#         db.session.add(new_hike)
#         db.session.commit()

#         return "New hiking trail successfully added"
    
#     elif request.method == 'GET':
#         # retrieving hiking trails from the database
#         hiking_lists = Hike.query.all()
#         hiking_json = [
#             {
#                 "id":hike.id,
#                 "name":hike.name,
#                 "image": hike.image,
#                 "description":hike.description,
#                 "distance": hike.distance,
#                 "difficulty": hike.difficulty,
#             }
#             for hike in hiking_lists
#         ]
#         return jsonify(hiking_json)
#     else:
#         return "Invalid request method", 400
    
# @app.route("/login", methods= ['GET', 'POST'])
# def login():
#     if request.method == "POST" and "username" in request.form and "password" in request.form:
#         username = request.form['username']
#         password = request.form['password']
#         user = UserSignup.query.filter_by(username=username).first()

#         if user and check_password_hash (user.password, password):
#             session["loggedin"] = True
#             session["id"]= user.id
#             session["username"] = user.username

#             # flash success message
#             flash('Logged in successfully', "success")
#             # redirect to a different route
#             return redirect(url_for("home"))
#         else:
#             return "Incorrect username/password!", 400

# @app.route('/logout')
# def logout():
#     session.pop("loggedin", None)
#     session.pop("id", None)
#     session.pop("username", None)
#     return redirect(url_for('login'))

# @app.route('/register', methods = ['GET', "POST"])
# def register():
#     if request.method == "POST":

#         # retrieving the data from the form
#         username =request.form["username"]
#         password = request.form["password"]
#         email = request.form["email"]
#         first_name = request.form["first_name"]
#         last_name = request.form["last_name"]

# # check if the username or email already exists
#         user_exists = UserSignup.query.filter_by(username= username).first()
#         email_exists = UserSignup.query.filter_by(email=email).first()

#         if user_exists:
#             return "Account already exists", 400
#         elif email_exists:
#             return "Email already exists", 400
#         elif not username or not password or not email or not first_name or not last_name:
#             return "Please fill out the entire form", "error"
#         elif not re.match(r'[^@]+@[^@]+\.[^@]+', email) or not re.match(r'[A-Za-z0-9]+', username):
#             return "Invalid email address or username", "error"
#         else:
#         # hashing the password before storing it in the database
#             password = generate_password_hash(password, method="sha256")
#             new_user = UserSignup(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
#             db.session.add(new_user)
#             db.session.commit()

#         return "You have successfully registered!"

#     # Redirect the user, if the registration is successful
#     return redirect(url_for("home"))
# @app.route("/reviews", methods=["POST"])
# def add_review():
#     if request.method == "POST":
#         if "user_id" in session:
#             user_id = session["user_id"]
#             hike_id = request.form["hike_id"]
#             description = request.form["description"]

#             # Create a new review and add it to the database
#             new_review = Review(user_id=user_id, hike_id=hike_id, description=description)
#             db.session.add(new_review)
#             db.session.commit()

#             return "Review added successfully"
#         else:
#             return "You must be logged in to add a review", 401
#     else:
#         return "Invalid request method", 400

# @app.route("/reviews/<int:review_id>", methods=["PATCH", "DELETE"])
# def edit_or_delete_review(review_id):
#     if request.method == "PATCH":
#         if "user_id" in session:
#             user_id = session["user_id"]
#             updated_description = request.form["description"]

#             # Find the review by ID and check if it belongs to the logged-in user
#             review = Review.query.filter_by(id=review_id, user_id=user_id).first()

#             if review:
#                 review.description = updated_description
#                 db.session.commit()
#                 return "Review updated successfully"
#             else:
#                 return "Review not found or you do not have permission to edit it", 404
#         else:
#             return "You must be logged in to edit a review", 401

#     elif request.method == "DELETE":
#         if "user_id" in session:
#             user_id = session["user_id"]

#             # Find the review by ID and check if it belongs to the logged-in user
#             review = Review.query.filter_by(id=review_id, user_id=user_id).first()

#             if review:
#                 db.session.delete(review)
#                 db.session.commit()
#                 return "Review deleted successfully"
#             else:
#                 return "Review not found or you do not have permission to delete it", 404
#         else:
#             return "You must be logged in to delete a review", 401


# if __name__ == "__main__":
#     app.run()
from flask import Flask, request, jsonify ,session, flash, redirect, url_for
from models import db
import re
from flask_migrate import Migrate, migrate
from flask_cors import CORS
from models import   UserSignup, Hike, Review

# creating a flask application instance
def create_app():
    app = Flask(__name__)

    # secret key for sessions
    app.secret_key = "mountainmomentum"

    # specifying the database file name
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mountainmomentum.db"

    # initializing the database with flask application
    db.init_app(app)
    return app

app = create_app()

# creating the database tables with flask application context
with app.app_context():
    db.create_all()

# Setting up the migrations
migrate = Migrate(app, db)

CORS(app)

# defining the routes
@app.route('/')
def home():
    return 'Flask is working'

@app.route("/hikes", methods=["GET", 'POST'])
def hikes():
    if request.method == 'POST':
        name = request.form['name']
        image = request.form["image"]
        description = request.form['description']
        distance = request.form['distance']
        difficulty = request.form['difficulty']

        # saving new hiking trails to the database
        new_hike = Hike(name=name, image=image, description=description, distance=distance, difficulty=difficulty)
        db.session.add(new_hike)
        db.session.commit()

        return "New hiking trail successfully added"
    
    elif request.method == 'GET':
        # retrieving hiking trails from the database
        hiking_lists = Hike.query.all()
        hiking_json = [
            {
                "id":hike.id,
                "name":hike.name,
                "image": hike.image,
                "description":hike.description,
                "distance": hike.distance,
                "difficulty": hike.difficulty,
            }
            for hike in hiking_lists
        ]
        return jsonify(hiking_json)
    else:
        return "Invalid request method", 400
    
@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Fetch the user by username
    user = UserSignup.query.filter_by(username=username).first()

    if user and user.password == password:  # This is for simplicity, not recommended for production
        # Authentication successful
        session["loggedin"] = True
        session["user_id"] = user.id
        session["username"] = user.username
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Incorrect username/password'}), 401

@app.route('/logout')
def logout():
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("username", None)
    return redirect(url_for('login'))

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    # Check if the username or email already exists in the database (you should hash passwords)
    existing_user = UserSignup.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    existing_email = UserSignup.query.filter_by(email=email).first()
    if existing_email:
        return jsonify({'message': 'Email already exists'}), 400

    new_user = UserSignup(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Registration successful'}), 200
@app.route("/reviews", methods=["POST"])
def add_review():
    if request.method == "POST":
        if "user_id" in session:
            user_id = session["user_id"]
            hike_id = request.form["hike_id"]
            description = request.form["description"]

            # Create a new review and add it to the database
            new_review = Review(user_id=user_id, hike_id=hike_id, description=description)
            db.session.add(new_review)
            db.session.commit()

            return "Review added successfully"
        else:
            return "You must be logged in to add a review", 401
    else:
        return "Invalid request method", 400

@app.route("/reviews/<int:review_id>", methods=["PATCH", "DELETE"])
def edit_or_delete_review(review_id):
    if request.method == "PATCH":
        if "user_id" in session:
            user_id = session["user_id"]
            updated_description = request.form["description"]

            # Find the review by ID and check if it belongs to the logged-in user
            review = Review.query.filter_by(id=review_id, user_id=user_id).first()

            if review:
                review.description = updated_description
                db.session.commit()
                return "Review updated successfully"
            else:
                return "Review not found or you do not have permission to edit it", 404
        else:
            return "You must be logged in to edit a review", 401

    elif request.method == "DELETE":
        if "user_id" in session:
            user_id = session["user_id"]

            # Find the review by ID and check if it belongs to the logged-in user
            review = Review.query.filter_by(id=review_id, user_id=user_id).first()

            if review:
                db.session.delete(review)
                db.session.commit()
                return "Review deleted successfully"
            else:
                return "Review not found or you do not have permission to delete it", 404
        else:
            return "You must be logged in to delete a review", 401

if __name__ == "__main__":
    app.run()
