'''

定义类：
     class 类名
     函数：方法   动态属性
     变量：类属性 静态属性
__init__方法：
      1 python帮我们创建了一个对象self={}
      2 调用类自动执行init方法,__init__方法里 默认传self  在init方法里面可以对self进行赋值
self：
     1 相当于是一个字典，内部存储数据的时候以字典存储
     2 在类的内部，self就是一个对象
        yua=Person()
        alex.walk==Person.walk(alex)
实例化
     对象=类（参数是init方法）
实例和对象没有局别

对象查看属性
      对象.属性名
对象调用方法：
      对象.方法名  类名.方法名（对象名，参数）


创建一个类就会创建一个类的名称空间，用来存储类中定义的所有名字，这些名字称为类的属性


类名.__name__# 类的名字(字符串)
类名.__doc__# 类的文档字符串
类名.__base__# 类的第一个父类(在讲继承时会讲)
类名.__bases__# 类所有父类构成的元组(在讲继承时会讲)
类名.__dict__# 类的字典属性
类名.__module__# 类定义所在的模块
类名.__class__# 实例对应的类(仅新式类中)



'''

'''
类的命名空间：
        执行文件的时候，创建一个类的命名空间
类实例化：
     类对象指针   类在实例化实际就等于又开了一个 属于实例化的命名空间 类对象指针就是表示来自于那个类
类命名空间和对象命名空间：
    变量调用顺序  
                会在对象本身的命名空间找，找不到就去类里边去找，
                 类中的静态变量，可以被对象和类调用
                但是对象更改或新增类的属性并不能更改类的属性，
                因为可能还有其他的对象调用了这个类
                如果用类来更改或则新增属性，那么引用它的对象也会
                变更或新增对应属性
                所以对于不可编数据类型来说，类变量最好用类操作
               


'''

# class coure:
#     language='Chinese'
#     pr=['niuni']
#     def __init__(self,teacher,coures_name,period,price):
#         self.teacher=teacher
#         self.coures_name=coures_name
#         self.period=period
#         self.price=price
#     def func(self):
#         print('ok')

'''
使用类来改变类内的属性，那么调用该类的对象也回变更属性
关于属性值 类不能用对象的属性，对象可以用类的   
          例如coure.name就无法知道调用的到底是py的还是linux的
          但是对象可以调用类的 比如py.language
'''
# coure.language='english'
# # coure.__dict__['language']='engish'
# print(coure.language)
# py=coure('yuan','python','60个月',998)
# print(py.__dict__)
# linux=coure('yu','linux','60个月',998)
# # print(py.language)

'''
对象修改属性，修改后只能更改自己的无法变更类的属性

会在对象本身的命名空间找，找不到就去类里边去找，
                 类中的静态变量，可以被对象和类调用
                但是对象更改或新增类的属性并不能更改类的属性，
                因为可能还有其他的对象调用了这个类
                如果用类来更改或则新增属性，那么引用它的对象也会
                变更或新增对应属性
                所以对于不可编数据类型来说，类变量最好用类操作
                单对于可变数据类型来说，就算使用对象更改也会变更
                #但是如果重新给属性赋予一个可变数据类型，则会就会像不可变数据类型那样在self中新增了了一个属性
                对于可以变数据类型来说，对象名的修改是共享的，重新赋值是独立的
'''
# py.language='edit'  # 等于在self字典中增加了键值对，这样就钓不到类中的静态变量，在查找的时候只能找到自己的
# print(py.language)
# print(py.__dict__)
# print(linux.language)
# print(coure.language)
#
# #对于可变类型来说  就算使用对象更改也回变更属性
# #对于可以变数据类型来说，对象名的修改是共享的，重新赋值是独立的
# #py.pr[0]='ossss'
# py.pr=['ssss']    #但是如果重新给属性赋予一个可变数据类型，则会就会像不可变数据类型那样在self中新增了了一个属性
# print(py.pr)
# print(coure.pr)
# print(linux.pr)



#模拟人生
# class family:
#     money=0
#     def work(self):
#         family.money+=1000
#
# mother=family()
# father=family()
# family.money+=1000
# family.money+=1000
# print(family.money)
# mother.work()
# father.work()
# print(father.money)
# print(family.money)
#


#创建一个类，每实例化一个对象就计数  最终所有的对象共享这个数据
#
# class counts:
#     count=0
#     def __init__(self):
#         counts.count+=1
#
#
# c1=counts()
# c2=counts()
# print(c1.count)
# print(c2.count)
# print(counts.count)


'''
绑定方法
     当对象调用方法时，就将本身self传入方法了，这时候就等于内部方法和外部变量形成了绑定关系
'''

# def func():pass
# print(func)
#
# class foo:
#     def func(self):
#         print('func')
# f1=foo()
# print(foo.func)#<function foo.func at 0x00000000023BBA60>
# print(f1)      #<__main__.foo object at 0x00000000023B8DA0>
# print(f1.func) #<bound method foo.func of <__main__.foo object at 0x00000000023B8DA0>>


#包  __init__
# import package----类的实例化的过程
# import time
# time.time()