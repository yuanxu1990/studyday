'''
条件   Condition()
 更复杂的锁

 acquire release
 一个条件被创建之处，默认有一个False状态
 False状态，回影响wait一直处于等待状态 等待notify
 notify（int） 制造几把钥匙
'''
# from threading import Thread,Condition
#
# def func(con,i):
#     con.acquire()
#     con.wait()
#     print('在第%s个循环里'%i)
#     con.release()
#     print('%s还钥匙'%i)
# con=Condition()
# for i in range(10):
#     Thread(target=func,args=(con,i)).start()
#
# while True:
#     num=int(input('>>num'))
#     con.acquire()
#     con.notify(num)
#     con.release()
'''
Condition（条件变量）通常与一个锁关联。需要在多个Contidion中共享一个锁时，
可以传递一个Lock/RLock实例给构造方法，否则它将自己生成一个RLock实例。

可以认为，除了Lock带有的锁定池外，Condition还包含一个等待池，
池中的线程处于状态图中的等待阻塞状态，直到另一个线程调用notify()/notifyAll()通知；
得到通知后线程进入锁定池等待锁定。

Condition():

acquire(): 线程锁
release(): 释放锁
wait(timeout): 线程挂起，直到收到一个notify通知或者超时（可选的，浮点数，单位是秒s）才会被唤醒继续运行。
wait()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。
notify(n=1): 通知其他线程，那些挂起的线程接到这个通知之后会开始运行，
默认是通知一个正等待该condition的线程,最多则唤醒n个等待的线程。
notify()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。notify()不会主动释放Lock。
notifyAll(): 如果wait状态线程比较多，notifyAll的作用就是通知所有线程


'''
import time
from threading import Condition,Thread

'''
Condition 条件变量 其实底层还是应用的lock，在子进程获取锁之后，执行了wait之后就被挂起，等待notify
'''

class producer(Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        global num
        con.acquire()
        while True:
            print('开始添加鱼丸')
            num+=1
            print('锅里的鱼丸个数:%d'%num)
            time.sleep(1)
            if num>=5:
                print('锅里已经有了5个鱼丸，不在添加')
                # 唤醒等待的线程 就是发送给consumers的wait方法
                con.notify()
                #等待被唤醒，这里是等待consumers的notify方法
                con.wait()
        con.release()

class consumers(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        con.acquire()
        global num
        while True:
            print('开始吃拉')
            num-=1
            print('锅里剩余的鱼丸数量：%d'%num)
            time.sleep(2)
            if num==0:
                print('锅里没有丸子了加丸子')
                #唤醒等待的线程 就是发送给producer的wait方法
                con.notify()
                con.wait()
        con.release()
if __name__ == '__main__':
    con = Condition()
    num = 0
    p=producer()
    c=consumers()
    p.start()
    c.start()
