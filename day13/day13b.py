'''

生成器与迭代器
    生成器：造出迭代器，
    生成器：本质就是迭代器,也就是说生成器的玩法起始就是迭代器的玩法
    函数内有yeild 都回被认为是生成器，打印该函数的执行结果返回生成器内存地址，并不会执行函数内代码


yeild总结：
       1 提供了一种自定义迭代器的方式
          可以在函数内使用yeild关键字，调用函数拿到的结果就是一个生成器，生成器就是迭代器
        2 yeild可以像return一样用于返回值，却别是return只能返回一次值
          而yeild可以返回多次 因为yeild可以保存函数执行的状态

'''


# def chicken():
#     print('one')
#     yield 1
#     print("two")
#     yield 2
#     print('three')
#     yield 3

# print(chicken())
# s=chicken().__iter__()
# s1=s.__next__()
# print(s1)



#  1 ss=chicken().__iter__() 拿到迭代器
#  2 触发 ss.__next__()，拿到该方法内的yield返回的值，赋值给a
#  3  周而复始，知道函数内不在有yield 取值完毕
#  4 for循环会检测到StopIteration 异常 结束循环
# ss=chicken()
# for a in ss:
#     print(a)
# print(s.__next__()

# for 循环的底层实现原理：
# def my_gen(start,end,steps=1):
#     n=start
#     while n<end:
#         yield n
#         n += steps
#
# s10=my_gen(0,10,2)
# print(s10.__next__())
# print(s10.__next__())
# print(s10.__next__())
#
# for i in range(0,10,2):
#     print(i)


'''
生成器之yeild的表达式

'''

def eat(name):
    print("%s ready to eat"%name)
    while True:
        print("1")
        food=yield
        print("%s start to eat %s"%(name,food))

dog1=eat("alex")
print(dog1)
#表达式 必须要先初始化 让函数停在yeild的位置
dog1.__next__()


#2 接下来的事情就是喂狗
#send有两方面的功能
#1 给yeild传值
# #2 同__next__一样 再次迭代
dog1.send("骨头")
# dog1.send("鱼")
