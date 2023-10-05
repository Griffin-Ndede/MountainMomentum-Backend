from models import db, Hike
from random import choice
from app import create_app  
# create the Flask app
app = create_app()

with app.app_context():
    print("seeding hikes...")
    hike_data = [
         {
    "name": "Mount Kenya",
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Mount_Kenya.jpg/1200px-Mount_Kenya.jpg",
    "description": "Mount Kenya is the highest mountain in Kenya and the second-highest in Africa. It offers a challenging and rewarding hiking experience. The diverse landscapes include glaciers, alpine meadows, and dense forests.",
    "distance": "60km",
    "difficulty": "Advanced"
  },
  {
    "name": "Aberdare Range",
    "image": "https://images.unsplash.com/photo-1555704475-952d817ce5a2",
    "description": "The Aberdare Range is known for its lush forests, waterfalls, and wildlife. Hiking here allows you to explore the beautiful moorlands and spot various animal species, including elephants and leopards.",
    "distance": "45km",
    "difficulty": "Intermediate"
  },
  {
    "name": "Hell's Gate National Park",
    "image": "https://images.unsplash.com/photo-1550863313-8f46a9eb5e92",
    "description": "Hell's Gate National Park is famous for its stunning scenery and unique rock formations. You can hike through the dramatic canyons and enjoy views of geothermal activity.",
    "distance": "15km",
    "difficulty": "Beginner friendly"
  },
  {
    "name": "Mount Elgon",
    "image": "https://images.unsplash.com/photo-1574219220047-45ad7b964711",
    "description": "Mount Elgon is an extinct volcano on the border of Kenya and Uganda. Hiking here takes you through pristine forests, caves, and waterfalls. The caldera at the summit is a must-see.",
    "distance": "40km",
    "difficulty": "Intermediate"
  },
  {
    "name": "Aberdare Range",
    "image": "https://images.unsplash.com/photo-1555704475-952d817ce5a2",
    "description": "The Aberdare Range is known for its lush forests, waterfalls, and wildlife. Hiking here allows you to explore the beautiful moorlands and spot various animal species, including elephants and leopards.",
    "distance": "45km",
    "difficulty": "Intermediate"
  },
  {
    "name": "Hell's Gate National Park",
    "image": "https://images.unsplash.com/photo-1550863313-8f46a9eb5e92",
    "description": "Hell's Gate National Park is famous for its stunning scenery and unique rock formations. You can hike through the dramatic canyons and enjoy views of geothermal activity.",
    "distance": "15km",
    "difficulty": "Beginner friendly"
  },
  {
    "name": "Mount Elgon",
    "image": "https://images.unsplash.com/photo-1574219220047-45ad7b964711",
    "description": "Mount Elgon is an extinct volcano on the border of Kenya and Uganda. Hiking here takes you through pristine forests, caves, and waterfalls. The caldera at the summit is a must-see.",
    "distance": "40km",
    "difficulty": "Intermediate"
  }
    ]
    for data in hike_data:
        hike = Hike(**data)
        db.session.add(hike)

    db.session.commit()
print("done seeding")


