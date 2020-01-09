import socket

ck=socket.socket()
ck.connect(('127.0.0.1',10050))

ret=ck.recv(1024).decode('utf-8')
print(ret)

msg=input('>>>>>').encode('utf-8')
ck.send(msg)
