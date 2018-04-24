from models.user import User
import mlab
mlab.connect()
new_user = User(fullname = "hi love",
email = "lolhyvl@gmail.com",
username = "admin",
password = "admin",)
new_user.save()
