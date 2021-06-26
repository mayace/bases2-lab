from settings import SQLS_CONN_STR
from models import Movie
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
    movies = []
    movies = Movie.objects.all().order_by("-created_at")
    return render_template("index.html", movies=movies)
