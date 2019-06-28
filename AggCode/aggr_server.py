# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 12:50:36 2018

@author: fog
"""

import selectors
import socket
import pickle
import numpy as np
import types
isImported=True
'''
	This allows the aggregator to receive messages from all N nodes.
	Once called it will sit untill all messages are received
	Requires the number of nodes and the aggregator's ip
	returns a matrix of w vectors and loss functions as attributes of result
'''
def aggr_server(host,n):
#def aggr_server(host,N,que):  # add N as input (number of nodes)
    global N, keep_running, sel, numconn, result
    N = n
    #num = num_con # number of nodes to listen for
    numconn = 0 # number times has been connected to and recieved a vector
    sel = selectors.DefaultSelector()
    keep_running = True
    
    w = np.zeros((N,784))
    #w = []
    fn = []
    result = types.SimpleNamespace(w=w,fn=fn)
    host = host
    port = 65432
    
    server_addr = (host, port)       
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Avoid bind() exception: OSERROR: [Errno 48] Address already in use
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setblocking(False)
    server.bind(server_addr)
    server.listen()
    #print('listening on', (host, port))
    
    sel.register(server, selectors.EVENT_READ, accept) # call accept()
    
    while keep_running:
        event = sel.select()
        for key, mask in event:
            callback = key.data # .data = accept() or read()
            #print(callback)
            callback(key.fileobj, mask) # .fileobj is socket, 
     
    sel.close()
    
    return result


def accept(sock, mask): 
    conn, addr = sock.accept()  # Should be ready
    #print('accepted connection from', addr)
    conn.setblocking(1)
    sel.register(conn, selectors.EVENT_READ, read) # call read

def read(conn, mask):
    global keep_running, numconn, result
    
    datain = b''  # initialize
    dataRecvd = conn.recv(1024)
    while dataRecvd:
        datain += dataRecvd
        dataRecvd = conn.recv(1024)
    
    conn.setblocking(0)
    
    arr = pickle.loads(datain)# recieved data
    result.fn = np.append(result.fn, arr.fn)
    result.w[numconn,:] = arr.w
    sel.unregister(conn)
    conn.close()
    
    numconn += 1
    if numconn >= N: # if numconn == num_con # number of times w recieved = number nodes
        keep_running = False
 
if not isImported:
    host = '192.168.0.103' # aggregator ip
    num_con =  2 # number nodes to collect from 
    result = aggr_server(host,num_con)
    ##print(w)    



