'''
迭代器和生成器
迭代器
     可迭代协议----含有iter方法的都是可迭代的
     迭代器协议-----含有next和iter的都是迭代器
     特点
         节省内存空间
         方便做个取值，一个迭代器只能取一次
生成器
     生成器函数
        含有yield函数的都是生成器函数
        特点：
            调用之后函数内代码不执行，返回生辰器
            每从生成器中取一个值就会执行一段代码，遇到yield就会停止
            从生成器中取值：
              for 没有break自动取完
              next每次只能取一个
              send  不能用在第一个，取下一个值的时候给上个位置传一个新的值
              数据类型的强制转换 回一次性把所有的数据都读到内存里
               g=genertor()
               g1=list(g)
               print(g1)
'''




'''
3 处理文件，用户指定要查找的文件和内容，
将文件中包含要产找内容的每一行都输出到屏幕

# '''
# def file_check(*args):
#    with open(args[0],encoding='utf-8')as f1:
#        for line in f1:
#            if args[1] in line:
#                yield line
#
# g=file_check('gentest','yuan')
# for i in g:
#     print(i.strip())



'''

4 写生成器，从文件中读取内容，
在每一次读取到的内容之前加上 ‘***’之后在返回给用户
'''
# def file_check1(*args):
#    with open(args[0],encoding='utf-8')as f1:
#        for line in f1:
#            yield '***'+line
#
# g1=file_check1('gentest')
# for j in g1:
#     print(j.strip())




'''
面试题

    特别注意的是   生成器的惰性运算 
'''
# def demo():
#     for i in range(4):
#         yield i
# g=demo()
# g1=(i for i in g)
# g2=(i for i in g1)
# #print(list(g1))# 在调用list的方法的时候实际上底层执行了for循环对g1了取值了
# print(list(g2))
# #如果先执行list（g2）  如果先执行g2  则先去G2先去找g1要值 则g1变空了
# print(list(g1))





def adds(n,i):
    return n+i

def test():
    for i in range(4):
        yield i
g1=test()
for n in [1,10]:
    #n在等于1的时候g1 就被重新赋值了 g1=(adds(n,i) for i in test())
    #n在等于10的时候 g1再次被赋值    g1=(adds(n,i) for i in (adds(n,i) for i in g1))
    g1=(adds(n,i) for i in g1)

print(list(g1))
'''
n=1      
g1=(adds(n,i) for i in g1)    右端的g1等于test()   而右端的g1是重新赋值即g1=(adds(n,i) for i in test())
n=10
因为在n=1的时候g1已经被赋值g1=(adds(n,i) for i in g1）
g1=(adds(n,i) for i in g1)    右端的g1在n=1的时候已经被重新赋值  所以左端的g1=(adds(n,i) for i in (adds(n,i) for i in g1))
这里并没有g3 g3实际上还是赋值给了g2 只是为了容易区分 实际上此时 等于g3=(adds(n,i) for i in (adds(n,i) for i in g1))
                                                                        g3=(adds(n,i)for i in [10,11,12,13])
                                                                        g3=[20,21,22,23]----------->>>  此时n已经等于10

'''

# def mult():
#     return [lambda x:x*i for i in range(4)]
#
# print([m(2) for m in mult()])

'''
上述函数中  最关键的是 mult函数返回值的问题  
        1 mult函数返回的是列表 而列表内是列表表达式 所以lambda函数就是返回元素
        2 mult返回值实际上就等于
            [lambda x:x*i] i=0
            [lambda x:x*i,lambda x:x*i] i=1
            [lambda x:x*i,lambda x:x*i,lambda x:x*i] i=2
            [lambda x:x*i,lambda x:x*i,lambda x:x*i,lambda x:x*i] i=3
            此时lambda函数并没有发生调用，所以元素就等于
            [lambda x:x*3,lambda x:x*3,lambda x:x*3,lambda x:x*3]
            
        3 下方 [m(2) for m in mult()]  实际上也是个列表表达式
           实际上等于[m(2) for m in [lambda x:x*3,lambda x:x*3,lambda x:x*3,lambda x:x*3]
           在使用for 循环第一次遍历列表的时候  m=lambda x:x*3 ----->m(2)就等于lambda 2:2*3 所以m(2)=6
           
        4 若想达到预期效果 只需要将mult的返回值变成 生成器 那么 m(2) for m in mult() 每调一次就回使上方的range函数返回一次
        就可以实现结果变成0,2,4,6   如下方函数实例
'''
# def mult_01():
#     return (lambda x:x*i for i in range(4))
#
# print([m(2) for m in mult_01()])
