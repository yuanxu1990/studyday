import socket

ck=socket.socket()
ck.connect(('127.0.0.1',10090))
while True:
    ck.send(b'hello server')
    msg=ck.recv(1024)
    print(msg)
ck.close()