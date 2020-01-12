'''
线程 事件

链接数据库
  检查数据库的可链接情况
     1 能够更方便的对数据进行怎删改查
     2 安全访问的机制

'''
from threading import Thread,Event
import time,random
def connect_db(e):
    cont=0
    while cont<3:
        e.wait(1)
        if e.is_set():
            print('链接数据库成功')
            break
        else:
            cont += 1
            print('第%s次链接数据库失败'%cont)
    else:
        raise TimeoutError("数据库链接超时")


def check_web(e):
    time.sleep(random.randint(0,10))
    e.set()
if __name__ == '__main__':
    e=Event()
    t1=Thread(target=check_web,args=(e,))
    t1.start()
    t2=Thread(target=connect_db,args=(e,))
    t2.start()
