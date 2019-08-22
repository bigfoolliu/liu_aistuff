import json
from copy import deepcopy

from bson.objectid import ObjectId


class MongoBase():
    def __init__(self, data):
        self.data = None

class Worker(MongoBase):

    def __init__(self, data):
        self.data = deepcopy(data)


def mongo_id_to_str(mgo_obj):
    """
        Transforms _id from mongo to what client accepts.
    """
    new_obj = deepcopy(mgo_obj)
    i = new_obj.pop("_id", None)
    if i:
        new_obj["_id"] = str(i)
    return new_obj


def translate(data):
    if isinstance(data, list):
        res = []
        for i in data:
            res.append(translate(i))
        return res
    elif isinstance(data, dict):
        res = {}
        for i, v in data.items():
            res[i] = translate(v)
        return res
    elif isinstance(data, MongoBase):
        return mongo_id_to_str(data.data)
    elif isinstance(data, ObjectId):
        print("oj data: ", data, type(data))
        return str(data)
    else:
        return data


if __name__ == "__main__":
    worker = Worker({
        "_id": ObjectId("fffffffffffffffffffffffe"),
        "name": {
            "type": 1,
            "a": "c"
        },
        "organization_id": ObjectId("ffffffffffffffffffffffff"),
    })
    print("worker: ", worker, type(worker))
    ret = translate(worker)
    json_worker = json.dumps(ret, sort_keys=True, separators=(',', ': '))
    print("json_worker：", json_worker, type(json_worker))
