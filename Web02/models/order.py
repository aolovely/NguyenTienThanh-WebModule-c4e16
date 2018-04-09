from mongoengine import *
from models.user import User
from models.service import Service

class Order(Document):
    service = ReferenceField(Service)
    user = ReferenceField(User)
    time = StringField()
    is_accepted = BooleanField()
