
from scapy.all import *
from pathlib import Path

packets = [
    # ARP request
    Ether(src="02:00:00:00:01:10", dst="ff:ff:ff:ff:ff:ff") /
    ARP(op=1, hwsrc="02:00:00:00:01:10",
        psrc="192.168.1.10", pdst="192.168.1.1"),

    # ARP reply
    Ether(src="02:00:00:00:01:01", dst="02:00:00:00:01:10") /
    ARP(op=2, hwsrc="02:00:00:00:01:01",
        psrc="192.168.1.1", pdst="192.168.1.10"),

    # DNS query
    Ether() /
    IP(src="192.168.1.10", dst="192.168.1.1") /
    UDP(sport=53000, dport=53) /
    DNS(rd=1, qd=DNSQR(qname="example.com")),

    # TCP SYN
    Ether() /
    IP(src="192.168.1.10", dst="93.184.216.34") /
    TCP(sport=50000, dport=80, flags="S", seq=1000),

    # TCP SYN-ACK
    Ether() /
    IP(src="93.184.216.34", dst="192.168.1.10") /
    TCP(sport=80, dport=50000, flags="SA", seq=2000, ack=1001),

    # HTTP GET
    Ether() /
    IP(src="192.168.1.10", dst="93.184.216.34") /
    TCP(sport=50000, dport=80, flags="PA", seq=1001, ack=2001) /
    Raw(load=b"GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n"),

    # ICMP ping
    Ether() /
    IP(src="192.168.1.10", dst="8.8.8.8") /
    ICMP(type="echo-request", id=1, seq=1),

    # ICMP reply
    Ether() /
    IP(src="8.8.8.8", dst="192.168.1.10") /
    ICMP(type="echo-reply", id=1, seq=1)
]

wrpcap("sample_traffic.pcap", packets)

print("Created sample_traffic.pcap")
print(f"Packets: {len(packets)}")