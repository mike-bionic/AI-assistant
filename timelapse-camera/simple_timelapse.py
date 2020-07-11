import time
nframes = 1024
interval = 5
for i in range(nframes):
    # capture
    ret, img = cap.read()
    # save file
    cv2.imwrite('./img_'+str(i).zfill(4)+'.png', img)
    # wait 5 seconds
    time.sleep(interval)
