# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:47:30 2019

@author: hokis
"""

import numpy as np
#import pandas as pd
import types
import AccTest
#import queue
#from threading import Thread
import ParsFile_v2_1 as ParsFile
#from med_avg import med_avg
#import SVM
#import mcast_send
#import MakeFile
import aggr_client_v1_3 as aggr_client
import aggr_server
import nodeDetection
import med_avg
import time
import matplotlib.pyplot as pt
#aggr_server(host,num_con,que)
isImported = False
'''
	The main of the system. It will initialize conditions and detect available nodes and 
	assumes that all devices connected to the router are ready to act as a node.
	Then it will enter a loop to perform K global updates.
		It will send a data packet to each node
		then it will wait to receive from each node. 
		Once it has data from each node it will process the w vectors (based on avc) and store the loss functions
		It also runs an accuracy test to show progress
	Once the loop is finished it plots the functions and returns the w vector, loss functions, and averages
	
'''
def run(K,tau=0,shuff=0,avc=0):
    
    # node detection
    router_ip = '192.168.0.1'
    host,iplist = nodeDetection.run(router_ip)
    node_dict = {} 
	# determine number of nodes
    n = 0
    for ind in iplist:
        node_dict[ind] = n
        n += 1
    N = n
	# initialize data size d, iterations tau, and matrices for w, averages, and loss functions.
    if tau ==0:
        tau =N
    multiplier = 3
    d = multiplier * n # number data points per node This value can be changed as desired.
    w = np.zeros(784)
    fnfn = np.zeros(shape=(N+1,K*tau))
    accs = np.zeros(K)
	
	## Start global updates
    for k in range (0,K): # aggregator as client, k global iterations 
        # send global update information to nodes
        ### Currently using the same dataset throughout. change k=k to refresh data
        data = types.SimpleNamespace(w=w,k=0,host=host,node_dict=node_dict,d=d,tau=tau,shuff=shuff)#data_pts=data_pts) #data on nodes
		
        # Send Data
        #mcast_send.send(data) # alternative to sending to nodes one at a time.
        for i in range(0,N): ## Send to each node
            aggr_client.client(iplist[i],data)
        
        # aggregator as server; get ws from nodes 
        result  = aggr_server.aggr_server(host,N)
        ww = result.w
        for i in range(0,N):
            fnfn[i,k*tau:(k+1)*tau] = result.fn[i*tau:i*tau+tau]
		# Process the w 
        w = ww
        if avc==1:
            w = med_avg.med(ww)
        elif avc==2:
            w = med_avg.med_avg(ww)
        else:
            w = med_avg.mean(ww)
        data.w = w #update w in data
		
        accs[k] = AccTest.AccTest(w)
    fnfn[-1,:]=med_avg.mean(fnfn[0:-1,:]) #average all loss functions
	
	# Graph the loss functions
    stypes = ['No','Random','RoundRobin','SegShift']
    avtypes = ['mean','median','med_avg']
    lable = '%s shuffling and %s processing'%(stypes[shuff],avtypes[avc])
    ParsFile.ParsFile(np.transpose(fnfn),lable)
    print(accs)
    return w,fnfn,accs

if not isImported:
    #use
    K = 10
    N = 5
    win = np.zeros(784)
    shuff = 4
    avc = 1 #(averaging condition)
    stypes = ['No','Random','RoundRobin','SegShift']
    avtypes = ['mean','median','med_avg']
    labellist=["","","","","","","","","","","",""]

    fnfn = np.zeros(shape=(shuff*avc,K*N))
	### Runs the system using each type of shuffling(shuff) and potentially averaging (avc)
    for s in range(0,shuff):
        for i in range(0,avc):
            print(stypes[s],avtypes[i])
            starttime = time.time()
            w,fn,a = run(K,avc=i,shuff=s)
            fnew = med_avg.mean(fn)
            labellist[s+s*i] ="%s shuffling with %s model processing" %(stypes[s],avtypes[i])
            fnfn[s+s*i,:] = fnew

            print('Final time is: %.2f\n'%(time.time()-starttime))

    print('done')




#ssh pi@192.168.0.


