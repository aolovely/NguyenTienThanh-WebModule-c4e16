from models.service import Service
import mlab
mlab.connect()

idToFind = '5ac08d0ddb80b234d01c6bfe'

object = Service.objects.get(id=idToFind)
print(object["name"])

#delete delete the records
id ="5ac0910ddb80b229705f1592"
object1 = Service.objects.get(id=id).delete()
