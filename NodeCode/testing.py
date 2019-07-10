import numpy as np
import pandas as pd
import socket

import SVM

"""
Used for testing the svm on a single machine.
"""

nodeIP = socket.gethostbyname_ex(socket.gethostname())[2]

n = 0 #info.N[nodeIP]#node number
Num = 1 #len(info.N) # total number of nodes
d = 20#info.d # number data points/node
tau = 5
# these can be pulled from the agg if desired 
weight = 1
eta = .01
lam = 1
k = 1
# pull data_pts for global update
#w = info.w
w = np.zeros(784)
D = d*Num 

filepath = r"train.csv"
data_pts = pd.read_csv(filepath, skiprows=(Num*k*D), nrows=(D)).values

# SVM
w,fn = SVM.svm(w,data_pts,eta,lam,tau,d,weight)

print(len(w), fn)
#print(w)