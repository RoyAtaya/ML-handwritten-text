import numpy as np
from PIL import Image as imag
from pathlib import Path

# get path of the images
# input: the relative path of the images
# return: the path of the images
def getPath(relative_path):
  PathList = Path(relative_path).glob('**/*.jpg')
  path_in_str = np.array([])
  for path in PathList:
      path_in_str = np.append(path_in_str, str(path))
  return path_in_str

# split the image into useable chunks
# input: list of images in the images directory
def imageSplit(dirList):
  imageArr = []
  i = 0
  for item in dirList:
    imgData = np.array(imag.open(item))
    imageArr.append([imgData, item])
    i+=1
  print(imageArr)

if __name__== "__main__":
  dirList = getPath("images/")
  print(dirList)
  imageSplit(dirList)