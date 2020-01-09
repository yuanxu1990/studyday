'''
p=Pool
p.map(funcname,iterable)  默认异步的执行任务，且自带close和join

p.apply(funcname,args)    同步调用的

p.apply_async(funcname,args)
异步调用和主进程完全异步
如果不需要可以通过p.close()  p.join()来关闭进程池链接 等待进程池内任务执行完毕






进程池的返回值

1 队列
2 直接返回值接收




'''
from multiprocessing import Pool
import time

def func(i):
    time.sleep(0.5)
    return i*i

if __name__ == '__main__':
    p=Pool(5)

    #同步提交
    for i in range(10):
        res=p.apply(func,args=(i,))
        print(res)


    #
    # for i in range(10):
    #     res=p.apply_async(func,args=(i,))
    #     #res 打印的是异步调用后的对象
    #     print(res)
    #     #res.get() 打印的是异步调用后的结果
    #     # 但是在res=p.apply_async(func,args=(i,))
    #     # func并没有立刻返回结果 所以在res.get()
    #     # 就会阻塞在这里 等待结果 同时在表现形式 为 同步
    #     print(res.get())

    #异步解决方法
    # start_time1=time.time()
    # p_lis=[]
    # for i in range(10):
    #     res=p.apply_async(func,args=(i,))
    #     p_lis.append(res)
    #
    # print([a.get() for a in p_lis])
    # end_time=time.time()-start_time1
    # #异步解决方法
    # start_time2=time.time()
    # res=p.map(func,range(10))
    # print(res)
    # end_time2=time.time()-start_time2
    # print(end_time,end_time2)

    #map和apply_async的区别
    #map是一次性返回所有数据 apply_async一次返回进程池中数量一点一点的返回
    #执行效率上 map稍高 但是apply_async分次返回 节省内存
