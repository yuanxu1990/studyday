import socket

sk=socket.socket()
sk.bind(('127.0.0.1',10055))
sk.listen()

while 1:
    conn,addr=sk.accept()
    data=conn.recv(1024)
    # 前后端 使用http格式交互数据，在浏览器直接访问
    with open('data','rb')as f:
        msg=f.read()
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    conn.send(msg)
    conn.close()

sk.close()