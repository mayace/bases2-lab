from flask.app import Flask
import pyodbc
from models import Movie


class Handler():
    def __init__(self, sql_connection_str=None) -> None:
        self.sql_connection_str = sql_connection_str

    def create_sqlserver_connection(self):
        return pyodbc.connect(self.sql_connection_str)

    def get_updates(self, from)->list :
        conn = self.create_sqlserver_connection()
        cursor = conn.Cursor()

        for row in cursor.execute("execute "):
            print(row.user_id, row.user_name)
        return []

    

    def execute(self, last_update = None):
        updates = self.get_updates(last_update)

        for item in updates:

