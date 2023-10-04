from models import db, Hike
from random import choice
from app import create_app  
# create the Flask app
app = create_app()

with app.app_context():
    print("seeding hikes...")
    hike_data = [
        {
            "name": "Karura Forest",
            "description": "Karura has a lot of waterfalls",
            "distance": "50",
            "difficulty": "Beginner friendly"
        },
        {
            "name": "Ngong hills",
            "description": "Ngong hills has beautiful views",
            "distance": "30",
            "difficulty": "Veteran"
        }
    ]
    for data in hike_data:
        hike = Hike(**data)
        db.session.add(hike)

    db.session.commit()
print("done seeding")


