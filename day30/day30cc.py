import time
import socket


ck=socket.socket()
ck.connect(('127.0.0.1',10005))
countc=0
while 1:
    countc+=1
    if countc<10:
        time.sleep(5)
        ctime=time.time()
        ck.send(bytes(str(ctime),encoding='utf-8'))
        ret=ck.recv(1024).decode('utf-8')
        print('s--->',ret)
    else:
        break
ck.close()