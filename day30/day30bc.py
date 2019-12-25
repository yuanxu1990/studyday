import socket

ck=socket.socket()
ck.connect(('127.0.0.1',10001))       #拨号  s端的ip和端口号
while 1:
    ck.send(b'this is client')

    ret01=ck.recv(1024)
    print(ret01)

ck.close()