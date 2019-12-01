'''

装饰器
     形成过程
     作用   不想修改函数的调用方式，但是还想在原来的函数前后添加功能
     原则 开放封闭原则
     固定模式
'''


import time

# def time_test(f):
#     start_time=time.time()
#     f()
#     end_time=time.time()
#     print(end_time-start_time)
#
# def func_01():
#     time.sleep(0.1)
#     print('装饰器')
#
# time_test(func_01)


# def timer(f):
#     #闭包函数   如果返回闭包函数的内存地址 则闭包函数引用的外部变量不回被销毁
#     def inner():
#         start=time.time()
#         print('f',f)
#         f()
#         end=time.time()
#         print(end-start)
#     print('inner',inner)
#     return inner
#
# def func():
#     time.sleep(0.1)
#     print('aaa')
#
#
# print('woshi func01',func)
# funb=timer(func)
# print('func02>>>inner>>',funb)
# funb()



'''
原则 开放封闭原则
     开放 对扩展是开放的 （对已经完成的功能进行扩展）
     封闭 对修改是封闭的（已经完成的功能不能在修改）
上边的timer就是一个装饰器，只是对一个函数有一些装饰作用
'''


'''
语法糖
'''

# def timer(f):
#     #闭包函数   如果返回闭包函数的内存地址 则闭包函数引用的外部变量不回被销毁
#     def inner(a):
#         start=time.time()
#         print('f',f)
#         ret=f(a)
#         end=time.time()
#         print(end-start)
#         return ret
#     print('inner',inner)
#     return inner
#
#
# @timer
# def func(a):
#     time.sleep(0.1)
#     print('aaa')
#     print(a)
#     return '新年好'
# #>>>>>>在加语法糖之后，
# # 实际上被装饰函数func已经作为参数传给了装饰函数，装饰函数返回
# #inner的内存地址 所以这时候的func是inner的内存地址加括号调用后
# #得到inner函数的返回值
# result=func(1)
# print(result)



'''
装饰器最终形态
'''

#
# def times(f):#times是装饰器函数名， f是被装饰的函数
#     def inner(*args,**kwargs):
#         start=time.time()
#         res=f(*args,**kwargs)
#         end=time.time()
#         print(end-start)
#         print('装饰函数')
#         return res
#     return inner
#
#
# @times
# def func_a(*args,**kwargs):
#     print('rucan',args,kwargs)
#     return args,kwargs
#
# result=func_a(['sdfsdf',444],c={'NAME':555})
# print('result',result)





# def warper(func):
#     def inner(*args,**kwargs):
#         ret=func(*args,**kwargs)
#         #ret=func()
#         return ret
#     return inner
#
# @warper
# def test(*args,**kwargs):
#     print(123)
#     return args, kwargs

# rets = test(1, 2, c=8)
# print(rets)


'''
自我扩展 
 使用语法糖  
后边默认有再一次进行了调用 
 所以装饰函数必须返回内嵌函数的内存地址 
 像str 等数据类型是无法被调用的

'''

def warpper01(f,*args,**kwargs):
    start=time.time()
    print(id(f))
    res=f(*args,**kwargs)
    end=time.time()
    print(end-start)
    print('res',res)
    return res

#@warpper01
def func_09(*args,**kwargs):
    time.sleep(0.1)
    print("aaa")
    return "123"

print('outfunc',id(func_09))
# res=func_09()
res=warpper01(func_09)
print(res)

