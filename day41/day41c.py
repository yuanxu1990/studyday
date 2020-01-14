'''


同步和异步

协程
    能够在一个线程中  实现并发效果的概念
    能够规避一些任务中的io操作
    在任务的执行过程中，检测到io就切换到其他任务

'''

from gevent import monkey;monkey.patch_all()
import time
import gevent
def time_check(func):
    def inner():
        start_time=time.time()
        func()
        end_time=time.time()-start_time
        print(func,end_time)
    return inner

def task():
    time.sleep(1)
    print(12345)
@time_check
def sync():
    for i in range(10):
        task()
@time_check
def asyn():
    g_lst=[]
    for i in range(10):
        g=gevent.spawn(task)
        g_lst.append(g)
    #[a.join() for a in g_lst]
    gevent.joinall(g_lst)

#通过 测试效率 发现异步采用协程比同步 高了10倍左右
sync()
asyn()


