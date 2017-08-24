#!python
import os,sys
import plistlib
from PIL import Image

scale_param = 0.852
root_save_path = 'c:/scale'

def scale_png(path, file, save_path):
    png_path = path + '/' + file
    big_image = Image.open(png_path)
    img_size = big_image.size
    scale_size = [img_size[0] * scale_param, img_size[1] * scale_param]
    print(scale_param, img_size, scale_size)
    big_image.thumbnail(scale_size, Image.ANTIALIAS)
    big_image.save(save_path + '/' + file)
        
    
def list_file(path, save_path):
    for file in os.listdir(path):
        if os.path.isdir(path + '/' + file):
            save_path = save_path + '/' + file
            if not os.path.exists(save_path) :
                os.mkdir(save_path)
            list_file(path + '/' + file, save_path)
            continue
        file_names = os.path.splitext(file)
        print file_names
        if file_names[1] == '.png' or file_names[1] == '.jpg' :
            scale_png(path, file, save_path )

if __name__ == '__main__':
    path = sys.argv[1]
    root_save_path = sys.argv[2]
    scale_param = float(sys.argv[3])
    if not os.path.exists(root_save_path):
        os.mkdir(root_save_path)

    if os.path.exists(path) :
        list_file( path, root_save_path )
    else :
        print('please input corret path')
