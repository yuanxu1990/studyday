'''

匿名函数
函数名=lambda 入参 ：返回值
参数可以有多个，用逗号隔开
匿名函数不管逻辑多复杂，只能写一行，且逻辑执行结束之后内荣就是返回值
返回值和正常函数一样可以是任意的数据类型
'''

# calc=lambda n:n*n
# print(calc(10))
#
# add01=lambda a,b:a+b
# print(add01(1,2))


#带有key参数的 函数 有 min max map filter sorted经常和lambda配合使用
#字典排序  max先回判断入参是什么类型 在根据类型采用对应的取值方法判断
# dic={'k1':10,'k2':100,'k3':30}
# print(max(dic,key=lambda k:dic[k]))
# lista=[1,2,3,4]
# print(max(lista,key=lambda x:lista[x-1]))
#
# listb=[3,2,100,888,999,213,1111]
# res=map(lambda x:x**2,[1,2,6,8])
# print(list(res))


#筛选列表中大于10的数字
# res1=filter(lambda n:n>10,listb)
# print(list(res1))

# d=lambda p:p*2
# t=lambda p:p*3
# x=2
# x=d(x)
# x=t(x)
# x=d(x)
# print(x)





#现有两个元组((('a'),('b')),(('c'),('d')))
# 请用python中的匿名函数成成列表[{'a':'c','b':'d'}]
# tup_01=zip((('a'),('b')),(('c'),('d')))
# print(tup_01)
#
# def func_01(tup):
#     return {tup[0]:tup[1]}
# #ret=map(func_01,tup_01)
# ret01=map(lambda tup:{tup[0]:tup[1]},tup_01)
# #print(list(ret))
# print(list(ret01))
# # for i in tup_01:
#     print(i)

def multipliers():
    return [lambda x:i*x for i in range(4)]
ret=multipliers()
print(ret)
# print([m(2) for m in multipliers()])
#
#
#
# def multipliers():
#     return (lambda x:i*x for i in range(4))
#
# print([m(2) for m in multipliers()])


