from multiprocessing import Process
import time
'''
join()

'''

def func(args1,args2):
    print('*'*args1)
    time.sleep(5)
    print('*'*args2)


if __name__ == '__main__':

    p1=Process(target=func,args=(5,2))
    p1.start()
    print('yuanhahahha')  #在start和join中的代码可以随意执行 相对于子进程是异步的
    p1.join()     #感知一个子进程的结束由异步变成同步 好像将子进程中的代码拼接到主进程中 阻塞
    print('=======:close()')

