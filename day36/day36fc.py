'''


多进程socket服务端的并发
'''

import socket


ck=socket.socket()
ck.connect(('127.0.0.1',10080))
res_msg=ck.recv(1024).decode('utf-8')
print(res_msg)
ck.send(b'yuan')

ck.close()