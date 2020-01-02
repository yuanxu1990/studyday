import socket

ck=socket.socket()
ck.connect(('127.0.0.1',10095))
ck.send(b'client')
ck.close()