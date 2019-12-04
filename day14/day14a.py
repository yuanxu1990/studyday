# def gener():
#     for i in range(2000000):
#         yield 'dandan%s'%(i)
#
#
# g=gener()
# num=0
# while True:
#     if num<60:
#         ret=g.__next__()
#         print(ret)
#     num+=1
#     if num>60:
#         break
#
# def gener_02():
#     print(123)
#     content=yield 1
#     print("****",content)
#     print(456)
#     yield 2
#
# g_02=gener_02()
# ret=g_02.__next__()
# print(ret)
# ret=g_02.send(222)
# print(ret)


#send 获取下一个值的效果和next基本一直
#只是在获取下一个值额时候，给上一个yield的位置传递一个数据
#使用send的注意事情
    #第一次使用生成器的时候，使用next获取下一个值
    #最后一个yield不能接受外部的值


#生成器进阶  获取移动平均值
# def inits(f):
#     def inner(*args,**kwargs):
#         a=f(*args,**kwargs)
#         a.__next__()
#         return a
#     return inner
#
#
# @inits
# def average():
#     sum=0
#     count=0
#     avg=0
#     while True:
#         num=yield avg
#         sum+=num
#         count+=1
#         avg=sum/count
#
# avg_g=average()
# ret=avg_g.send(10)
# print(ret)
# ret=avg_g.send(30)
# print(ret)

# ###yield from使用方法

# def genertor():
#     a='qwertyuio'
#     b='asdfghjk'
#     for i in a:
#         yield i
#     for j in b:
#         yield j
#
# g=genertor()
# for i in g:
#     print(i)

#
# def genertor_01():
#     a = 'qwertyuio'
#     b = 'asdfghjk'
#     yield from a
#     yield from b
# ggg=genertor_01()
# for i in ggg:
#     print(i)

