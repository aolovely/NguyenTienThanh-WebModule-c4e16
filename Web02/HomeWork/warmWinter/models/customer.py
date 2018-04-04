from mongoengine import*
import mlab

mlab.connect()

class Customer(Document):
     name = StringField()
     gender = IntField() #0 : female
     email = StringField()
     phone = StringField()
     job = StringField()
     company = StringField()
     contacted = BooleanField()
