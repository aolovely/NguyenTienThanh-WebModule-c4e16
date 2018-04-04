import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds235239.mlab.com:35239/warm_winter

host = "ds235239.mlab.com"
port = 35239
db_name = "warm_winter"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
