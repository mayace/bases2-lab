from mongoengine import Document, StringField
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import DateTimeField, FloatField, IntField, ListField


class Movie(Document):
    netflix_id = IntField()
    title = StringField()
    imdb_rating = FloatField()
    year = IntField()
    episodes = ListField(StringField(), default=list) # solo total

    created_at = DateTimeField()
    # genres = ListField(StringField(), default=list) # solo total

    # start_year = IntField()
    # end_year = IntField()
    # run_time = IntField()

    # alternative_titles = ListField(StringField(), default=list)
    # languages = ListField(StringField(), default=list)
    # regions = ListField(StringField(), default=list)
    # categories = ListField(StringField(), default=list)
    # genres = ListField(StringField(), default=list)
