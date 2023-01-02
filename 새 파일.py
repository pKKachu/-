from socket import *
import os


def parsing(host): # raw socket 생성 및 bind
    if os.name=="nt":
        sock_protocol=IPPROTO_IP
    else:0
        sock_protocol=IPPROTO_ICMP
    sock=socket(AF_INET, SOCK_RAW, sock_protocol)
    sock.bind((host, 0))
    
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1) #socket옵션
    
    if os.name=="nt":
        sock.ioctl(SIO_RCVALL. RCVALL_ON) #promiscuous mode
    
    data=sock.recvfrom(65535)
    print(data[0])
    
    if os.name=="nt":
        sock.ioctl(SIO_RCVALL, RCCALL_OFF) #promiscuous mode 끄기
        
        sock.close() #소켓 종료
        
        if __name__=="__main__":
            host="192.168.45.184" # 자신의 IP주소로 변경
            print(f"Listening at [{host}]")
            parsing(host)
        
    
    
