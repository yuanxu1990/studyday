import socket
qq=socket.socket(type=socket.SOCK_DGRAM)
qq.bind(('127.0.0.1',10020))

while True:
    msg,addr=qq.recvfrom(1024)
    print(msg.decode('utf-8'))
    serverinfo=input('服务端说：').encode('utf-8')
    qq.sendto(serverinfo,addr)

qq.close()