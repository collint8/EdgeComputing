import socket
import struct
import pickle

#turn usage on and off
#use = False
use = True

def m_recv():
#def m_recv(que):
    print("receiving")
    MCAST_GRP = '225.1.1.1' #UDP IP
    #MCAST_PORT = 5007 # UDP port
    #MCAST_GRP = '192.168.0.102'
    server_addr = ('',5007)
    #print(server_addr)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#, socket.IPPROTO_UDP)
    sock.bind(server_addr)
    print("bound to ", server_addr) 
    group = socket.inet_aton(MCAST_GRP)
    mreq = struct.pack("=4sl", group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    
#    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#    sock.setblocking(False)
    #sock.bind(('',5007))       
    #sock.bind((MCAST_GRP, MCAST_PORT))
#    mreq = struct.pack("=4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
#    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    
    on = True
    while on:
        print("trying to receive")
        recvd = sock.recv(8126)
        print(len(recvd))
        #recvd = sock.recvfrom(40000)
        if recvd:
            on = False

    rec = pickle.loads(recvd) 
    sock.close()  
    return rec
    #que.put(rec)

    
if use == True:
    #use:
    rec = m_recv()
    print(len(rec.w))
    print(rec.w)    











