# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 22:09:55 2021

@author: ramazan.guven
"""


import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt



target_size = 512  # 512x512


def padding_zeros(IMAGE_PATH,DEST_IMAGE_PATH,is_mask):
    i=0
    if is_mask:
        file_extention = ".png"
    else:
        file_extention = ".jpg"

    
    for image in os.listdir(IMAGE_PATH):
        
        file_name   = image.split(".")[0]
        img = Image.open(IMAGE_PATH + file_name + file_extention)
        width, height = img.size
        
        if width < 512  or height < 512:
            
            left_side = int((target_size - width) / 2)
            top_side = int((target_size - height) / 2)
            print(img.mode)
            
            if is_mask:
                #THIS FOR PNG IMAGE IN PILLOW :)
                
                result = Image.new(img.mode, (target_size, target_size), (0))
            else:
                result = Image.new(img.mode, (target_size, target_size), (0,0,0))
                
            result.paste(img, (left_side, top_side))
    
            result.save("{}{}{}".format(DEST_IMAGE_PATH,file_name,file_extention))
     
            #print('Image Size', np.asarray(img).shape)
            #print('Image Size', np.asarray(result).shape)
            
            #plt.imshow(img)
            #plt.show()
            #plt.imshow(result)
            #plt.show()
        else:
            
            print(file_name)
            img = img.resize((512,512))
            img.save("{}{}{}".format(DEST_IMAGE_PATH,file_name,file_extention))
    
                
                
            
#this for images padding

padding_zeros(IMAGE_PATH = "./roi_images/",
              DEST_IMAGE_PATH = "./roi_images_padding_zeros/",
              is_mask=False
             )       
    
    
    
#this for maskes

padding_zeros(IMAGE_PATH = "./roi_maskes/",
              DEST_IMAGE_PATH = "./roi_maskes_padding_zeros/",
              is_mask=True
             )       
     
    
    