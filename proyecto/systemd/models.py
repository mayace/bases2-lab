from mongoengine import Document, StringField
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import DateTimeField, EmbeddedDocumentField, FloatField, IntField, ListField, ReferenceField
import datetime


class NetflixUpdate(Document):
    start_date_param = DateTimeField()
    total = IntField()
    start_date = DateTimeField(default=datetime.datetime.utcnow)
    end_date  = DateTimeField()


class Episode (EmbeddedDocument):
    name = StringField()
    number = IntField()


class Genre(EmbeddedDocument):
    name = StringField()


class Movie(Document):
    netflix_id = IntField()
    title = StringField()
    imdb_rating = FloatField()
    year = IntField()
    created_at = DateTimeField()

    episodes = ListField(EmbeddedDocumentField(Episode), default=list)
    genres = ListField(EmbeddedDocumentField(Genre), default=list)

    netflix_update = ReferenceField(NetflixUpdate)

    # start_year = IntField()
    # end_year = IntField()
    # run_time = IntField()

    # alternative_titles = ListField(StringField(), default=list)
    # languages = ListField(StringField(), default=list)
    # regions = ListField(StringField(), default=list)
    # categories = ListField(StringField(), default=list)
    # genres = ListField(StringField(), default=list)
