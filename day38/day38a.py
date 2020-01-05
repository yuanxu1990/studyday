'''
信号量  Semaphore
      用锁的原理实现，内置了一个计数器
      在同一时间，只能有指定数量的进程执行某一段被控制住的代码
事件  Event

   通过一个信号 来控制多个进程同时执行或阻塞
   wait阻塞收到事件状态控制的同步组件
   状态 True Flase    is_set  set clear

队列   Queue  JoinableQueue
Queue
     put    当队列满的时候 阻塞 等待队列有空余的位置
     get    当队列空的时候  阻塞  等待队列有数据
     full   判断队列中是否满
     empty  判断队列是否为空


JoinableQueue
      除了拥有Queue的方法外还有
      task_done() 执行一次就像p.join发送一次
      p.join()   阻塞  直到队列中的数据被执行完


'''