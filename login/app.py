from flask import Flask, request, jsonify ,session, flash, redirect, url_for
from models import db
import re
from flask_migrate import Migrate, migrate
from werkzeug.security import generate_password_hash, check_password_hash

# creating a flask application instance
app = Flask(__name__)
# specifying database file name
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:/// mountainmomentum.db"

# initializing the database with flask application
db.init_app(app)

from models import UserSignup, Hike
# creating the database tables with flask application context
with app.app_context():
    db.create_all()
# Setting up the migrations
migrate = Migrate(app, db)

# secret key for sessions
app.secret_key = "mountainmomentum"

# defining the routes
@app.route('/')
def home():
    return 'Flask is working'

@app.route("/hikes", methods=["GET", 'POST'])
def hikes():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        distance = request.form['distance']
        difficulty = request.form['difficulty']

        # saving new hiking trails to the database
        new_hike = Hike(name=name, description=description, distance=distance, difficulty=difficulty)
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
                "description":hike.description,
                "distance": hike.distance,
                "difficulty": hike.difficulty,
            }
            for hike in hiking_lists
        ]
        return jsonify(hiking_json)
    else:
        return "Invalid request method"
    
@app.route("/login", methods= ['GET', 'POST'])
def login():
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        username = request.form['username']
        password = request.form['password']
        user = UserSignup.query.filter_by(username=username, password=password).first()

        if user and check_password_hash (user.password_hash, password):
            session["loggedin"] = True
            session["id"]= user.id
            session["username"] = user.username

            # flash success message
            flash('Logged in successfully', "success")
            # redirect to a different route
            return redirect(url_for("home"))
        else:
            return "Incorrect username/password!", "error"

if __name__ == "__main__":
    app.run()