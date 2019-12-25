'''


socket

  socket是应用层与tcp/ip协议族通信的中间软件抽象层  是一组接口 在设计模式中 socket其实就是一个门面模式
  它把复杂的tcp/IP协议族隐藏在socket接口后面，对用户来说，一组简单的接口即使全部
  让socket去组织数据，以符合指定的协议

  socket是一个模块 我们通过模块中已经实现的方法建立两个进程之间的链接和通信 也有人将socket说成ip+port
  因为ip是用来在互联网中的一台主机的位置，而port用来表示主机上的应用程序  所以我们只要确立了ip和sort就能找到一个应用程序
  并使用socket模块来与之通讯

  开始套接字被设计用在同一台主机多个应用程序之间的通讯，这也被成为进程间的通讯或ipc
  套接字有两种 分别是基于文件行的和基于网络型的
'''


import socket

#tcp  有收必有发  收发必相等

sk=socket.socket()             #买手机 创建socket对象
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#避免服务重启的时候报address already in use
sk.bind(('127.0.0.1',10001))   #绑定手机卡
sk.listen()                    #监听 等着有人给我打电话
conn,addr=sk.accept()          #参数conn 链接     addr客户端地址
while 1:
    ret=conn.recv(1024)            #接收   听别人说话 1024倍数
    print(ret)
    conn.send(b'hello')            #发送   给别人说话   参数必须传bytes
conn.close()                   #关闭链接  挂电话
sk.close()                     #关手机
