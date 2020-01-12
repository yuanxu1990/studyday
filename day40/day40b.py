'''


线程锁


'''


'''
线程锁   

'''

from threading import Thread,Lock
import time

# def func(lock,i):
#     lock.acquire()
#     print('第%s个'%i)
#     time.sleep(0.5)
#     lock.release()
#     pass

def func(lock):
    lock.acquire()
    global n
    temp=n
    time.sleep(0.2)
    n=temp-1
    lock.release()


if __name__ == '__main__':
    print(__name__)
    n=10
    t_lst=[]
    locks=Lock()
    '''
    多线程本身就收到gil锁的控制，但是gil锁是针对的线程
    并不能保证其他线程几乎同时访问同一个数据。
    所以要加锁，变异步为同步，降低了效率但是保证了数据的安全行
    
    '''
    # for i in range(10):
    #     t=Thread(target=func,args=(locks,i))
    #     t.start()
    for i in range(10):
        t=Thread(target=func,args=(locks,))
        t.start()
        t_lst.append(t)
    [a.join() for a in t_lst]
    print(n)

