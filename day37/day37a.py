'''
多进程代码

方法
    进程对象.start()       开启一个子进程
    进程对象.join()        感知一个子进程的结束
    进程对象.is_alive()    结束一个子进程
    进程对象.terminate()   查看某个子进程是否存货

属性
     进程对象.name          进程的名字
     进程对象.pid           进程的id
     进程对象.daemon        设置进程为守护进程
          守护进程随着主进程代码的执行结束而结束
           要在start之前设置


锁
from multiprocessing import Lock
l=Lock()
l.acquire()      拿钥匙
l.replease()    还钥匙


'''