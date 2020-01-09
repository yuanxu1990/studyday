'''
管道



数据的共享  Manager dict list




进程池
      1 节省内存 节省创建多个进程系统所花费的时间
      2 cpu个数或cpu个数+1
      3  ret=map(func,iterable)
          异步 自带close和join
          返回值  所有结果的[]
      4 apply
            同步的  只有当func执行完之后，才会继续向下执行其他代码
            ret=apply(func,args=())
            返回值  就是func的return

      5 apply_async
         异步的  当func被注册进入一个进程之后，程序就继续向下执行
         apply_async(funcname,args=())
         返回值  apply_async返回的对象obj
                 为了用户能从获取func的返回值obj.get()
         get回阻塞直到对应的func执行完毕后拿到结果
         使用apply_async给进程池分配任务，需要先close后join来保持多进程和主进程代码的同步性，可视情况为定



'''