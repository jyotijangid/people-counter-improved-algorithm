from PIL import Image
import math
path = r"C:\Users\Lenovo\Desktop\Datasets for ML\image7.jfif" # Your image path
img = Image.open(path)
members = [(0,0)] * 9
width,height = img.size

newimg = Image.new("RGB",(width,height),"white")
for i in range(1,width-1):
    for j in range(1,height-1):
        members[0] = img.getpixel((i-1,j-1))
        members[1] = img.getpixel((i-1,j))
        members[2] = img.getpixel((i-1,j+1))
        members[3] = img.getpixel((i,j-1))
        # Center Pixel
        members[4] = img.getpixel((i,j))
        members[5] = img.getpixel((i,j+1))
        members[6] = img.getpixel((i+1,j-1))
        members[7] = img.getpixel((i+1,j))
        members[8] = img.getpixel((i+1,j+1))
        new = [list(u) for u in members]
        #print('mem ',new)
        res = [0,0,0]
        for z in new:
            res = list(map(sum,zip(res,z)))  
        #print('res ',res)
        local_mean = [t*(1/9) for t in res]
        #print('mean ',local_mean)
       
        val = [[(a_i - b_i)*(a_i - b_i) for a_i, b_i in zip(local_mean, x)]for x in new]
        #print(val)
       
        pixel_sum = [0,0,0]
        for r in val:
            pixel_sum = list(map(sum,zip(pixel_sum,r)))
        pixel_distance = [k*(1/9) for k in pixel_sum]
        new_pixel = [round(math.sqrt(y)) for y in pixel_distance]
        newimg.putpixel((i,j),(tuple(new_pixel)))
        predicted=[]
        predicted.append(new_pixel)
        #print(new_pixel)
img.show()
newimg.show()



