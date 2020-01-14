from gevent import monkey;monkey.patch_all()
from greenlet import greenlet
import time




#真正的协程模块 就是使用greenlet完成的切换
# def eat():
#     print('start eat')
#     g2.switch()  #切换 且有记录上次代码执行的位置
#     print('end eat')
#     g2.switch()
#
# def play():
#     print('og')
#     g1.switch()
#     print('end og')


# g2=greenlet(play)
# g1=greenlet(eat)
# # 切换
# g1.switch()

'''
线程的效率 对比
比如2个任务，一个任务中有io操作，就可以用swich切换到另外一个任务执行
等前一个任务的io结束就可以 在切换回来 是线程不空闲

进程+线程+协程
操作系统 调度进程+线程
协程之间的程序 由程序完成。例如join。只有遇到协程模块认识的io操作的时候，程序才会切换
实现并发的效果，实现并发的效果


进程+线程+协程
5（cpu+1）   + 20（cpu*5） + 500（一个线程内）
'''
# def f1():
#     res=1
#     for i in range(100000000):
#         res+=i
# def f2():
#     res=1
#     for i in range(100000000):
#         res*=i
# start_time=time.time()
# f1()
# f2()
# stop=time.time()
# print('run time is %s'%(stop-start_time))

#
# def f3():
#     res=1
#     for i in range(100000000):
#         res+=i
#         g2.switch()
# def f4():
#     res=1
#     for i in range(100000000):
#         res*=i
#         g1.switch()
#
# start_time=time.time()
# g1=greenlet(f3)
# g2=greenlet(f4)
# g1.switch()
# stop=time.time()
# print('run time is %s'%(stop-start_time))

'''
gevent 模块

'''

import gevent
import threading
def eat(name):
    print(threading.current_thread().getName())
    print('%s eat 1'%name)
    # 但是协程无法感知time.sleep()
    # 但是能感知gevent.sleep()
    # 但是可以在引入的最上方使用from gevent import monkey;monkey.patch_all()
    # 可以将引入包的所有io操作打成一个包 那么time.sleep(）就可以被gevent感知
    #gevent.sleep(1)
    time.sleep(1)
    print('%s eat 2'%name)
    return 1
def play(name):
    '''
    # 但是协程无法感知time.sleep()
    # 但是能感知gevent.sleep()
    :param name:
    :return:
    '''
    print(threading.current_thread().getName())
    print('%s play 1'%name)
    #gevent.sleep(1)
    time.sleep(1)
    print('%s play 2'%name)

if __name__ == '__main__':
    #g1=gevent.spawn(funcname,1,2,3,多个参数（可以是位置参数或者关键字实参）)
    g1=gevent.spawn(eat,'egon')
    g2=gevent.spawn(play,name='egon')
    # 加  join（） 之后会启动协程  但是协程无法感知time.sleep() 但是能感知gevent.sleep()
    g1.join()   #等待g1结束
    g2.join()   #等待g2结束
    print(g1.value)
    #gevent.joinall(g1,g2)