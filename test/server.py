import requests
import json
import base64


def get_data(name):
    with open(name, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
    return s


def data_post(name):
    url =  "http://"":3301/image"
    data = {'img':get_data(name), 'name':name}
    json_mod = json.dumps(data)
    res = requests.post(url=url, data=json_mod.encode("utf-8"), headers ={'Content-Type': 'application/json'})
    return res.text

