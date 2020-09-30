'''import numpy as np
import cv2

cap = cv2.VideoCapture('C:\\Users\\Lenovo\\Desktop\\ML CETPA\\people-counting-opencv\\videos\\example_01.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()'''

# Importing all necessary libraries 
import cv2 
import os 
# Read the video from specified path 

cam = cv2.VideoCapture(r"C:\Users\Lenovo\Desktop\ML CETPA\data\example_02.mp4") 
  
try: 
      
    # creating a folder named data 
    if not os.path.exists('data'): 
        os.makedirs('data') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0
i=0
while(i<300): 
      
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret: 
        # if video is still left continue creating images 
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name) 
  
        # writing the extracted images 
        cv2.imwrite(name, frame) 
  
        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
        i+=1
    else: 
        break
  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows()
