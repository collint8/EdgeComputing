#

import nmap
import socket
#routerIP='192.168.0.1'

def run(routerIP):


#latency speed recording is possible with nmap.
    nMappy =nmap.PortScanner()
    
    #scanning the router's ip address, on specified ports.
    nMappy.scan(hosts='192.168.0.1/24', arguments= '-n -sn ') #-sP -PE -PA21,23,24,80,3389
    #scanner results are put into a matrix. Status is ignored, only the ip.
    hosts_list = [(x) for x in nMappy.all_hosts()]
            
    #removing the router's IP address.
    hosts_list.remove(routerIP)
    
    #identify aggregator IP address
    aggIPList = socket.gethostbyname_ex(socket.gethostname())[2]
    aggIP = aggIPList[-1]
    #removing aggregator IP address
    
    hosts_list.remove(aggIP)
    return aggIP, hosts_list

print(run('192.168.0.1'))
print(' ')