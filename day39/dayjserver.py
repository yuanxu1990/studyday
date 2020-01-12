from threading import Thread
import socket

def func(conn):
    while True:
        res_msg=conn.recv(1024).decode('utf-8')
        print(res_msg)
        if not  res_msg=='q':
            msg=input('server>>>').encode('utf8')
            conn.send(msg)
        else:
            conn.send(b'q')
            conn.close()
            break




if __name__ == '__main__':
    sk=socket.socket()
    sk.bind(('127.0.0.1',10060))
    sk.listen()
    while True:
        conn,addr=sk.accept()
        t=Thread(target=func,args=(conn,))
        t.start()
    sk.close()