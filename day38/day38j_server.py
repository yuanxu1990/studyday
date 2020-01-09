import socket
from multiprocessing import Pool

def func(conn):
    conn.send(b'hello')
    print(conn.recv(1024).decode('utf-8'))
    conn.close()



if __name__ == '__main__':
    p=Pool(5)
    sk=socket.socket()
    sk.bind(('127.0.0.1',10050))
    sk.listen()
    while True:
        conn,addr=sk.accept()
        p.apply_async(func,args=(conn,))
        # p.close()
        # p.join()
    sk.close()
