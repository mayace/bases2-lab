from flask import Flask, render_template
from flask_mongoengine import MongoEngine
import pyodbc

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
    "db": "lab-bases2", "host": "104.248.234.39", "port": 27017,
}
db = MongoEngine()
db.init_app(app)


@app.route("/check_updates")
def check_updates():
    return "dude"


@app.route("/")
def index():
    # User(name="bruh", email="cesar.etx@gmail.com").save()
    # users = User.objects.all()

    conn = pyodbc.connect(
        "Driver={SQL Server};Server=.\SQLEXPRESS;Database=PruebaTecnica;Trusted_Connection=yes;")
    cursor = conn.cursor()
    cursor.execute("select * from dbo.Auto")
    print(conn)

    for item in cursor:
        for i, col in enumerate(cursor.columns(table="Auto")):
            value = item[i]
            print(col.column_name, value)

            
    return render_template("index.html", users=[])
