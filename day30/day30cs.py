'''
c 10秒发送time.time() 发给s
s 接收时间戳，转化成格式化时间
'''

import time
import socket
import time


sk=socket.socket()
sk.bind(('127.0.0.1',10005))
sk.listen()
conn,addr=sk.accept()
count=0
while 1:
    count+=1
    if count<10:
        stime=conn.recv(1024)
        print('s-->',(stime))
        stime=float((stime))
        fortime=time.localtime(stime)
        strtime=time.strftime('%Y-%m-%d %H:%M:%S',fortime)
        print(type(strtime))
        conn.send(bytes(strtime,encoding='utf-8'))
    else:
        break
conn.close()
sk.close()



