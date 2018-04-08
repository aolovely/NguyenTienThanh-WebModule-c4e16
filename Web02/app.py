from flask import Flask, render_template, redirect, url_for
from flask import*
from mongoengine import *
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

@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template("admin.html", services=services)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_delete = Service.objects.with_id(service_id)
    if service_delete is None:
        return "not found"
    else:
        service_delete.delete()
        return redirect(url_for('admin'), code=302)
            #return "Delete "

@app.route('/new-service', methods=["GET", "POST"])
def create():
    if  request.method == "GET":
        return render_template("new-service.html")
    elif request.method == "POST":
        form = request.form
        # name = form["name"]
        # yob = form["yob"]
        # address = form["address"]
        new_service = Service(name = form["name"],
                              yob = form["yob"],
                              gender = form["gender"],
                              height = form["height"],
                              phone = form["phone"],
                              address = form["address"],
                              image = form["image"],
                              description = form["description"],
                              measurements = [form["measurements1"], form["measurements2"], form["measurements3"]],
                              status = bool(form["status"]))
        new_service.save()

        return redirect(url_for('admin'))
#exercise1
@app.route('/delete-all')
def deleteAll():
    Service.objects.delete()
    return redirect(url_for('admin'), code=302)

@app.route('/services')
def services():
    allservices = Service.objects()
    return render_template("allservices.html", allservices=allservices)

#exercise3
@app.route('/detail/<service_id>')
def detail(service_id):
    service_item= Service.objects.with_id(service_id)
    return render_template("detail.html", service_item=service_item)

#exercise6
@app.route('/update-service/<service_id>', methods=["GET", "POST"])
def update(service_id):
    service_update = Service.objects.with_id(service_id)
    if service_update is None:
        return "not found"
    else:
        if  request.method == "GET":
            return render_template("update-service.html", service_update=service_update)
        elif request.method == "POST":
            form = request.form
            service_update.update(set__name = form["name"],
                                  set__yob = form["yob"],
                                  set__gender = form["gender"],
                                  set__height = form["height"],
                                  set__phone = form["phone"],
                                  set__address = form["address"],
                                  set__image = form["image"],
                                  set__description = form["description"],
                                  set__measurements = [form["measurements1"], form["measurements2"], form["measurements3"]],
                                  set__status = bool(form["status"])
                                  )
            service_update.reload()
            return redirect(url_for('admin'))

if __name__ == '__main__':
  app.run(debug=True)
