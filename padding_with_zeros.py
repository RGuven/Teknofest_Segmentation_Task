# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 22:09:55 2021

@author: ramazan.guven
"""


import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

IMAGE_PATH = "./roi_images/"
target_size = 512  # 512x512

DEST_PATH = "./roi_images_padding_zeros/"

i=0
for image in os.listdir(IMAGE_PATH):
    
   
    file_name   = image.split(".")[0]
    img = Image.open(IMAGE_PATH + file_name + '.jpg')
    width, height = img.size
    
    if width < 512  or height < 512:
        
        left_side = int((target_size - width) / 2)
        top_side = int((target_size - height) / 2)
        result = Image.new(img.mode, (target_size, target_size), (0,0,0))
        result.paste(img, (left_side, top_side))
        """
        saving way not tested
        result.save("{}{}.jpg".format(DEST_PATH,file_name))
        """
        #print('Image Size', np.asarray(img).shape)
        #print('Image Size', np.asarray(result).shape)
        
        #plt.imshow(img)
        #plt.show()
        #plt.imshow(result)
        #plt.show()
        
    else:
        
        print(file_name)
        img = img.resize((512,512))

            
            
        
        
    
    
    
    
    
    