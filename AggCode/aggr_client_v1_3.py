# aggr_client_v1
# v1_2
# v1_3: Keoki Daley 01/21/2019-16:57 MST
#       updated 01/31/2019-comments and useless lines removed

import socket
import pickle
import time

'''
	Send data to one node. requires some form of data to send and the ip of the recipiant 
'''

start = time.time()

def client(host,data):
    #print('aggr_client_v1_3 start: %.2f'%(time.time()-start))
    host = host
    data = data
    port = 65432
    datasend = pickle.dumps(data)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_addr = (host, port)
    s.connect(server_addr)
    total_sent = 0
    while len(datasend):
        sent = s.send(datasend)
        total_sent += sent
        datasend = datasend[sent:]
    #print('aggr_client_v1_3 end: %.2f'%(time.time()-start))
    s.close()
    