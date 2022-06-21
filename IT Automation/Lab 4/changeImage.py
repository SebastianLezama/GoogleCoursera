# .tiff to jpeg
from PIL import Image
import os

source_path = '~/supplier-data/images'
dest_path = '~/supplier-data/images'
size = (600,400)
im_format = '.jpeg'

def image_convert_resize_to_jpg(source, dest, size, format):
    for i in os.listdir(source):
        out_file = str(os.path.splitext(i)[0] + format)
        os.chdir(source)
        if not os.path.isdir(i):
            if i != out_file:
                try:
                    print("Filename: " + i)
                    with Image.open(source + i) as im:
                        if im.mode != 'RGB':
                            im.convert('RGB')
                        os.chdir(dest)
                        im.resize(size).save(out_file)
                        print("Saved as: " + dest + out_file)
                        print('-' * 50)
                except OSError:
                    print("Couldn't save file")
                    print('-' * 30)
            else:
                print("File already formated")
                print('-' * 30)
        else:
            continue


if __name__ == '__main__':
    image_convert_resize_to_jpg(source_path, dest_path, size, im_format)
