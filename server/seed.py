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
            "image": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fhips.hearstapps.com%2Fhmg-prod%2Fimages%2Fwoman-hiking-at-red-rock-canyon-during-sunset-with-royalty-free-image-1601478369.jpg%3Fcrop%3D0.671xw%3A1.00xh%3B0.137xw%2C0%26resize%3D1200%3A*&tbnid=m-mwFx3NkHSnRM&vet=12ahUKEwj4zcuund2BAxUjrEwKHTnVDOYQMygAegQIARBu..i&imgrefurl=https%3A%2F%2Fwww.runnersworld.com%2Ftraining%2Fa34222588%2Fhow-to-start-hiking%2F&docid=zSEiegGLlZl6SM&w=1200&h=1192&q=hiking&ved=2ahUKEwj4zcuund2BAxUjrEwKHTnVDOYQMygAegQIARBu",
            "description": "Karura has a lot of waterfalls",
            "distance": "50",
            "difficulty": "Beginner friendly"
        },
        {
            "name": "Ngong hills",
            "image": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fhips.hearstapps.com%2Fhmg-prod%2Fimages%2Fwoman-hiking-at-red-rock-canyon-during-sunset-with-royalty-free-image-1601478369.jpg%3Fcrop%3D0.671xw%3A1.00xh%3B0.137xw%2C0%26resize%3D1200%3A*&tbnid=m-mwFx3NkHSnRM&vet=12ahUKEwj4zcuund2BAxUjrEwKHTnVDOYQMygAegQIARBu..i&imgrefurl=https%3A%2F%2Fwww.runnersworld.com%2Ftraining%2Fa34222588%2Fhow-to-start-hiking%2F&docid=zSEiegGLlZl6SM&w=1200&h=1192&q=hiking&ved=2ahUKEwj4zcuund2BAxUjrEwKHTnVDOYQMygAegQIARBu",
            "description": "Ngong hills has beautiful views",
            "distance": "30",
            "difficulty": "Veteran"
        },
         {
            "name": "Longonot ",
            "image": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fhips.hearstapps.com%2Fhmg-prod%2Fimages%2Fwoman-hiking-at-red-rock-canyon-during-sunset-with-royalty-free-image-1601478369.jpg%3Fcrop%3D0.671xw%3A1.00xh%3B0.137xw%2C0%26resize%3D1200%3A*&tbnid=m-mwFx3NkHSnRM&vet=12ahUKEwj4zcuund2BAxUjrEwKHTnVDOYQMygAegQIARBu..i&imgrefurl=https%3A%2F%2Fwww.runnersworld.com%2Ftraining%2Fa34222588%2Fhow-to-start-hiking%2F&docid=zSEiegGLlZl6SM&w=1200&h=1192&q=hiking&ved=2ahUKEwj4zcuund2BAxUjrEwKHTnVDOYQMygAegQIARBu",
            "description": "Longonot is the biggest crater in kenya",
            "distance": "30",
            "difficulty": "Moderate"
        }
    ]
    for data in hike_data:
        hike = Hike(**data)
        db.session.add(hike)

    db.session.commit()
print("done seeding")


