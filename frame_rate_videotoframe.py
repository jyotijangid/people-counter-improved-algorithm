import cv2
import os
vidcap = cv2.VideoCapture(r"C:\Users\Lenovo\Desktop\ML CETPA\data\example_02.mp4")

import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

try: 
      
    # creating a folder named data 
    if not os.path.exists('data_new'): 
        os.makedirs('data_new') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of new data') 
  
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite('./data_new/image'+str(count)+'.jpg', image)
        print("created frame"+str(count))
        # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 2 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

