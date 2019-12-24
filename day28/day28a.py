'''
item
     __getitem__
     __setitem__
     __delitem__
      支持字典增删改查   查看字典的源码  其实还是这样实现的 包括列表
      多了一种取值方法

'''

# class foo(object):
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def __getitem__(self, item):
#         if hasattr(self,item):
#             return self.__dict__[item]
#     def __setitem__(self, key, value):
#         self.__dict__[key]=value
#     def __delitem__(self, key):
#         del self.__dict__[key]
#
# f=foo('yuan',18,'man')
# print(f['name'])
# f['like']='son'
# print(f.like)                    #object原生支持
# print(f.like,f['like'])          #通过自己实现的
# print(f.__dict__)
# del f['like']
# print(f.__dict__)
#
#
# dic2=dict({'k':'v'})



# __init__初始化方法
# __new__ 构造方法 创建一个对象

# 其实在类的实例化时 是默认执行了object的__new__方法的 用于构造一个self

# class a:
#     def __init__(self):
#         self.x=1
#         print('init function')
#     def __new__(cls, *args, **kwargs):
#         print('__new__')
#         return object.__new__(a,*args,**kwargs) #这里class a并没有能实现构造的方法 所以还是需要调用object的
# b=a()

#设计模式
#23种
#__new__   单例模式
#        一个类始终只有一个实例 限制一个类从头到尾只有一个实例
#        当你之后再来实例化的时候看就用之前创建的对象

# class b:
#     __insta=False
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __new__(cls, *args, **kwargs):
#         '''
#         在外部实例化该类的时候，回执行类中的双下new方法
#         通过判断_insta的真假，返回不同的返回值，在第一次
#         实例化该类的时候，其实通过在类的内部改变了私有__insta的方法
#         当下次再实例化调用时，就返回已经变更过的私有__insta方法
#
#         '''
#         if cls.__insta:
#             return cls.__insta
#         cls.__insta=object.__new__(b)
#         return cls.__insta
# egon=b('agg',38)
# nezha=b('nazha',25)
# print(nezha)
# print(egon)
# print(nezha.name)
# print(egon.name)





# class f:
#     def __init__(self,name):
#         self.name=name
#
#     def __eq__(self, other):
#         if self.name==other.name:
#             return True
#         else:
#             return False
# yu1=f('yuan')
# yu2=f('yuan')
# print(yu1==yu2)






class h:
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
    def __hash__(self):
        return hash(self.name+self.sex)

h1=h('yu','man')
h2=h('yu','man')
print(hash(h1))
print(hash(h2))

