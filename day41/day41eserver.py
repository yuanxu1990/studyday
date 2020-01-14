from gevent import monkey
monkey.patch_all()
import socket
import gevent

'''
python的多线程被gil弱化了
协程在一个线程上 提高了cpu的利用率
协程相比多线程的优势  切换的效率更高

'''
def sock_server(con):
    '''
    使用gevent 必须要将
    from gevent import monkey
    monkey.patch_all() 导入
    不然gevent不认识socket的阻塞操作
    :param con:
    :return:
    '''
    while True:
        msg=con.recv(1024).decode('utf-8')
        print(msg)
        con.send(b'hello client')
        con.close()

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1', 10090))
    sk.listen()
    while True:
        con, addr = sk.accept()
        gevent.spawn(sock_server,con)
        print(123)
        con.close()
    sk.close()
