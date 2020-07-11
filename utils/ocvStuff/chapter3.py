import cv2
import numpy as np

img = cv2.imread('images/prod-1.jpg')
print(img.shape)

imgResize = cv2.resize(img,(300,300))

imgCropped = img[100:250,150:300]

cv2.imshow("Image",img)
cv2.imshow("resized",imgResize)
cv2.imshow("cropped",imgCropped)
cv2.waitKey(0)