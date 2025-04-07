from scapy.all import *
import time
from random import randint
def main():
    while 1:
        pdst = "%i.%i.%i.%i"%(randint(1,254),randint(1,254),randint(1,254),randint(1,254))
        psrc = "192.168.19.12"
        send(IP(src=psrc,dst=pdst)/ICMP())
        time,sleep(0.5)
        print(pdst)
    pass
if __name__ == '__main__':
    main()