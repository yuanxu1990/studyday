'''
io multiplexing 也被成为事件驱动io  select/epoll的好处就在于单个process就可以同时处理多个网络链接的io
他的基本原理就是select/epoll这个function回不断的轮训所负责的所有socket 当某个socket有数据到到达了，就通知
用户进程   但是如果连接数较少的话还不如阻塞io效率高


'''

import select
import socket


sk=socket.socket()
sk.bind(('127.0.0.1',10088))
sk.setblocking(False)
sk.listen()
read_lista=[sk]
while True:
    #r_lst 里边只会有存 client给我链接的对象
    # 所以第一次循环 只会有sk也就是socket对象，因为sk对象接到了client的链接请求
    # 第二次client发送了信息，是给conn的也就是链接的
    # 所以r_lst中只会有conn的对象，能读的加载到r_lst
    print('io111')
    # 在select处阻塞
    r_lst,w_lst,x_lst=select.select(read_lista,[],[])
    print('io222')
    #r_lst内返回的实际上是socket对象
    print(r_lst)
    for i in r_lst:
        if i == sk:
            conn,addr=i.accept()
            read_lista.append(conn)
        else:
            msg=i.recv(1024).decode('utf-8')
            if msg==b'':
                i.close()
                read_lista.remove(i)
                continue
            print(msg)
            i.send(b'bye')
