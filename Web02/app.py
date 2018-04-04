from flask import Flask, render_template
from mongoengine import Document, StringField, IntField, BooleanField
import mlab
from models.service import Service
app = Flask(__name__)
mlab.connect()
#creat collection
#design database
# class Service(Document):
#     name = StringField()
#     yob = IntField()
#     gender = IntField() #0 : female
#     height = IntField()
#     phone = StringField()
#     address = StringField()
#     status = BooleanField()
#creat a document
# new_service = Service(name="linh ka",
#                       yob= 1997,
#                       gender=0,
#                       height=152,
#                       phone="00983456",
#                       address="hanoi",
#                       status =True
# )
# new_service.save()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    all_services = Service.objects(gender=gender, yob__lte=1998, address__contains="ha noi")

    kieuAnh = all_services[0]
    return render_template("search.html", all_services=all_services)

if __name__ == '__main__':
  app.run(debug=True)
