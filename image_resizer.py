import os
import imghdr
import PIL
from PIL import Image

def resizeImages (dir_name, width):
    """Resize the images in a folder.

       Arguments:
       dir_name -- the path of the folder
       width -- width that the images should be resized to
       Returns:
       countFiles -- the number of files resized
    """
    countFiles = 0
    files = os.listdir(dir_name)
    #Add separator if missing from end of folder path
    if not dir_name.endswith(os.sep):
        dir_name = dir_name + os.sep
    #Filter out files which are not recognised image types
    files = [f for f in files if imghdr.what(dir_name + f) > 0]
    #Resize all the image files in the folder
    for filename in files:
             img = Image.open(dir_name + filename)
             ratio = float(img.size[1])/float(img.size[0])
             img = img.resize((width,int(width*ratio)),PIL.Image.ANTIALIAS)
             img.save(dir_name + filename)
             countFiles = countFiles + 1
    return countFiles

if __name__ == "__main__":
    import sys
    _, dir_name,w = sys.argv
    resizeImages(dir_name,int(w))
