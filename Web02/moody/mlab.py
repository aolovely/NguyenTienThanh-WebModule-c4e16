import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds249415.mlab.com:49415/moody-app

host = "ds249415.mlab.com"
port = 49415
db_name = "moody-app"
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
