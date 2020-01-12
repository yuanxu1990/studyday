'''

线程中的队列
queue
'''
# 直接导入就是线程的队列，进程的需要从Processing
import queue

# q=queue.Queue(10)
# for i in range(10):
#     q.put(i)
# #q.put_nowait(1)队列满的时候回报错 而不是像put一样等待
# print(q.qsize())
# for a in range(11):
#     print(q.get())
#q.get_nowait() 队列取空的时候回报错 而不是像get一样阻塞等待

# LifeQueue  像栈  先进后出
q=queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
print(q.get())

#优先级队列  数字越小优先级越高 可以为负
# 如果存在优先级别一样 则按照值的ascii排列
q1=queue.PriorityQueue()
q1.put((20,'a'))
q1.put((10,'b'))
q1.put((30,'c'))
q1.put((10,'d'))
print(q1.get())
