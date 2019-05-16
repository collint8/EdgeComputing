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
import MakeFile
import aggr_client_v1_3 as aggr_client
import aggr_server
import nodeDetection
import med_avg
import time
import matplotlib.pyplot as pt
#aggr_server(host,num_con,que)
isImported = True

def run(K,tau=0,shuff=0,avc=0):
    
    # node detection
    router_ip = '192.168.0.1'
    host,iplist = nodeDetection.run(router_ip)
    node_dict = {} # determine number of nodes
    n = 0
    for ind in iplist:
        node_dict[ind] = n
        n += 1
    N = n
    if tau ==0:
        tau =N
    multiplier = 10
    d = 10#multiplier * n # number data points per node
    #D = d * N # total number of data points needed
    w = np.zeros(784)
    #w = np.ones(784)
    #filepath = r"train.csv"
    #ww = np.zeros[N,784]
    fnfn = np.zeros(shape=(n+1,K*tau))
    accs = np.zeros(K)

    
    for ind in range (0,K): # aggregator as client, k global iterations 
        # send global update information to nodes
        #data_pts = pd.read_csv(filepath, skiprows=(ind*D), nrows=(D)).values
        
        ### Currently using the same dataset throughout. change k=k to refresh data
        data = types.SimpleNamespace(w=w,k=0,host=host,node_dict=node_dict,d=d,tau=tau,shuff=shuff)#data_pts=data_pts) #data on nodes
        #datasend = pickle.dumps(data) 
        #print(len(datasend))
        
        #mcast_send.send(data)
        for i in range(0,N):
            aggr_client.client(iplist[i],data)
        
        # aggregator as server; get ws from nodes 
        result  = aggr_server.aggr_server(host,N)
        ww = result.w
        for i in range(0,N):
            fnfn[i,ind*tau:(ind+1)*tau] = result.fn[i*tau:i*tau+tau]
#            MakeFile.MakeFile(fnfn,i)
#        print('this is avc',avc)
        w = ww
        if avc==1:
            w = med_avg.med(ww)
        elif avc==2:
            w = med_avg.med_avg(ww)
        else:
            w = med_avg.mean(ww)
        data.w = w
#        print('averaged')
        accs[ind] = AccTest.AccTest(w)
    fnfn[-1,:]=med_avg.mean(fnfn[0:-1,:])
    stypes = ['No','Random','RoundRobin','SegShift']
    avtypes = ['mean','median','med_avg']
    lable = '%s shuffling and %s processing'%(stypes[shuff],avtypes[avc])
    ParsFile.ParsFile(np.transpose(fnfn),lable)
    print(accs)
    return w,fnfn,accs

if not isImported:
    #use
    K = 5
    N = 5
    win = np.zeros(784)
    shuff = 4
    avc = 1
    stypes = ['No','Random','RoundRobin','SegShift']
    avtypes = ['mean','median','med_avg']
    labellist=["","","","","","","","","","","",""]

    fnfn = np.zeros(shape=(shuff*avc,K*N))
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


