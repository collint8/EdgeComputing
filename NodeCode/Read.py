# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:42:06 2019

@author: hokis
"""
import numpy as np
#import pandas as pd
'''
	Process the data to work with svm. Labels are changed to 1 if even and -1 if odd
	x vectors are normalized to values between 1 and 0
	data is returned as label vector y and data matrix x.
'''

def Read(numPoints, data, weight, offset=0):
    pointstart = numPoints*offset #numPoints=d=points/node
    pointend = pointstart + numPoints
    
    x = np.array(data[pointstart:pointend,1:])/255 # normalized pixel values
    y = np.array(data[pointstart:pointend,0])
    	
    ### adjust y values to 1 or -1
    for i in range(0, len(y)):		
        if  y[i]%2 == 0: # for determining even or odd (mod2)
            y[i] = 1*weight
        else:
            y[i] = -1
    			
    return x,y




