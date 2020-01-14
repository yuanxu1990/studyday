'''
实现并发的手段


进程     启动多个进程 进程之间是由操作系统负责调用
线程     启动多个线程 真正被cpu执行的最小单位实际是线程
         开启一个线程  创建一个线程 寄存器 堆栈 这些都需要时间
         关闭一个线程  需要收回 寄存器 堆栈


协程
         本质上是一个线程 ，
         能够在多任务之间切换来节省一些io时间
         协程中任务之间的切换也消耗时间，但是开销要远远小于
         进程线程之间的切换


网络io模型


'''

# def consumer():
#     while True:
#         x=yield
#         print('处理了数据',x)
# # c=consumer()
# # next(c)
# # c.send(1)
#
# def producer():
#     c=consumer()
#     next(c)
#     for i in range(10):
#         print('生产了数据',i)
#         c.send(i)
#
# producer()