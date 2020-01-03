'''


多进程之间的数据通讯问题

进程和进程之间 数据是隔离的
'''


from multiprocessing import Process
import os
n=2
def func():
    global n
    n=100
    print('spid:',os.getpid(),n)


if __name__ == '__main__':
    n = 2
    p1=Process(target=func)
    p1.start()
    p1.join()
    print('fpid',os.getpid(),n)