'''


面向对象进阶


'''
# class a(object):
#     pass
#
# class b(a):
#     pass
# obj=a()
# #判断obj是不是a的实例化对象
# print(isinstance(obj,a))
# #判断b是不是a的派生类(子类)
# print(issubclass(b,a))


'''
反射：
      使用字符串类型的名字去获取类中的变量，进行操作
      name=1
      eval('print(name)')  安全隐患
      如果用反射就完美的解决了这问题，反射是操作已经在内存中存在的代码


'''
#反射对象中的属性和方法 getattr hasattr setattr delattr

# class c:
#     def func(self):
#         print('it is func')
#         return 'it func'
# a1=c()
# ret=hasattr(a1,'func')
# if ret==True:
#     print('ok')
# ret02=getattr(a1,'func')
# print(ret02())



# 反射类的属性
# 反射类的方法  classmethod   staticmethod
# class ab:
#     price=20
#     @classmethod
#     def func01(self):
#         print('ab_func01')
# # 反射类的属性
# #正常调用
# ab.price
# #反射
# print(getattr(ab,'price'))
#
# #反射类的方法  classmethod staticmethod
# #正常调用
# ab.func01()
# #反射调用
# ret=getattr(ab,'func01')
# ret()


#模块反射


#1 模块中的属性
#正常引入
# import attr_test
# print(attr_test.day)
#
# #反射
# ret1=getattr(attr_test,'day')
# print(ret1)
#
#
# # 2 模块中的方法
# #正常调用模块中的方法
# ret2=attr_test.attr_test01
# print(ret2())
#
# #反射
# ret3=getattr(attr_test,'attr_test01')
# print('ret3',ret3())

#3 内置模块也能用
import time
# time.asctime()
ret9=getattr(time,'asctime')
print(ret9())

#4 反射自己模块中的变量

# import sys
# def cap():
#     print('反射自己模块中变量')
#     return '反射自己模块中变量01'
# year=2018
# ret4=getattr(sys.modules['__main__'],'year')
# print(ret4)
# #反射自己模块中的函数
# ret5=getattr(sys.modules['__main__'],'cap')
# print(ret5())




'''
setattr 设置修改变量


delattr 删除一个变量
'''
#setattr 设置修改变量
class abc:
    def fucn02(self):
        print('hello world')
    pass

a1=abc()

setattr(abc,'name','yuan')
print(abc.name)
setattr(abc,'name','wangdazhu')
print(abc.name)
#setattr(abc,'fucn02','fucn03')
print(abc.__dict__)
ret99=getattr(abc,'fucn02')
print(ret99())
setattr(a1,'name','dndan')
print(a1.name)


#delattr 删除一个变量
# delattr(a1,'name')
# print(abc.name)
# delattr(abc,'name')
# 对象中和类中的name都被删除了 所以一定回报错下边
#print(abc.name)