import cv2 #image open cv 
import time #delay 
import imutils #resize

cam=cv2.VideoCapture(0) #cam id
#for laptop put (0) and for webcam put (1 or 2)
time.sleep(1)   #optional

firstFrame=None  #first frame is consider as empty background
area=500

while True:
    _,img = cam.read()  #red frame from camera
    text = "Normal"
    img = imutils.resize(img,width=1000) #resizing the image
    graying = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #convert color to gray scale image
    gaussianImg = cv2.GaussianBlur(graying,(21,21),0) #smoothening the image

    if firstFrame is None:
        firstFrame = gaussianImg   #capturing 1st frame on its 1st iteration
        continue
    imgDiff = cv2.absdiff(firstFrame,gaussianImg) #absolute diff b/w 1st and current image

    threshImg = cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1]  #binary
    threshImg = cv2.dilate(threshImg, None, iterations=2)  #to avoid leftover

    cnts = cv2.findContours(threshImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)   #.copy is used to copy the image
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x,y), (x + w, y + h),(0, 255, 0), 2)
        text = "Moving Object detected"
    print(text)
    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow("camerafeed",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("j"):
        break
cam.release()
cv2.destroyAllWindows()
    
