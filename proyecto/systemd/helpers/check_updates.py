from flask.app import Flask
import pyodbc
from models import Movie


class Handler():
    def __init__(self, sql_connection_str=None) -> None:
        self.sql_connection_str = sql_connection_str

    def create_sqlserver_connection(self):
        return pyodbc.connect(self.sql_connection_str)

    def get_updates(self, last_update) -> list:
        conn = self.create_sqlserver_connection()
        cursor = conn.cursor()
        l = list()

        for item in cursor.execute("execute get_updates ?;", last_update):
            l.append(Movie(title=item.title, imdb_rating=item.imdb_rating,
                     netflix_id=item.netflix_id, year=item.year, created_at=item.created_at).save())
        return l

    def execute(self, last_update=None) -> list:
        return self.get_updates(last_update)
