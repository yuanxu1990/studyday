'''


守护进程

子进程转化守护进程
   主进程结束 子进程也要结束
守护进程 回随着主进程的代码执行完毕 而结束




'''

from multiprocessing import Process
import time


def func():
    while True:
        time.sleep(0.2)
        print("子进程转化为守护进程")
def func1():
    print('子进程start')
    time.sleep(8)
    print('子进程end')

if __name__ == '__main__':
    '''
    p1为主进程的守护进程p2为子进程
    
    守护进程只会关注主进程是否结束
        比如主进程代码结束后，p1就回结束
        但是p2还没有结束 但是p1已经随着主进程的结束已经不执行了
    
    而父进程会关注子进程是否已经结束
        父进程已经结束了 但是p2还没有结束
        父进程回等待p2的结束而结束
        这时候父进程的代码已经执行完毕了
        所以守护进程也不结束了


在主进程内结束一个子进程 p.terminate()
     结束一个进程不是在执行方法之后立即生效 需要操作系统相应的过程
检查一个进程是否还存在的状态 p.is_alive()
p.name p.pid p.getpid 分别是获取进程的名字 进程号 以及父进程
    
    
    '''
    p1=Process(target=func)
    p1.daemon=True  #设置子进程为守护进程
    p1.start()
    p2=Process(target=func1)
    p2.start()
    print(p1.is_alive())#检查进程是否还存在还活着
    print(p2.name)    #获取一个进程的名字
    p2.terminate()  #结束一个进程
    # 这个时候应该是True
    # 因为上一句代码发结束进程指令发给了操作系统
    # 操作系统还需要时间关闭该进程
    p2.is_alive()
    i=0
    while i<5:
        print('我是socket，server',i)
        time.sleep(1)
        i+=1
    p2.join()
    print(p1.is_alive())
    print(p2.is_alive())