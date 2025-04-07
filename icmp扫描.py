from whois import whois

from scapy.all import *
from random import randint
def main():
    ip_id = randint(1,65535)
    icmp_id = randint(1,65535)
    icmp_seq = randint(1,65535)
    packet = IP(dst="192.168.19.212",ttl=64,id=ip_id)/ICMP(id=icmp_id,seq=id_seq)/b'rootkit' #创建一个 IP 数据包，目标地址为 192.168.19.212，TTL（存活时间，每经过一个路由器减一）为 64，ID 为 ip_id。然后，将一个 ICMP 数据包附加到 IP 数据包上，ICMP 数据包的 ID 为 icmp_id，序列号为 icmp_seq。最后，将字节串 b'rootkit' 附加到 ICMP 数据包上作为数据负载个包
    result = sr1(packet,timeout=1,verbose=False) # verbose=False 代表着不输出日志信息
    if result:
        for rcv in result:
            scan_ip = rcv[IP].src # 获取源IP地址
            print(scan_ip+'is alive')
    else:
        printa('is down')
    pass
if __name__ == '__main__':
    main()