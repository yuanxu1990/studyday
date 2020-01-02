'''

socket tcp 只能和一个客户端通讯
socketserver tcp 能和多个客户端通讯
       1 必须继承  ocketserver.BaseRequestHandler
       2 类中必须要有一个叫handle的方法

看源码
    1 多个类之间的继承关系要先整理
    2 每一个类中有哪些方法 要大致列出来
    3 所有的self对象调用要清除了解 到底是谁的对象
    4 所有的方法调用 要退回到最子类的类中开始寻找逐级向上


'''

import socketserver

class myserver(socketserver.BaseRequestHandler):
    def handle(self):#self.request相当与 socket中的链接 类似于day33bs 中的conn
        while True:
            msg=self.request.recv(1024).decode('utf-8')
            print(msg)
            info=input('server>>>>').encode('utf-8')
            self.request.send(info)
if __name__ == '__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',10095),myserver)
    server.serve_forever()# 永远启动一个server服务