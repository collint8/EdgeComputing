# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:08:14 2019

@author: hokis
"""
import numpy as np
import Read
import Shuffle

### SVM Gradient Descent. Takes training vectors x and lables y to perform T iterations. 
### lambda and eta adjust the rate of convergence.
### Outputs SVM vector w. And vector of loss functions fn for convergence analysis

def svm(w,data_pts,eta,lam,tau,d,weight,shuff=0,N=1):#,result,index): #,tau):
    n = len(w)
    fn = np.zeros(tau) # array of calculated loss functions for each local iteration (tau)

    for t in range(0, int(tau)):
        if shuff==1:
            np.random.shuffle(data_pts)
        elif shuff==2:
            data_pts = Shuffle.rRobin(data_pts,N=N)
        elif shuff==3:
            data_pts = Shuffle.segShift(data_pts,N=N)
        x, y = Read.Read(d, data_pts, weight) # weight modifies yread
        wT = w.transpose()
        dfn = np.zeros(n)
        for j in range(0 , d):           
            if (1-y[j]*np.dot(wT, x[j]))<0:
                max = 0
            else:
                max = 1-y[j]*np.dot(wT, x[j])                
                        
            for i in range(0,n):
                dfn[i] += (lam*w[i]-(y[j]*x[j,i])*max)/d
      
            fn[t] += ((lam/2)*np.dot(w, wT)**2 + (max**2)/2)/d
            
        
        w = w - eta*dfn


    return w,fn




