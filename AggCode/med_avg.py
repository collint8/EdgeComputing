# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 09:04:45 2019

@author: hokis
"""
import statistics as stats
import numpy as np

"""
These are the various forms of processing the models from the nodes. Mean 
performs a simple average
median is also self explanitory
med_avg takes the average after eliminating some outlying values
"""
def med_avg(win): #, len_w):   <=optional
    
    w = win
    N, n = np.shape(w)

    ww = np.zeros(n) 
    for i in range (0,n): # iterate through length of w vector
        vals = w[:,i]
        # remove hig and low values
        vals = np.delete(vals, [np.argmax(vals),np.argmin(vals)])         
        val = np.sum(vals) # average value at position i; +1 for aggregator
        ww[i] = val/(N-2) # averaged w vector   
#        print('w_avg = ', ww)
        

    return ww
	
def med(win):
	w = win
	N, l = np.shape(w)
	
	ww = np.zeros(l)
	for i in range(0,l):
		ww[i] = stats.median(w[:,i])
	return ww
	
def mean(win):
	w = win
	N, l = np.shape(w)
	ww = np.zeros(l)
	for i in range(0,l):
		ww[i] = stats.mean(w[:,i])
	return ww
	