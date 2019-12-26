import socket


sk=socket.socket(type=socket.SOCK_DGRAM)

ip_port=('127.0.0.1',10010)



sk.sendto(b'byte',ip_port)
msg,addr=sk.recvfrom(1024)
print(msg.decode('utf-8'))

sk.close()


