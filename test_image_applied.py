# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 18:34:32 2021

@author: ramazan.guven
"""

import matplotlib.pyplot as plt
from PIL import Image
import os
import pandas as pd
import numpy as np

IMAGE_PATH = './roi_images/'
MASK_PATH  = './roi_maskes/'



for image in os.listdir(IMAGE_PATH):
    file_name   = image.split(".")[0]
    print(file_name)
    img = Image.open(IMAGE_PATH + file_name + '.jpg')
    mask = Image.open(MASK_PATH + file_name + '.png')
    print('Image Size', np.asarray(img).shape)
    print('Mask Size', np.asarray(mask).shape)
    
    
    plt.imshow(img)
    plt.imshow(mask, alpha=0.6)
    plt.title('Picture with Mask Appplied')
    plt.show()