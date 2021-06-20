from flask import Flask, render_template
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
    "db": "lab-bases2", "host": "104.248.234.39", "port": 27017,
}
db = MongoEngine()
db.init_app(app)


class User(db.Document):
    name = db.StringField()
    email = db.EmailField()


@app.route("/")
def hello_world():
    # User(name="bruh", email="cesar.etx@gmail.com").save()
    users = User.objects.all()
    return render_template("index.html", users=users)
