import os
from multiprocessing import Process

'''
第二中开启多线程方法  
 1 自定义类 继承Process
 2 类中必须实现一个run方法，实在子进程 中使用的

'''
class my_process(Process):

    def __init__(self,a,b):
        '''
        这里要调用父类的__init__
        因为下方要实现的函数内部可能要
        调用父类的方法
        比如下方的在调用self.pid的时候实际上是
        调用父类的属性 
        :param a：
        :param b:
        '''
        super().__init__()
        self.a=a
        self.b=b
    def run(self):
        '''
        在启动子进程的时候才会执行
        :return:
        '''
        print(self.a,self.b)
        print(self.pid)
        print(self.name)
        print('子',os.getpid())


if __name__ == '__main__':

    print('主',os.getpid())
    p1=my_process(1,2)
    #p1.start 实际上在内部调用了run方法
    p1.start()
    p2=my_process(4,5)
    p2.start()