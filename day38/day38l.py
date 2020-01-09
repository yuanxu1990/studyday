'''


回调函数


'''

from multiprocessing import Pool
import os

def func1(n):

    print('in func1 %s'%n,os.getpid())
    return n*n
def func2(nn):
    print('in func2 %s' % nn,os.getpid())
    print(nn)

if __name__ == '__main__':
    p=Pool(5)
    print('主进程',os.getpid())
    #callback 回调函数  主进程中执行
    #将func1的返回值作为入参费func2  回调函数不能传参数
    for i in range(10):
        p.apply_async(func1,args=(i,),callback=func2)

    p.close()
    p.join()