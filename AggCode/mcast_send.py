# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 09:59:11 2019

@author: hokis
"""


import socket
import types
import pickle
import numpy as np

def send(data):
 
    MCAST_GRP = '224.3.29.71'
    MCAST_PORT = 5007
    
    data = data # data has properties .w .nodenum .tau .k
    datasend = pickle.dumps(data) 
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 20)
    sock.sendto(datasend, (MCAST_GRP, MCAST_PORT))



#use:
#w = np.zeros(784)
w = np.ones(784)
tau = 2
#w,fn = NodeSvm.NodeSVM(w,N)
data = types.SimpleNamespace(w=w,tau=tau) 
send(data)


#source: https://stackoverflow.com/questions/603852/how-do-you-udp-multicast-in-python


