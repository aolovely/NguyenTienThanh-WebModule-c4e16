from mongoengine import*
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() #0 : female
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    image = StringField()
    description = StringField()
    measurements = ListField(IntField())
