import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

# get path of the images
# input: the relative path of the images
# return: the path of the images
def getPath(relative_path):
    PathList = Path(relative_path).glob('**/*.jpg')
    path_in_str = np.array([])
    for path in PathList:
        path_in_str = np.append(path_in_str, str(path))
    return path_in_str

def showImage(dirList):
    for item in dirList:
        image = plt.imread(item)
        plt.imshow(image)
        plt.show()
        x = input('x coord of img to save: ')
        y = input('y coord of img to save: ')
        saveImage(x,y)


def saveImage(x, y):
    img = resize(im, (x,y), mode = 'reflect')
    roi = cv2.selectROI(img)
    print(roi)

if __name__== "__main__":
  dirList = getPath("images/")
  showImage(dirList)