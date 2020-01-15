import time
import socket
import threading

def func():
    ck=socket.socket()
    ck.connect(('127.0.0.1',10088))
    ck.send(b'hello')
    time.sleep(1)
    print(ck.recv(1024))
    ck.close()

for i in range(10):
    threading.Thread(target=func).start()