from flask import Flask, render_template, redirect, url_for
from flask import*
from mongoengine import *
import mlab
from models.service import Service
from models.user import User
from models.order import Order
from datetime import *
from gmail import GMail, Message

app = Flask(__name__)
app.secret_key = "lovely"
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

@app.route('/delete-all')
def deleteAll():
    Service.objects.delete()
    return redirect(url_for('admin'), code=302)

@app.route('/services')
def services():
    allservices = Service.objects()
    return render_template("allservices.html", allservices=allservices)


@app.route('/detail/<service_id>')
def detail(service_id):
    if "logged_in" in session:
        service_item= Service.objects.with_id(service_id)
        return render_template("detail.html", service_item=service_item)
    else:
        session["service_id"] = service_id
        return redirect(url_for('login'))


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

@app.route('/sign-in', methods=["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template("sign_in.html")
    elif request.method == "POST":
        form = request.form
        new_user = User(fullname=form["fullname"],
                        email=form["email"],
                        username=form["username"],
                        password=form["password"])
        new_user.save()
        return "dang ki tai khoan thanh cong"

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        acc = User.objects(username=username, password=password).first()
        if acc is None:
            return render_template("error.html")
        else:
            session["logged_in"] = str(acc["id"]) #luu id-user phuc vu cho exercise3
            return redirect(url_for('detail', service_id=session["service_id"]))

@app.route('/logout')
def logout():
    del session["logged_in"]
    return redirect(url_for('index'))

@app.route('/order/<service_id>')
def order_service (service_id):
    user = User.objects.with_id(session["logged_in"])
    service = Service.objects.with_id(service_id)
    time ='{0:%I:%M %p - %d/%m}'.format(datetime.now())
    new_order = Order(service=service,
                      user=user,
                      time=time,
                      is_accepted=False)
    new_order.save()
    return "da gui yeu cau"

@app.route('/all-order')
def all_order():
    all_order = Order.objects(is_accepted=False)
    return render_template('all_order.html', all_order=all_order)

@app.route('/accept/<order_id>')
def accept(order_id):
    order = Order.objects.with_id(order_id)
    order.update(set__is_accepted=True)
    order.reload()
    mail = order["user"]["email"]
    gmail = GMail("lolhyvl@gmail.com", "khuelovely")
    htmlContent = "yêu cầu của bạn đã được xử lý, chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất. Cảm ơn bạn đã sử dụng dịch vụ của Mùa Đông Không Lạnh"
    msg = Message("Mùa Đông Không Lạnh", to= mail, html= htmlContent)
    gmail.send(msg)
    return redirect(url_for('all_order'))

if __name__ == '__main__':
  app.run(debug=True)
