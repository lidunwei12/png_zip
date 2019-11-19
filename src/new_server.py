from http_api_exporter import ApiHttpServer
import base64
import json


def upload_data(img, name):
    try:
        img_data = base64.b64decode(img)
        with open('../image/' + name, 'wb') as f:
            f.write(img_data)
        with open("../temp/+"+name+".json", 'r') as load_f:
            json.dump({'name':'../image/' + name},load_f)
        return {'status': 0}
    except:
        return {'status': 1}


def main():
    app = ApiHttpServer()
    app.bind("/image", upload_data)
    app.start(3301)


main()
