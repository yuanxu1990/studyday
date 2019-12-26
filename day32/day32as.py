import socket

sk=socket.socket()
sk.bind(('127.0.0.1',10060))

sk.listen()
conn,addr=sk.accept()
while True:
    cmd=input('命令---->')
    if cmd=='q':
        conn.send(b'q')
        break
    conn.send(cmd.encode('gbk'))
    ret=conn.recv(1024)
    print(ret.decode('gbk'))
conn.close()
sk.close()