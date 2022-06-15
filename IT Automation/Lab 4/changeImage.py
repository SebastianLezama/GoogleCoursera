# .tiff to jpeg
from PIL import Image
import os

source_path = 'C:\\Users\\Sebastian Lezama\\Pictures\\'
dest_path = 'C:\\Users\\Sebastian Lezama\\Pictures\\Saved Pictures\\'
size = (600,400)
im_format = '.jpeg'

def imResizeJpg(source, dest, size, format):
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


imResizeJpg(source_path, dest_path, size, im_format)
