# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 13:01:23 2018

@author: fog
"""
import selectors
import socket
import pickle
import numpy as np
import types


def client(wout,fn,host):
    
    #w = wout
    data = types.SimpleNamespace(w=wout,fn=fn) 
    keep_running = True
    datasend = pickle.dumps(data)    
    port = 65432    
    
    sel = selectors.DefaultSelector()
    
    server_addr = (host, port)
    print('starting connection to', server_addr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_addr) #.connect_ex()
    sock.setblocking(0) # vs False
    print(sock)
    sel.register(sock, selectors.EVENT_WRITE)

    while keep_running:
        print('waiting for connection')
        for key, mask in sel.select(timeout=None): #changed from 1 to None 11Nov
            conn = key.fileobj
            print(conn)

        totalsent = 0
        while len(datasend):
            print(len(datasend))
            sent = conn.send(datasend)
            totalsent += sent
            datasend = datasend[sent:]
            print('sending data',totalsent)

        print('data sent')
        keep_running = False
                
    print('shutting down')
    sel.unregister(conn)
    conn.close()
    sel.close()
    #return portionSent

 
###w, fn = NodeSvm.NodeSVM(w,N) # run SVM on node, N is nodenum
##host = '192.168.0.14'
##tau = 2
##w = np.ones(784) #w = np.zeros(784)
##fn = np.zeros(tau)
##data = client(w,fn,host)



