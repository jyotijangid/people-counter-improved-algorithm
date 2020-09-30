import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os 
import cv2  
from PIL import Image  
#print(os.getcwd())  
  
# Folder which contains all the images 
# from which video is to be generated 
os.chdir(r"C:\Users\Lenovo\Desktop\ML CETPA\data_new")   
path = r"C:\Users\Lenovo\Desktop\ML CETPA\data_new"
  
mean_height = 0
mean_width = 0
  
#num_of_images = len(os.listdir('.')) 
# print(num_of_images) 
  
for file in os.listdir('.'): 
    im = Image.open(os.path.join(path, file)) 
    width, height = im.size 
    mean_width += width 
    mean_height += height 
for file in os.listdir('.'): 
    if file.endswith(".jpg") or file.endswith("png"): 
        # opening image using PIL Image 
        im = Image.open(os.path.join(path, file))  
        ch=3
        # im.size includes the height and width of image 
        width, height = im.size  
        #row,col,ch = im.shape
        gauss = np.random.randn(height,width,ch)
        gauss = gauss.reshape(height,width,ch)
        noisy = im + im * gauss
        #print(width, height) 
        im = noisy
        plt.imshow(im)
        # resizing  
        #imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)  
        #imResize.save( file, 'JPEG', quality = 95) # setting quality 
        # printing each resized image name 
        #print(im.filename.split('\\')[-1], " is resized")  
#def noisy(noise_typ,image):
    #if noise_typ =="speckle":
        
        
                
        
'''        return noisy
count=1
for i in range(1,36):
    image = mpimg.imread("image"+str(count)+".jpg")
    plt.imshow(image)
    count+=1
    #out_image = noisy("speckle", image)
    #plt.imshow(out_image)
