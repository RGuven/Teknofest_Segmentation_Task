import numpy as np
from PIL import Image
import cv2
import os
import time
import mask_to_1_channel

"""
app.hasty - 1 İskemik
            2 Hemorojik labelled

"""

def focus_actual_image(image):
    
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
    
    # Find contour and sort by contour area
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    
    # Find bounding box and extract ROI
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        ROI = image[y:y+h, x:x+w]
        break
    
    return ROI,x,y,w,h





MASK_PATH="./maskes/"


for folder_name in os.listdir("./images"):
    
    if folder_name == "INMEYOK":
        print("INMEYOK png images creating ..... wait")
        mask_to_1_channel.inme_yok_png_creator()
    elif folder_name =="ISKEMI":
        print("ISKEMI png images converting ..... wait")
        mask_to_1_channel.iskemi_converter_1_ch()
    elif folder_name == "KANAMA":
        print("KANAMA png images converting ..... wait")
        mask_to_1_channel.kanama_converter_1_ch()
        
        
    print("Ohh, Here we going to thresholding and catting cutting for {}".format(folder_name))
    
    IMG_PATH ="./images/{}/PNG".format(folder_name)
    MASK_PATH ="./images/{}/ONE_CH_MASK".format(folder_name)
    
    i=0
    
    for image in os.listdir(IMG_PATH):
        file_name   = image.split(".")[0]
        ROI,x,y,w,h = focus_actual_image(IMG_PATH+"/{}".format(image))
        cv2.imwrite("./roi_images/{}.jpg".format(file_name),ROI)
        
        try:
            mask = np.asarray(Image.open(MASK_PATH+"/{}.png".format(file_name)))
            
            roi_mask= mask[y:y+h, x:x+w]
            print(roi_mask.shape)
            roi_mask = Image.fromarray(roi_mask)
            print(type(roi_mask))
            roi_mask.save("./roi_maskes/{}.png".format(file_name))
        except :
            print("bir hata oluştu")
        
        i+=1
        if i%400 ==0 :
            time.sleep(3)










     
#############################################################
"""
img = Image.open(IMG_PATH + "10003" + '.png')
mask = Image.open(MASK_PATH + "10003" + '.png')
print('Image Size', np.asarray(img).shape)
print('Mask Size', np.asarray(mask).shape)


plt.imshow(img)
plt.imshow(mask, alpha=0.6)
plt.title('Picture with Mask Appplied')
plt.show()

img = Image.open("./roi_images/" + "10003" + '.jpg')
mask = Image.open("./roi_maskes/"  + "10003" + '.png')
print('Image Size', np.asarray(img).shape)
print('Mask Size', np.asarray(mask).shape)


plt.imshow(img)
plt.imshow(mask, alpha=0.6)
plt.title('Picture with Mask Appplied ROI')
plt.show()


"""

#############################################################

    
    
    
    
    