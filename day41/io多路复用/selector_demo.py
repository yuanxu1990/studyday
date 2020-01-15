'''
selectors  会自动选择适合你当前系统的 io多路复用模式
           例如在win上使用select 在linux上是用poll或epoll


'''
from socket import *
import selectors


def accpet(server_fileobj,mask):
    conn,addr=server_fileobj.accpet()
    sel.register(conn,selectors.EVENT_READ,read)

def read(conn,mask):
    try:
        data=conn.recv(1024)
        if not data:
            print('closing',conn)
            sel.unregister(conn)
            conn.close()
            return
        conn.send(data.upper()+b'_SB')
    except Exception:
        print('closing',conn)
        sel.unregister(conn)
        conn.close()
sel=selectors.DefaultSelector()# 选择一个适合我的io多路复用
sk=socket()
sk.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sk.bind(('127.0.0.1',8088))
sk.listen(5)
sk.setblocking(False)
#相当于往select的读列表李append了一个文件句柄server_fileobj
#说白了就是 如果有人请求链接sk就appect方法
sel.register(sk,selectors.EVENT_READ,accpet)

while True:
    events=sel.select()   #检测所有的fileobj 时候有完成wait_data的
    for sel_obj,mask in events:
        callback=sel_obj.data#callback=accpet
        callback(sel_obj.fileobj,mask)#accpet(server_fileobj,1)