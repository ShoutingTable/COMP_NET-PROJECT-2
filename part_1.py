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
