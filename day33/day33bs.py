'''

检测用户端是否合法
不依靠登录认证


import hmac
'''
import hmac        #hashlib
import os
import socket

strect_key='yuan'.encode('utf-8')

sk=socket.socket()
sk.bind(('127.0.0.1',10090))
sk.listen()
conn,addr=sk.accept()
def check_conn(conn):
    msg=os.urandom(32)
    conn.send(msg)
    ret=hmac.new(strect_key,msg)  #secret_key  你想进行加密的bytes
    server_digst=ret.digest()     #加密 得到密文
    client_digst=conn.recv(1024)
    return hmac.compare_digest(client_digst,server_digst)   #对比密文    （密文，另外一个密文）
ret=check_conn(conn)
if ret:
    print('login pass')
    conn.close()
else:
    print('login faile')
    conn.close()
sk.close()