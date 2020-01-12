'''
1 常用字符串格式化有那些？病说明他们的区别
format 直接调用函数
%s 语法糖
%r

2 请写出 元组 列表 字典 集合的定义方法

3 利用python打印前一天的本地时间，格式‘2018-01-30’（面试题）
时间戳-（60*60*24）----转化成格式化时间

4 python re search（）和 match()的区别
同样都只匹配一个
search 根据正则匹配符合条件的第一个
match  根据正则 从头开始匹配


5  说明是lambda函数，有说明好处
匿名函数  语义简单，
可以和max min fiddler map等配合使用，较少冗余的代码


6 说明__init__  __new__的作用
__init__  初始化方法  类在实例化的初始化方法  self
__new__   构造方法    在实例化化类的对象    默认参数cls
__del__    析构方法    在删除一个类之前调用的方法


7 简述反射
用字符串数据类型的变量名或者函数名来盗用对应的属性
A.b     getattr(A,'b')

8解释python中深拷贝和浅拷贝的区别
python使用引用语义 变量对应的是值的内存地址
浅拷贝就是拷贝一层：
     只是重新开辟一块空间来copy第一层的数据（内存地址）


深拷贝就是拷贝到最后一层  ：
    不管一个数据类型有多少层，
    都另外开辟新的空间来储存一分和原来一模一样的数据

9 用最简洁的方式生成这样一个列表【4,16,32,64,128】
lsta=[pow(2,i) for i in range(2,8) if i!=3 ]


10 python如何实现随机数并打印，默认的随机数范围是多少

random.random   0-1
random.randit

11 新式类和经典类的区别
  1 新式类如果没有继承就默认继承object类
  2 新式类内的方法 self非必须传
  3 在继承过程中 新式类 是广度优先 内置mro方法来表示广度优先的继承顺序
     而经典类是深度优先


12 装饰器什么时候被执行
被装饰函数被调用的时候
在加载函数的时候被执行

13 什么是并发？  什么是并行？
并发：
     python 多线程就是并发 在同一时间，只能有一个cpu在处理任务
       gil锁在同一时刻限制了多个线程 只能有一个线程被cpu执行
       单cpu时间片轮转很快 给人的感觉是并行

并行 ：
     python 多进程就是并行
    是真正意义上的在同一时刻有多个cpu在同时处理任务
    多个进程在同一时刻可以占用多个cpu

14  以个人理解描述Event的执行原理

  事件  通过一个状态信号决定进程或线程的阻塞
        有一个状态控制 wait方法是否阻塞
        事件的状态控制 wait方式是否阻塞


15  什么是黏包，如何避免
    基于tcp协议面向流的传输因为无法感知数据的长度 导致数据错乱
    基于tcp协议面向流的传输，数据是无界限的

如何避免
      先发送文件的长度给接受端 让接受端按照长度接受
       自定义协议 struct模块  现将任意长度的数据转成固定的4为长度的字节
       现将文件的长度给接收端

16  什么是进程
  资源单位
  运行中的程序，是最小的资源分配单位，为多个任务之间的数据安全和内存隔离做约束


17  什么是线程
  执行单位
  cpu调度的最小单位，可是说是轻量级的进程
  是进程的一部分，在多个线程之间共享数据


18  简述你对管道。队列的理解
    在多进程中开启一条数据通讯的通道，但是如果不配合锁的使用 管道容易引起数据安全问题
    队列 就是管道加锁，先进先出

     管道
         双系那个通信的数据容器，在多进程的ipc中用到，数据不安全
     队列
         先进先出，基于管道和锁实现的一个数据在线程\进程之间安全的容器




19  编程   写一个装饰器实现功能，打印程序的运行时间


20  读一下代码，写出答案 并简述原因
def f(x,l=[])
    for i in range(x)
         l.append(i*i)
    print l
f(2)         [0,1]
f(3,[3,2,1])  [3,2,1,0,1,4]
f(3)           [0,1,0,1,4]


21  使用python简单打印九九乘法表

for a in range(1,10):
    for b in range(a,10):
        c=a+b
        print('%d+%d=%d'%(a,b,c),end=' ')
    print('')


22 简述python gil的概念，以及他对python多线程的影响
  gil  python的全局解释器锁，限定同一时刻只能有一个线程去访问cpu
  影响了效率 但是提高了数据的安全

  GIL 全局解释器锁
  属于Cpython解释器
  用来在Cpython解释器解释一段多线程的代码时，约束线程在同一时刻只
  能有一个线程访问cpu
  它对python多线程的影响，在Cpython解释器下启动的多线程并不能真正实现并行


23  写一个到单例模式




24 将list3的格式转换成list4格式
   list3=[
         {'name':'alex','hobby':'抽烟'},
         {'name':'alex','hobby':'养马'},
         {'name':'alex','hobby':'喝酒'},
         {'name':'alex','hobby':'烫头'},
         {'name':'egon','hobby':'喊麦'},
         {'name':'egon','hobby':'跳舞'},

   ]

    list4=[
    {'name':'alex','hobby_list':['抽烟','养马','喝酒','烫头']},
    {'name':'egon','hobby_list':['喊麦','跳舞']}

    ]



25
一
    定义一个学生类，有下面的类属性
      1 姓名
      2年龄
       3成绩（语文，数学，英语，）每科成绩的类型为整数
    类方法：
       1 获取学生的姓名 get_name() 返回类型str
       2 获取学生的年龄 get_age()   返回类型int
       3 返回3门科目中最高的分数 get_course() 返回类型int

       zm=Studen('zhangming',20,[69,88,100])


26 写一个socket客户端和服务端进行通讯

27 什么是异步，什么是异步阻塞
在同一时间可以同时做两件事情  表现 子进程启动后，主进程执行主进程代码，子进程去执行自己的代码，个只执行自己的

在同一时刻在各自的线程中，存在io操作

28  写一个程序，包含10个线程，子线程必须等待sleep10秒后才执行，并打印当前时间
定时器

29  你了解的锁有那些
  互斥锁
   在同一个线程或进程之间，当有2个acquire的时候，就会产生阻塞，死锁


   递归锁
     在同一个线程或者进程之间，无论acquire多少次都不回产生阻塞，但是acquire次数必须和release次数对应
30 thread.RLock  threading.Lock的区别

'''
# list3 = [
#     {'name': 'alex', 'hobby': '抽烟'},
#     {'name': 'alex', 'hobby': '养马'},
#     {'name': 'alex', 'hobby': '喝酒'},
#     {'name': 'alex', 'hobby': '烫头'},
#     {'name': 'egon', 'hobby': '喊麦'},
#     {'name': 'egon', 'hobby': '跳舞'},
# ]
# list4=[]
# dic1={}
# dic2={}
# for a in list3:
#     if a['name']=='alex':
#         dic1.setdefault('name', 'alex')
#         dic1.setdefault('hobby_list', [])
#         dic1['hobby_list'].append(a['hobby'])
#     if a['name']=='egon':
#         dic2.setdefault('name', 'egon')
#         dic2.setdefault('hobby_list', [])
#         dic2['hobby_list'].append(a['hobby'])
# list4.append(dic1)
# list4.append(dic2)
# print(list4)
# list3 = [
#     {'name': 'alex', 'hobby': '抽烟'},
#     {'name': 'alex', 'hobby': '养马'},
#     {'name': 'alex', 'hobby': '喝酒'},
#     {'name': 'alex', 'hobby': '烫头'},
#     {'name': 'egon', 'hobby': '喊麦'},
#     {'name': 'egon', 'hobby': '跳舞'},
# ]
# count=0
# list4=[{'name':'alex','hobby_list':[],},{'name':'egon','hobby_list':[],}]
# for item in list3:
#     for dic in list4:
#         if item['name']==dic['name']:
#             dic['hobby_list'].append(item['hobby'])
#             break
#
#         else:
#             count+=1
#             list4.append({'name':item['name'],'hobby_list':[item['hobby']]})
#             print(count)
#
# print(list4)
# for a in range(10):
#     for b in range(10):
#         if a==5:
#             break
#         print(a,b)



# list4 = [
#     {'name': 'alex', 'hobby_list': ['抽烟', '养马', '喝酒', '烫头']},
#     {'name': 'egon', 'hobby_list': ['喊麦', '跳舞']}
#
# ]