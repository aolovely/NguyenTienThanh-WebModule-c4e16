import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds239009.mlab.com:39009/csmapp

host = "ds239009.mlab.com"
port = 39009
db_name = "csmapp"
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
