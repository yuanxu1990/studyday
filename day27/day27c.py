'''

类的内置方法
    类的内置方法 和 内置函数之间有着千丝万缕的联系
双下方法
   __str__
         object 里边有个__str__，一旦被调用，就返回调用这个方法的对象的内存地址
         __str__返回的一定是个字符串
   __repr__


   %s str() 直接打印 实际上执行的是 __str__
   %r repr() 实际上是__repr__
   repr是str的备胎，但是str不能做repr的备胎
   str(obj) 实际上是内部调用了obj.__str__方法，如果str方法有，那么它必须返回一个字符串
   如果没有__str__方法，回系按照本类 __repr__方法，再没有再找父类中的__str__
   repr() 只会找__repr__ 如果没有找父类的
'''

# class a:
#     def __str__(self):
#         return 'a'
#
# a1=a()
# print(a1) #打印一个对象的时候，就是调用a.__str__
# #a1.__str__ ---》object
# #object 里里边有个__str__ 一旦被调用，就返回调用这个方法的对象的内存地址
#
# l=[1,2,3,4]  #实例化了一个列表对象
# print(l)  #---->实际上 调用了 __str__

# class teacher:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def __str__(self):
#         return 'teacher object :%s'%self.name
#
#     def __repr__(self):
#         return str(self.__dict__)
#     def func(self):
#         return 'dddddd'
#
# wukong=teacher('aoteman',252)
# print(str(wukong))
# print(repr(wukong))
# print('%r'%wukong) #自己有__repr__ 就用自己的 如果没有 就调用父类的object


# class cla:
#     def __init__(self,name):
#         self.name=name
#         self.studen=[]
#     def __len__(self):
#         print('len1')
#         # 这个地方self.studen不是实例化对象所以不会调用自己的双下len方法，
#         # 但是如果写成len(self)就回默认调用自己的双下len方法，因为self指的是类的本身
#
#         # __len__方法是cla类的内置方法，根据继承可知，实例在调用方法的时候，会先调自己的
#         #所以在外部调用len(实例化对象) 会调自己的__len__方法
#         #但是在return的时候又了一次len方法，但是传入的是一个实例化的列表对象
#         #所以这个return的len实际上是调用list的__len__方法，list自己没有__len__方法，所以最终调用的还是object的
#         return len(self.studen)

# ps=cla('py9')
# ps.studen.append('dsf')
# ps.studen.append('dsf')
# print(len(ps))
#
# '''
__del__ 析构函数
在删除一个对象之前，进行一些收尾工作
'''
# class af:
#     def __del__(self):  #析构函数 在删除一个对象前进行一些收尾工作
#         self.f.close()
# a123=af()
# a123.f=open()  #打开文件1 在操作系统中打开一个文件 拿到文件操作符存在内存中
# del a123       #直接删除a123 等于也删除了a123.f拿到的了文件操作符，但是此时系统中的文件并没有关闭
#引用计数 python的垃圾回收机制  如果检测到下边还有地方引用a123或者类 计数+1如果没有就制程0
# 
# '''
# __call__  一个对象加() 等于执行类内部的__call__方法
#
# '''

class yu:
    def __init__(self,name):
        self.name=name

    def __call__(self):
        print('内置call方法被执行')

a=yu('ni')()