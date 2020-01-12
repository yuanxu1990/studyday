from threading import Thread

import socket


if __name__ == '__main__':

    ck=socket.socket()
    ck.connect(('127.0.0.1',10060))
    while True:
        msg=input('client>>>>').encode('utf-8')
        ck.send(msg)
        res_msg=ck.recv(1024).decode('utf-8')
        print(res_msg)
        if res_msg=='q':
            ck.close()
            break
