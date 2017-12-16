import cv2
import numpy as np 

def nothing(x):
	pass

img = cv2.imread('lena.jpg')

cv2.namedWindow('image')

cv2.createTrackbar('Gamma','image',0,30,nothing)

while(1):
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    gamma = cv2.getTrackbarPos('Gamma','image')
    gamma = gamma/10.0
    img2 = img/255.0
    img2 = cv2.pow(img2,gamma)
    img2 = np.uint8(img2*255.0)

    both = np.hstack((img,img2))
    cv2.imshow('image',both)
    
cv2.destroyAllWindows()