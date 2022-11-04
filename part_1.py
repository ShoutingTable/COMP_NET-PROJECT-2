from scapy.all import *
# We imported scapy to our modules to add functions to work with PCAP

cap = [] # intializes array
PCAP_FILE = rdpcap(input("Enter name of input file: ")) # takes input file for TCP flow count

counter = 0 # initialize count at 0

for pkt in PCAP_FILE: 
    if pkt.haslayer(IP):
        if pkt[IP].src == '10.182.0.2': # packet source is 10.182.0.2
            counter+=1 # counter will add 1 if source IP address is 10.182.0.2
            
counter = counter/3 # shows three way handshake and calculates TCP flow(s)


print("The total number of TCP flow(s):", int(counter)) # prints the TCP flow(s)
