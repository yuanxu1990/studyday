'''

有几个重要的协议  tcp udp ip  arp
应用层的协议   http（https） 网页   ftp文件传输   smtp邮件相关的协议


'''

#client  接受命令


import socket
import subprocess
ck=socket.socket()
ck.connect(('127.0.0.1',10060))

while True:
    cmd=ck.recv(1024).decode('gbk')
    if cmd=='q':
        break
    res=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    ck.send(res.stdout.read())
    ck.send(res.stderr.read())
ck.close()