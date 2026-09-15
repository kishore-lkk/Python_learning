from scapy.all import *

packets =sniff(filter="tcp",count=10)
wrpcap("Learning/day_17_sidetrack/network_capture.pcap",packets)