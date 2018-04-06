from models.service import Service
import mlab
mlab.connect()
#all_service = Service.objects()

#print(all_service[0]["name"])
#print(all_service[1].name)

id_to_find = "5ac08c25db80b21a783f6d94"
#love = Service.objects(id=id_to_find)[0]
#print(love["name"])
#print(love.to_mongo())
love1 = Service.objects.with_id(id_to_find)
if love1 is None:
    print("Service not found")
else:
    print("delete love1")
    love1.update(set__yob=1995)
    love1.reload()
    #love1.delete()
    print(love1.yob)

#object = Service.objects.get(id=id_to_find)
#print(object.name)
