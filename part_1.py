# import dpkt

# counter=0
# ipcounter=0
# tcpcounter=0
# udpcounter=0

# filename ='project_A.pcap'

# for ts, pkt in dpkt.pcap.Reader(open(filename,'rb')):

#     counter+=1
#     eth=dpkt.ethernet.Ethernet(pkt)
#     ip=eth.data
#     if ip(eth.src) == '10.182.0.2':
#    #  if eth.type!=dpkt.ethernet.ETH_TYPE_IP:
#        continue

#    #  ip=eth.data
#     ipcounter+=1

#     if ip.p==dpkt.ip.IP_PROTO_TCP: 
#        tcpcounter+=1

#     if ip.p==dpkt.ip.IP_PROTO_UDP:
#        udpcounter+=1

# print("Total number of packets in the pcap file: ", counter)
# print("Total number of ip packets: ", ipcounter)
# print("Total number of tcp packets: ", tcpcounter)
# print("Total number of udp packets: ", udpcounter)






from scapy.all import *

fob = rdpcap('project_A.pcap') 
cap = []
inputFileName= input("Enter name of input file: ")

counter = 0

for pkt in fob:
    if pkt.haslayer(IP):
        if pkt[IP].src == '10.182.0.2':
            counter+=1
            
counter = counter/3


print(int(counter))