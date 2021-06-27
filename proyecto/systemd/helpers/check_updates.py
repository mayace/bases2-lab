import datetime
from flask.app import Flask
import pyodbc
from models import Episode, Genre, Movie, NetflixUpdate


class Handler():
    def __init__(self, sql_connection_str=None) -> None:
        self.sql_connection_str = sql_connection_str

    def create_sqlserver_connection(self):
        return pyodbc.connect(self.sql_connection_str)

    def get_fields(self, item):
        fields = dict()
        fields["imdb_rating"] = getattr(item, "averageRating", None)
        fields["title"] = getattr(item, "primaryTitle", None)
        fields["netflix_id"] = getattr(item, "id", None)
        fields["year"] = getattr(item, "startYear", None)
        fields["created_at"] = getattr(item, "createdAt", None)
        return fields

    def get_genres_query(self) -> str:
        return """
        select g.id, g.name
        from TitleGenre tg
        left join Genre g on g.id = tg.genreId
        where titleId = ?
        """

    def get_episodes_query(self) -> str:
        return """
        select e.id, e.episode, e.season
        from Episode e
        where e.titleId = ?
        """

    def append_genres(self, conn, movie: Movie):
        conn = self.create_sqlserver_connection()
        cursor = conn.cursor()
        query = self.get_genres_query()
        for item in cursor.execute(query, movie.netflix_id):
            genre = Genre()
            genre.name = getattr(item, "name", None)
            movie.genres.append(genre)

    def append_episodes(self, conn, movie: Movie):
        conn = self.create_sqlserver_connection()
        cursor = conn.cursor()
        query = self.get_episodes_query()
        for item in cursor.execute(query, movie.netflix_id):
            doc = Episode()
            doc.name = getattr(item, "episode", None)
            doc.number = getattr(item, "episode", None)
            movie.episodes.append(doc)

    def get_updates(self, last_update) -> list:
        conn = self.create_sqlserver_connection()
        cursor = conn.cursor()
        new_list = list()

        this_update = NetflixUpdate().save()
        for item in cursor.execute("execute select_news_titles ?;", last_update or ""):
            fields = self.get_fields(item)
            if fields.get("netflix_id"):
                movie = Movie(netflix_update=this_update, **fields)
                self.append_episodes(conn, movie)
                self.append_genres(conn, movie)
                movie.save()
                new_list.append(movie)

        this_update.total = len(new_list)
        this_update.end_date = datetime.datetime.utcnow
        this_update.save()

        return new_list

    def execute(self, last_update=None) -> list:
        return self.get_updates(last_update)
