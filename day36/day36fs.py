import socket
from multiprocessing import Process




def sock_server(connt):
    sen_msg = input('>>>>>').encode('utf-8')
    connt.send(sen_msg)
    msg = connt.recv(1024).decode('utf-8')
    print(msg)
    connt.close()



if __name__ == '__main__':
    sk=socket.socket()
    sk.bind(('127.0.0.1',10080))
    sk.listen()
    while True:
        connt, addr = sk.accept()
        p1=Process(target=sock_server,args=(connt,))
        p1.start()
    sk.close()



