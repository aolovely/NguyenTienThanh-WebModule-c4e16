import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds049848.mlab.com:49848/muadongkhonglanh1

host = "ds049848.mlab.com"
port = 49848
db_name = "muadongkhonglanh1"
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
