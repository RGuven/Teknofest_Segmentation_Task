# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 16:40:17 2021

@author: ramazan.guven
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import time

def inme_yok_png_creator():
    
    
    INMEYOK="./images/INMEYOK/"
    
    i=0
    for image in os.listdir(INMEYOK+'PNG'):
        file_name   = image.split(".")[0]
        
        inme_yok = Image.open(INMEYOK+'PNG/{}'.format(image))
        #print('Mask Size', np.asarray(inme_yok).shape)
        width,height,_ = np.asarray(inme_yok).shape
        
        img_zeros = np.zeros((width,height),dtype=np.uint8)
        new_image = Image.fromarray(img_zeros)
        new_image.save(INMEYOK+'ONE_CH_MASK/{}'.format(file_name+".png" ))
        
        i+=1
        if i%400==0:
            time.sleep(5)
        
        #quick control
        """
        mask = Image.open(INMEYOK+'ONE_CH_MASK/{}'.format(file_name+".png" ))
        print('Mask Size', np.asarray(mask).shape)
    """
    
##########################################################################


def iskemi_converter_1_ch():
        
    ISKEMI="./images/ISKEMI/"
    
    i=0
    for image in os.listdir(ISKEMI+'MASK'):
        file_name   = image.split(".")[0]
        iskemi = Image.open(ISKEMI+'MASK/{}'.format(image))
        #print('Mask Size', np.asarray(iskemi).shape)
        red, green, blue = iskemi.split()
        blue_image= np.asarray(blue)
    
    
        new_mask= np.zeros((512,512),dtype=np.uint8)
        for y in range(0,512):
            for x in range(0,512):
                if blue_image[y, x] == 255:
                    new_mask[y, x]= 1
                else:
                    new_mask[y, x]= 0
                    
        new_mask = Image.fromarray(new_mask)
        new_mask.save(ISKEMI+'ONE_CH_MASK/{}'.format(file_name+".png" ))   
        
        i+=1
        if i%400==0:
            time.sleep(5)
    
##########################################################################
    
    
def kanama_converter_1_ch():     
    KANAMA="./images/KANAMA/"
    
    i=0
    for image in os.listdir(KANAMA+'MASK'):
        file_name   = image.split(".")[0]
        kanama = Image.open(KANAMA+'MASK/{}'.format(image))
        #print('Mask Size', np.asarray(iskemi).shape)
        red, green, blue = kanama.split()
        green_image= np.asarray(green)
    
    
        new_mask= np.zeros((512,512),dtype=np.uint8)
        for y in range(0,512):
            for x in range(0,512):
                if green_image[y, x] == 255:
                    new_mask[y, x]= 2
                else:
                    new_mask[y, x]= 0
                    
        new_mask = Image.fromarray(new_mask)
        new_mask.save(KANAMA+'ONE_CH_MASK/{}'.format(file_name+".png" ))   
        
        """
        plt.imshow(kanama)
        plt.show()
        
        plt.imshow(new_mask)
        plt.show()
        """
        
        i+=1
        if i%400==0:
            time.sleep(5)  



