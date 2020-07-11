import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)
# # place in matrix on special location
# img[200:300,100:300]=255,0,0

# # line(imgage,statringPont,ending point,color,thickness)
# cv2.line(img,(0,0),(300,300),(0,255,0),3)

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# user cv2.FILLED to fill
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
# CIRCLE(image,center,radius,color,thickness)
cv2.circle(img,(400,50),30,(255,255,0),5)

cv2.imshow("image",img)

cv2.waitKey(0)