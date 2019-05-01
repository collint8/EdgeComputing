# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:42:06 2019

@author: hokis
"""
import numpy as np
#import pandas as pd

def Read(numPoints, data, weight, offset=0, case=None):
    pointstart = offset
    pointend = pointstart + numPoints
    
    x = np.array(data[pointstart:pointend,1:])/255 # normalized pixel values
    y = np.array(data[pointstart:pointend,0])
    	
    ### adjust y values to 1 or -1
    #	D,_ = np.shape(x)
    for i in range(0, len(y)):		
        #if y[i] == 8: # looking for the digit of interest  
        if  y[i]%2 == 0: # for determining even or odd (mod2)
            y[i] = 1*weight
        else:
            y[i] = -1
    			
    return x,y

#	### Select particular values in case
#	if case!=None:
#		ttab = np.zeros(numPoints, dtype=bool)
#		points = np.size(case)
#		for i in range(0,points):
#			ttab = ttab + (y==case[i])
#		x = x[ttab,]
#		y = y[ttab]



