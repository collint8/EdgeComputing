# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 13:13:17 2019

@author: hokis
"""
import numpy as np
import pandas as pd
import socket
import queue
import types
import SVM
import Read
import node_client
import node_server
'''
	Main for the nodes. Starts and waits for data from agg. once received it unpacks data and runs the svm.
	It then sends the w vector and loss functions back to the agg.
'''

def run():
    while True:

        # node detection: determine IP address
        #nodeIP = socket.gethostbyname_ex("raspberrypi.local")#[-1]
	'''Currently unable to detect own ip do to identical names. Must be changed for each node'''
        nodeIP = '192.168.0.106' 
        print(nodeIP)
        # listen for info from aggregator.
        # determine node number (n) and total number of nodes (Num) from agg Xmission
        # N is list of node
        # win,tau,k,d,N,aggIP = node_server.server(node_ip)
        info = node_server.server(nodeIP) 
        
        n = info.node_dict[nodeIP] #node number
        Num = len(info.node_dict) # total number of nodes
        d = info.d # number data points/node
        tau = info.tau # number of local iterations
        k = info.k # global iteration number
        host = info.host # aggregator IP
        shuff = info.shuff # Shuffling type: 0=none,1=random,2=roundrobin,3=segShift
        
        # these can be pulled from the agg if desired 
        weight = 1
        eta = .01
        lam = 1
        
        # pull data_pts for global update
		# 	Currently pulling the entire dataset for each node but using a part. 
        w = info.w
        D = d*Num# Total data points 
        filepath = r"train.csv"
        data_pts = pd.read_csv(filepath, skiprows=(k*D), nrows=(D)).values

        # SVM
        w,fn = SVM.svm(w,data_pts,eta,lam,tau,d,weight,shuff=shuff,N=Num, n=n)
            
        # send w to agg
        node_client.client(w,fn,host)
        
run()
