import os
import cv2
import base64
def image_zip(image_name,save_path):
    name = image_name[image_name.find('/')+1:image_name.find('.png')]
    os.system('pngquant --quality=65-80 '+image_name+' --output='+save_path+name+'.png')
    with open(save_path+name+'.png','rb')as f:
	   image_data = base64.b64encode(f.read())
	   image_data = image_data.decode()
   os.remove(save_path+name+'.png')
   os.remove(image_name)
   return {'image_data':image_data}
image_zip('image/20190930124444.png','temp/')

	
