from scapy.all import rdpcap, IP, TCP, UDP, ICMP, ARP

# Load the capture file
packets = rdpcap("sample_traffic.pcap")

print(f"Total packets: {len(packets)}\n")

for i, packet in enumerate(packets, 1):
    print(f"--- Packet {i} ---")

    # IP packet
    if IP in packet:
        ip = packet[IP]

        print(f"Source      : {ip.src}")
        print(f"Destination : {ip.dst}")
        print(f"Protocol    : {ip.proto}")
        print(f"Packet Size : {len(packet)} bytes")

        # TCP
        if TCP in packet:
            tcp = packet[TCP]
            print("Transport   : TCP")
            print(f"Source Port : {tcp.sport}")
            print(f"Dest Port   : {tcp.dport}")
            print(f"Flags       : {tcp.flags}")

        # UDP
        elif UDP in packet:
            udp = packet[UDP]
            print("Transport   : UDP")
            print(f"Source Port : {udp.sport}")
            print(f"Dest Port   : {udp.dport}")

        # ICMP
        elif ICMP in packet:
            print("Transport   : ICMP")

    # ARP packet
    elif ARP in packet:
        arp = packet[ARP]

        print("Protocol    : ARP")
        print(f"Sender      : {arp.psrc}")
        print(f"Target      : {arp.pdst}")
        print(f"Sender MAC  : {arp.hwsrc}")
        print(f"Target MAC  : {arp.hwdst}")

    else:
        print(f"Protocol    : {packet.summary()}")

    print()