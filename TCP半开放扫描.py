from scapy.all import *
def main():
    ip = '192.168.19.128'
    port = 80
    packet = IP(dst=ip)/TCP(sport=12345,dport=port,flags="S")
    resp = sr1(packet,timeout=20)
    if(str(type(resp))=="<type 'NoneType'>"): #回包里没有东西
        print("port %s is closed"%(port))
    elif(resp.haslayer(TCP)):
        if(resp.getlayer(TCP).flags==0x12): #返回的头是0x12
            send_rst = sr(IP(dst=ip)/TCP(sport=12345,dport=port,flags="R"),timeout=20) #返回ack包AR=ack respone
            print("port %s is open"%(port))
        elif(resp.getlayer(TCP).flags==0x14): #返回的头是0x14
            print("port %s is down"%(port))
    pass
if __name__ == '__main__':
    main()