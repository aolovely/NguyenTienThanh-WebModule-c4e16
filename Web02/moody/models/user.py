from mongoengine import *

class User(Document):
    fullname = StringField()
    email = emailField()
    username = StringField()
    password = StringField()
class Song(Document):
    happy = IntField()
    name = StringField()
    singer = StringField()
    link = StringField()
    link_img = StringField()
    user_id = ReferenceField(User)
class Book(Document):
    happy = IntField()
    name = StringField()
    author = StringField()
    link = StringField()
    link_img = StringField()
    user_id = ReferenceField(User)
class Film(Document):
    happy = IntField()
    name = StringField()
    director = StringField()
    link = StringField()
    link_img = StringField()
    user_id = ReferenceField(User)
class Place(Document):
    happy = IntField()
    name = StringField()
    describe = StringField()
    link = StringField()
    user_id = ReferenceField(User)
