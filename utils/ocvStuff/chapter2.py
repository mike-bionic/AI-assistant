import cv2
import numpy as np

img = cv2.imread("images/user8.jpg")

kernel = np.ones((5,5),np.uint8)
# gray blur image
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# canny image?
imgCanny = cv2.Canny(img,150,200)
# dialation makes lines fatter thicer
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
# erosion is opposite to dialation
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("some gray",imgGray)
cv2.imshow("blurryface",imgBlur)
cv2.imshow("canny image",imgCanny)
cv2.imshow("Dialatioin image",imgDialation)
cv2.imshow("imgEroded image",imgEroded)
cv2.waitKey(0)