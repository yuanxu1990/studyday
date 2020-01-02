'''

启动多个子进程


'''

from multiprocessing import Process
import time

def func(args1,args2):
    print('*'*args1)
    time.sleep(1)
    print('*'*args2)
    return 1


if __name__ == '__main__':
    p_list=[]
    for i in range(10):
        p=Process(target=func,args=(2*i,4*i))
        p_list.append(p)
        p.start()
    #for循环中的子进程是异步执行，但是并不是所有的进程都是
    #同时执行，在告诉操作系统时确实是按照顺序告诉的
    #但是操作系统并不一定是按照顺序执行，那么就无法保证
    #子进程全部结束了,就像下边的p.join（）此时的p是上边
    #for循环等于10的时候。所以可以将子进程都装到list表中
    #在利用列表推倒式循环每一个p，确保没一个p都已经被结束
    #这样所有的子进程之间都是异步 但是整个子进程相对于父进程
    #又是同步的

    #比如 启动100个进程 去写文件 要想在写完之后再去读
    #就需要这样 确保每一个子进程都写完


    #p.join()
    [p.join() for p in p_list]
    print('子进程全部结束')
        #p.join() #若不加join则变成了子进程间异步

