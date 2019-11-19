import os
import json
import base64


def image_zip(image_name, save_path):
    try:
        name = image_name[image_name.find('/') + 1:image_name.find('.png')]
        os.system('pngquant --quality=65-80 ' + image_name + ' --output=' + save_path + name + '.png')
        # with open(save_path + name + '.png', 'rb')as f:
        #     image_data = base64.b64encode(f.read())
        #     image_data = image_data.decode()
        # os.remove(save_path + name + '.png')
        # os.remove(image_name)
        return {'status': 0, 'save': save_path + name + '.png'}
    except:
        return {'status': 1}


while True:
    for file in os.listdir('temp/'):
        with open("temp/" + file, 'r') as load_f:
            load_dict = json.load(load_f)['name']
            result = image_zip(load_dict, 'save/')
            if result['status'] == 1:
                f = open('finish.txt', 'a')
                f.write(load_dict + ' ' + str(result['save']) + '\n')
                f.close()

        os.remove("temp/" + file, )
