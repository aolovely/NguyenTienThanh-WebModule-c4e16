from mongoengine import*

class User(Document):
    fullname = StringField()
    email = EmailField()
    username = StringField()
    password = StringField()
