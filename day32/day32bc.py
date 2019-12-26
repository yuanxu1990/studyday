import socket

import subprocess

ck=socket.socket()
ck.connect(('127.0.0.1',10070))
while True:
    cmd=ck.recv(1024).decode('utf-8')
    if cmd=='q':
        break
    res=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)#管道中的数据只能取一次类似队列
    res_stdout=res.stdout.read()
    res_stderr=res.stderr.read()
    ck.send(str(len(res_stdout)+len(res_stderr)).encode('utf-8'))
    slen=(ck.recv(1024))
    if slen:
        ck.send(res_stdout)
        ck.send(res_stderr)
ck.close()

# 好处 确定了我到底要接受多大的数据
# 坏处  多了一次交互 网络延迟