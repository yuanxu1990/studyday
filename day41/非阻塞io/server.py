import socket


#非阻塞io失败的例子
# sk=socket.socket()
# sk.bind(('127.0.0.1',10066))
# #设置为非阻塞 默认是阻塞
# sk.setblocking(False)
# sk.listen()
# # 如果没有收到链接就一直阻塞，让出了cpu控制权
# #sk.accept()
# while True:
#     try:
#         #sk.setblocking(False)之后
#         #收不到链接不但阻塞并且报错
#         #recv同理
#         conn,addr=sk.accept()
#         if conn:
#             print('建立链接')
#             msg=conn.recv(1024)
#             print(msg)
#     except BlockingIOError:
#         pass


sk=socket.socket()
sk.bind(('127.0.0.1',10066))
#设置为非阻塞 默认是阻塞
sk.setblocking(False)
sk.listen()
# 如果没有收到链接就一直阻塞，让出了cpu控制权
#sk.accept()
con_lista=[]
del_lista=[]
while True:
    try:
        #sk.setblocking(False)之后
        #收不到链接不但阻塞并且报错
        #recv同理
        conn,addr=sk.accept()
        print('建立链接',addr)
        # 要将链接存入列表，这是因为client有网络延迟
        # 本机执行代码速度远远快过网络延迟，如果recv放在这里回报错
        # 且恰好这是再有人链接server，conn会e被内存冲掉，就找不到当时和
        # server链接的通道
        con_lista.append(conn)
    except BlockingIOError:
            for a in con_lista:
                try:
                    #这里为什么将recv放在这里呢
                    #如果是非阻塞模式，那么收不到信息会报错
                    #这是因为client端有网络延迟，但是代码在本机会执行的
                    #很快所以必须要放在下边
                    msg = a.recv(1024)
                    if msg==b'':
                        # 如果客户端断开链接那么 接到的信息是byte类型的空信息
                        # 那么就将链接加入到del_lista列表中，这样就保存了准备删除的链接
                        del_lista.append(a)
                        continue
                    print(msg)
                    a.send(b'byebye')
                except BlockingIOError:
                    pass
            #等待循环结束之后 由于del_lista已经储存了将要删除的链接，则就可以循环删除
            for conn in del_lista:
                con_lista.remove(conn)
            #同时清空del_lista列表中的元素
            del_lista.clear()

