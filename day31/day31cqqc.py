import socket

qqc=socket.socket(type=socket.SOCK_DGRAM)
ip_port=('127.0.0.1',10020)
while True:
    info=input('客服端说：').encode('utf-8')
    qqc.sendto(info,ip_port)
    ret,addr=qqc.recvfrom(1024)
    print(ret.decode('utf-8'))


qqc.close()