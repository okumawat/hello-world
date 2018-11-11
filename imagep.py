import cv2
import numpy as np
def showImage(imageFile):
    img = cv2.imread(imageFile,0)
    cv2.imshow('flower',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    imageFile = input("Enter Image file name:")
    showImage(imageFile)

