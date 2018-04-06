import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds237409.mlab.com:37409/river

host = "ds237409.mlab.com"
port = 37409
db_name = "river"
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
