# .tiff to jpeg
from PIL import Image
import os


source_path = "supplier-data/images/"
dest_path = "supplier-data/images/"
size = (600,400)
im_format = '.jpeg'


def image_convert_resize_to_jpg(source, dest, size, format):
    path = os.getcwd() + source
    for i in os.listdir(path):
        out_file = str(os.path.splitext(i)[0] + format)
        if not os.path.isdir(i):
            if i != out_file:
                try:
                    print("\nFilename: " + i)
                    with Image.open(path + i) as im:
                        if im.mode != 'RGB':
                            im.resize(size).convert('RGB').save(dest + out_file)
                        else:
                            im.resize(size).save(dest + out_file)
                        print("Saved as: " + dest + out_file)
                        print('-' * 50)
                except OSError:
                    print("Couldn't save file: " + out_file)
                    print('-' * 30)
            else:
                print(out_file + " already formated")
                print('-' * 30)
        else:
            continue

if __name__ == '__main__':
    image_convert_resize_to_jpg(source_path, dest_path, size, im_format)
