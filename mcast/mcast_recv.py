import socket
import struct
import pickle

#turn usage on and off
use = False
use = True

def m_recv():
#def m_recv(que):
    print('M_recv called')
    MCAST_GRP = '225.1.1.1' #UDP IP
    #MCAST_GRP = '224.3.29.71'
    MCAST_PORT = 5007 # UDP port
    #MCAST_GRP = '192.168.0.102'
    #server_addr = ('192.168.0.101',10000)
    server_addr = ('',MCAST_PORT)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#, socket.IPPROTO_UDP)
    
    sock.bind(server_addr)
    print("bound to ", server_addr)    
    group = socket.inet_aton(MCAST_GRP)
    mreq = struct.pack('=4sl', group, socket.INADDR_ANY) # removed "=" from 4sl
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
#    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#    mreq = struct.pack("=4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
#    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
#    sock.settimeout(10)
    
    on = True
    while on:
        print("YO")
        #recvd = sock.recv(8126)
        recvd, addr = sock.recvfrom(8126)
#        try:
#            recvd, addr = sock.recvfrom(8126)
#            print('recvd', recvd, addr)
#            #print(len(recvd))
#            #recvd = sock.recvfrom(40000)
#            print("dog")
#        except socket.timeout:
#            print('timed out')
#            break
        if recvd:            
            on = False
        print('recvd',len(recvd))
        
    print('recieved info')
    rec = pickle.loads(recvd) 
    sock.close()  
    #return rec
    return rec
    #que.put(rec)

    
if use == True:
    #use:
    rec = m_recv()
    print((rec.w))
    











