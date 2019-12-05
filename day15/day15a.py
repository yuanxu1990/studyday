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
g=test()
for n in [1,10]:
    g=(adds(n,i) for i in g)

print(list(g))
"""
n=1
g=(adds(n,i) for i in test())>>>>>>实际上n=1的时候没有被执行
n=10
g=(adds(n,i) for i in adds(n,i) for i in test() )实际上n=10也没有被执行但是此时n=10了
print(list(g))此时上边两句才会被执行 但是注意此时n已经等于了10

同理
for n in [1,20,5]
    g=(add(n,i) for i in g)

n=1
g=(adds(n,i) for i in test())
n=10
g=(adds(n,i) for i in (adds(n,i) for i in test()) )
n=5
g=(add(n,i) for i in ( add(n,i) for i in (add(n,i) for i in test()) ) )
print(list(g))  最后打印结果   [15,16,17,18]

"""

