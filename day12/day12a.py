'''
装饰器的进阶
       1 functools.warps
       2 带参数的装饰器
       3 多个装饰装饰同一个函数

装饰器的本质 ：  闭包函数

'''

#装饰器作业三次登录

# def login_check(f):
#     def inner(**kwargs):
#         count=0
#         while count<=3:
#             res=f(**kwargs)
#             if res==True:
#                 print('login ok')
#             else:
#                 print('login not ok')
#             count+=1
#     return inner
#
#
# @login_check
# def login_test(**kwargs):
#     if kwargs['username']=='yuan' and kwargs['username']:
#         if kwargs['pwd']=='nihao':
#             print('login success')
#             return True
#     else:
#         return False
#
# login_test(username='yuan',pwd='nihao')


#   进阶版
from functools import wraps
# def login_check(f):
#     def inner(*args,**kwargs):
#         res=f(*args,**kwargs)
#         username=res[1]['username']
#         pwd=res[1]['pwd']
#         print('pwd',pwd)
#         with open('loginword',encoding='utf-8')as f1:
#             for i in f1:
#                 print(i)
#                 if username in i:
#                     if i.split(" ")[1].strip()==pwd:
#                         print('login pass')
#                         return True
#                     else:
#                         print('请输入正确密码')
#                         return False
#     return inner
#
#
# @login_check
# def login(*args,**kwargs):
#     print(args,kwargs)
#     return args,kwargs
#
#
# login(username='yuanbao',pwd='hanqing')


# 为什么 装饰器函数要 加 *打散
from functools import wraps
# def outer(*args):
#     '''
#     函数注释
#             .__doc__
#     :param args:
#     :return:
#     '''
#     print(args)
#     print(*args)
#
#     def inner(*args):
#         print('inner>>',args)
#     inner(args)
#
# outer(1,2,3,4)
# print(outer.__name__)#查看字符串格式的函数名
# print(outer.__doc__)#查看函数的注释


# from functools import wraps
# def login_check(f):
#     # functools中提供的装饰器   如果不加则实际在调用被装饰函数的时候
#     #调用的是装饰器内的闭包函数，这一点可以只用.__name__方法验证
#     #但是如果加了 就是不会影响原函数
#     @wraps(f)
#     def inner(*args,**kwargs):
#         res=f(*args,**kwargs)
#         username=res[1]['username']
#         pwd=res[1]['pwd']
#         print('pwd',pwd)
#         with open('loginword',encoding='utf-8')as f1:
#             for i in f1:
#                 print(i)
#                 if username in i:
#                     if i.split(" ")[1].strip()==pwd:
#                         print('login pass')
#                         return True
#                     else:
#                         print('请输入正确密码')
#                         return False
#     return inner
#
#
# @login_check
# def login(*args,**kwargs):
#     print(args,kwargs)
#     return args,kwargs
#
# login(username='yuanbao',pwd='hanqing')
# print(login.__name__)



'''
带参数的装饰器  
 本质是 装饰器又封装了一层外部函数 将flage穿进去 装饰器最多三层
 并没有改变装饰器的原来的调用方式

'''

import time
# FlAGE=1
# def timer_out(flag):
#     def timer(func):
#         def inner(*args,**kwargs):
#             if flag:
#                 start=time.time()
#                 ret=func(*args,**kwargs)
#                 end=time.time()
#                 print(end-start)
#                 return ret
#             else:
#                 ret=func(*args,**kwargs)
#                 print('没有执行装饰器')
#                 return ret
#         return inner
#     return timer


#以下两句基本相等
# timer=timer_out(FlAGE)
# @timer
# @timer_out(FlAGE)
# def wahah():
#     time.sleep(0.1)
#     print('wahah')
#
#
# wahah()

'''
多个装饰器装饰一个函数
书：python核心编程

如果有多个装饰器 那么就先执行最近的那个装饰器
'''

# def warper1(f):
#     def inner1():
#         print('start warper1')
#         res=f()
#         print('end inner1')
#         return res
#     return inner1
#
# def warper2(f):
#     def inner2():
#         print('start warper2')
#         res=f()
#         print('end inner2')
#         return res
#     return inner2
#
# def warper3(f):
#     def inner3():
#         print('start warper3')
#         res=f()
#         print('end inner3')
#         return res
#     return inner3
# @warper3    #f=warper(f)>>>>waper3(inner2)==inner3
# @warper2    #f=warper(f)>>>>waper2(inner1)==inner2
# @warper1    #f=warper1(f)=inner1  最先执行
# def func_01():
#     print("func_01")
#     return '多层装饰器'
#
# func_01()


#思考  如果同时使用2个装饰器 记录用户的登录情况  和  函数执行时间的先后顺序
import time
def login_time(f):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(0.1)
        res=f(*args,**kwargs)
        end=time.time()
        print(end-start)
        return res
    return inner

def login_status(f):
    def inner(*args,**kwargs):
        print('判断登录状态')
        print(args,kwargs)
        result=f(*args,**kwargs)
        username=result[1]['name']
        pwd=result[1]['pwd']
        with open('loginword',encoding='utf-8')as f1:
            for i in f1:
                if username in i:
                    listuser=i.strip().split()
                    if username==listuser[0] and pwd==listuser[1]:
                        print('login pass')
                        return True
                    else:
                        print('请检查密码')
                        return False

    return inner


@login_time
@login_status
def login(*args,**kwargs):
    print("login",args,kwargs)
    return args,kwargs

result=login(name='yuan',pwd='nihao')
print("result",result)