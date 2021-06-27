from settings import SQLS_CONN_STR
from models import Movie, NetflixUpdate
from helpers.check_updates import Handler
from flask import Flask, render_template
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_pyfile("settings.py")
db = MongoEngine()
db.init_app(app)


@app.route("/check_updates")
def check_updates():
    first = Movie.objects.all().order_by("-created_at").first()

    handler = Handler(SQLS_CONN_STR)
    data = handler.execute(last_update=first.created_at if first else None)
    return render_template("last_updates.html", data=data)


@app.route("/")
def index():
    updates = NetflixUpdate.objects.all().order_by("-start_date")
    return render_template("updates.html", updates=updates)


@app.route("/update/<id>/")
def update_detail(id=None):
    update = NetflixUpdate.objects.get(id=id)
    return str(update.id)
    

@app.route("/movies/<update_id>/")
def movies(update_id=None):
    movies = Movie.objects(netflix_update=update_id).order_by("-created_at")
    return render_template("movies.html", movies=movies)

@app.route("/genres/<movie_id>/")
def movie_genres(movie_id=None):
    movie = Movie.objects.get(id=movie_id)
    return render_template("genres.html", movie=movie)

@app.route("/episodes/<movie_id>/")
def movie_episodes(movie_id=None):
    movie = Movie.objects.get(id=movie_id)
    return render_template("episodes.html", movie=movie)