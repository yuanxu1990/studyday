import socket
import time
from threading import Thread

# ck=socket.socket()
# ck.connect(('127.0.0.1',10066))
# ck.send(b'hello')
# msg=input('client>>>').encode('utf8')
# ck.send(msg)
# time.sleep(0.1)
# ck.send(b'hello')
# ck.close()
def func():
    ck=socket.socket()
    ck.connect(('127.0.0.1',10066))
    ck.send(b'hello')
    time.sleep(1)
    print(ck.recv(1024))
    ck.close()

for i in range(20):
    Thread(target=func).start()