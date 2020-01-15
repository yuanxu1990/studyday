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
#设置为非阻塞 默认是阻塞 把socket当中需要阻塞的方法都改变成非阻塞 recv recvfrom accpet
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
                conn.close()
                con_lista.remove(conn)
            #同时清空del_lista列表中的元素
            del_lista.clear()

'''
非阻塞io一般不推荐
优点 ：
     能够在等待任务完成的时间里干其他活 （包括提交其他任务，也就是后台 可以有多个任务在同时执行）

缺点：
    1 循环调用recv（）将大幅推高cpu占用率，这也是我们在代码中留一句time.sleep()的原因，否则在低配主机下极容易出现卡机情况
    2 任务完成的响应延迟增大了，因为每过一段时间才去轮训一次read操作，而任务可能在两次轮询之间的任意时间完成，这回导致整体
    数据吞吐量的降低

此外 在这个方案占用recv（）更多的是起到检测 操作是否完成  的作用，实际操作系统提供了更为高效的检测 操作是否完成 作用的接口
例如select（）多路复用模式，可以一次检测多个链接是否活跃

'''