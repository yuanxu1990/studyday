'''
常用模块一
  collections模块  python中的扩展数据类型
  time模块      时间模块
  random模块   随机数模块
  os模块       和操作系统打交道模块
  sys模块       和python解释器打交道
  序列化模块    python中的数据类型和str转换的模块

'''




'''
python中的默认数据类型
list tuple
dict
set frozenset
str


堆栈 python中没有这个数据类型 特点 先进后出 后进先出
队列 先进先出  


collections
    1 namedtuple    生成可以使用名字来访问元素内容的tuple
    2 deque         双端队列，可以快速的从另外一侧追加和推出对象
    3 Counter       计数器 主要用来技术
    4 OrderedDict   有序字典
    5 defaultdict    带有默认值的字典
'''
from collections import namedtuple,deque,OrderedDict,defaultdict,Counter
# #obj=namedtuple(name,list)  list列表中的参数需要和调用该方法的参数位置和数量对等
# point=namedtuple('point',['x','y'])
# p=point(1,2)
# print(p.x)
# print(p.y)
# print(p)

#花色和数字
# card=namedtuple('card',['suits','number'])
# c1=card('红桃',2)
# print(c1)
# print(c1.suits)
# print(c1.number)


#deque  使用list存储数据的时，按索引访问元素很快，
#       但是插入和删除元素就很慢了，因为list是线性存储，
#       数据量大的时候，插入和删除效率就很低
#deque  是为了高效实现插入和删除操作的双向列表，适合与队列和栈
# import queue
# q=queue.Queue()
# q.put(5)
# q.put(6)
# q.put(7)
#
# #qsize 查看队列中的长度是多少
# print(q.qsize())
# print(q.get())
# print(q.get())
# print(q.get())
# # 若队列中已经被取空 则回被阻塞
# print(q.get())  #阻塞

#deque 双端队列  可以从两端存或则取
# q=deque([1,2])
# q.append('a')   #从后边放数据   [1,2,a]
# q.appendleft('b')  #左边放数据  [b,1,2,a]
# print(q.pop())          #从右边删 a
# q.popleft()      # 从左边删 b


#OrderedDict
# d=dict([('a',1),('b',2),('c',3)])
# print(d)   #dict的key是无序的
# od=OrderedDict([('a',1),('b',2),('c',3)]) #orderedDict 中的key是有序的
# print(od)
# print(od['a'])
# for i in od:
#     print(i)


#defaultdict
values=[11,22,33,44,66,77,88]
my_dict=defaultdict(list)  #参数内必须是可调用的数据类型 可传入 list set等
my_dict01=defaultdict(lambda :5)
for value in values:
    if value>66:
        my_dict['k1'].append(value)
    else:
        my_dict['k2'].append(value)
print(my_dict,my_dict01)





#Counter类 的目的是用来跟踪值出现的次数，它是一个无序的容器类型，以字典的键值对形式存储，其中元素做为key
#其计数作为value，计数值可以是任意的interger（包括0和负数）。counter和其他语言的bags或multisets很相似

# c=Counter('asdfvfkldjklfjl')
# print(c)
# print(c.get('a'))
# print(c['f'])