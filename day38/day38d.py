'''
进程同步控制---锁/信号量/事件

multiprocessing.Lock
multiprocessing.Semaphore
multiprocessing.Event


进程间通讯  队列和管道
multiprocessing.Queue
multiprocessing.Pipe


进程间的数据共享
multiprocessing.Manager


消息中间件  接受消息发送
send------mamcache-------recv

kafak
rabbitmq
memcache
redis

'''


'''
进程池  process pool
        提高了效率
        每开启一个进程 都需要开启属于这个进程的内存空间（寄存器 堆栈 文件）
        进程过多 操作系统的调度

进程池
      python中的进程池  
           在python中在启动程序之前，先建立一个数据进程的尺子
           这个尺子指定能存放多少个进程
           先将这些进程创建好
      进程池和信号量区别
            信号量  进程等待排队  多个进程已经被创建 等待执行代码
            进程池  任务等待排队  固定的进程已经被创建 任务每次使用就调用一个进程 任务完成后 将进程放回进程池
            
            
更高级的进程池  默认上限服务器cpu+1
       n,m（进程上下限）
       某一时段只使用n个进程
       如果不够用就自动加进程
       上限为m
'''

from multiprocessing import Pool,Process
import time

def func(n):
    # for i in range(10):
    #     print(n+1)
    print(n)
def func1(m):
    print(m[0])
    print(m[1])

if __name__ == '__main__':
    # 创建线程池指定线程有5个
    # start_time=time.time()
    #  Pool()若不指定参数 则默认本机所有的cpu数量os.cpu_count()
    poo=Pool(5)
    #poo.map(func,{'num':10,'age':18})
    #poo.map(func,[0,1,3,4,5])
    # 创建100个任务 可迭代参数中传多少就是多少
    #每次只能同时启动5个进程但是进程并没有
    #map自带join
    #只使用5个进程 执行函数 直到可迭代对象中值被函数执行完毕
    # poo.map(func,range(100))
    poo.map(func1,[('yuan',18),])
    # end=time.time()-start_time
    # start_time1=time.time()
    # p_lis=[]
    # for i in range(100):
    #     p=Process(target=func,args=(i,))
    #     p.start()
    #     p_lis.append(p)
    # [a.join() for a in p_lis]
    # end1=time.time()-start_time1
    # print(end,end1)
    # print(end1/end)
