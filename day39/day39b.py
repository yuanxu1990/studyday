'''
回调函数
  应用场景  爬虫
              花费的时间主要在网络延时 处理数据的时间其实很短 如果处理数据也要在子进程中做那么效率回比较低
              因为 如果不处理完就回一直占用进程池中的进程
              如果使用回调函数在主进程中去做，整体的效率就回提升
              首先 访问一个网址
              将这些数据从网址上下载下来
              数据就是bytes转成字符串
              处理字符串
'''

from multiprocessing import Pool

def func1(n):
    return n+2

def func2(m):
    print(m)

if __name__ == '__main__':
    p=Pool(5)
    for i in range(10,20):
        p.apply_async(func1,args=(i,),callback=func2)
    p.close()
    p.join()