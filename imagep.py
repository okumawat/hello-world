import cv2
import numpy as np
imageFile = input("Enter Image file name:")

def showImage(imageFile):
    img = cv2.imread(imageFile,0)
    cv2.imshow('flower',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


