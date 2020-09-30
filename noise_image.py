import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

'''def noisy(noise_typ,image):
   if noise_typ == "gauss":
      row,col,ch= image.shape
      mean = 0
      var = 0.1
      sigma = var**0.5
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss
      return noisy
   elif noise_typ == "s&p":
      row,col,ch = image.shape
      s_vs_p = 0.5
      amount = 0.004
      out = np.copy(image)
      # Salt mode
      num_salt = np.ceil(amount * image.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape
      out[coords] = 1

      # Pepper mode
      num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
      out[coords] = 0
      return out
   else noise_typ == "poisson":
      vals = len(np.unique(image))
      vals = 2 ** np.ceil(np.log2(vals))
      noisy = np.random.poisson(image * vals) / float(vals)
      return noisy
   else noise_typ =="speckle":
      row,col,ch = image.shape
      gauss = np.random.randn(row,col,ch)
      gauss = gauss.reshape(row,col,ch)        
      noisy = image + image * gauss
      return noisy
  
image=cv2.imread("flower.jpg")
plt.imshow(image)
plt.show()'''

image = mpimg.imread('flower.jpg')
plt.imshow(image)
row,col,ch = image.shape
gauss = np.random.randn(row,col,ch)
gauss = gauss.reshape(row,col,ch)        
noisy = image + image * gauss

out_image = noisy("gauss", image)
plt.imshow(out_image)

out_image = noisy("speckle", image)
plt.imshow(out_image)

out_image = noisy("poisson", image)
plt.imshow(out_image)

out_image = noisy("s&p", image)
plt.imshow(out_image)

gray = cv2.cvtColor(out_image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
pixel = image[10,10]
print(pixel)

blue=image[:,:,0]
print(blue)


from PIL import Image
pix_value = list(out_image.getdata())

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()












