from models.service import Service
import mlab
from random import randint, choice

mlab.connect()
new_service = Service(name="Hang Nga",
                      yob=1997,
                      gender=0,
                      height=152,
                      phone="0969179767",
                      address="bac Ninh",
                      status =True,
                      image = "../static/image/14523193_1079611532159091_3212195191308021271_n.jpg",
                      description = "ngoan hien, de thuong, thich di du lich ...",
                      measurements = [79, 59, 83]
)
new_service.save()
