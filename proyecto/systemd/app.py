from models import Movie
from settings import MONGODB, NETFLIX_CONNECTION_STR
from helpers.check_updates import Handler
from flask import Flask, render_template
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = MONGODB
db = MongoEngine()
db.init_app(app)


@app.route("/check_updates")
def check_updates():
    first = Movie.objects.all().order_by("-created_at").first()

    handler = Handler(NETFLIX_CONNECTION_STR)
    data = handler.execute(last_update=first.created_at if first else None)
    return render_template("last_updates.html", data=data)


@app.route("/")
def index():
    movies = Movie.objects.all().order_by("-created_at")
    return render_template("index.html", movies=movies)
