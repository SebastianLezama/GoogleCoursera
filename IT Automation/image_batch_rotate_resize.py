from PIL import Image
import os

source_path = 'C:\\Users\\Sebastian Lezama\\Pictures\\'
dest_path = 'C:\\Users\\Sebastian Lezama\\Pictures\\Saved Pictures\\'
size = (640,480)
rotation = -90
im_format = '.PNG'

def imRotateResizeJpg(source, dest, size, rotation, format): # Rotates and resizes as PNG
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
                        im.resize(size).rotate(rotation).save(out_file)
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


def main():
    imRotateResizeJpg(source_path, dest_path, size, rotation, im_format)


if __name__ == '__main__':
    main()
