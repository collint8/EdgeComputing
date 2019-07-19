# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 09:59:11 2019

@author: hokis
"""


import socket
import types
import pickle
import numpy as np
#import pandas as pd

use = False 
use = True
# cannot send more than 65k bytes at a time (at least to pis)
def send(data):
    print("sending")
    MCAST_GRP = '225.1.1.1'
    MCAST_PORT = 5007
    
    data = data # data has properties .w .nodenum .tau .k
    datasend = pickle.dumps(data) 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
    
    sock.sendto(datasend, (MCAST_GRP, MCAST_PORT))
    print("sent")


if use == True:
    #use:
    K = 1
    N = 1
    d = 10   
    w = "array of values"
    #w = np.ones(784)
    #filepath = r"train.csv"
    #data_pts = pd.read_csv(filepath, skiprows=0, nrows=(d*N)).values
    #w,fn = NodeSvm.NodeSVM(w,N)
    data = types.SimpleNamespace(w=w)#,data_pts=data_pts) 
    print("message is %s"%data.w)
    send(data)
    #send(d)

#source: https://stackoverflow.com/questions/603852/how-do-you-udp-multicast-in-python


