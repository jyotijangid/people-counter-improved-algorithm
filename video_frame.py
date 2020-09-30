# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 12:59:11 2020

@author: Lenovo
"""

import cv2
vidcap = cv2.VideoCapture(r"C:\Users\Lenovo\Desktop\ML CETPA\data\example_02.mp4")
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 5 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

