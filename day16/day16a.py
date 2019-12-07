'''

内置函数
'''
# s='sdfsdfsd'
# # lista=[1,2,3,4,5]
# # l2=reversed(lista)
# # sli=slice(1,4,2)
# # print(s[sli])
# # print(lista)
# for i in l2:
#     print(i)


#format()  调整输出
# print(format('test','<20'))
# print(format('test','>20'))
# print(format('test','^20'))



#  bytearray 修改字节编码
# s1=bytearray('你好',encoding='utf-8')
# print(s1)
# s1[0]=128
# print(s1)


# memoryview 将切片返回成字节 不占内存空间，但是转成字符串依然占内存空间
# str01='sdfsdfvcc'
# str02=str01[:3]
# l2=memoryview(bytes(str02,encoding='utf-8'))
# print(list(l2))


#转成
# ord 字符按照unicode转数字(可以理解成字符在unicode中的位置)
# chr 数字按照unicode转成对应字符
# ascii 入参只要实在ascii中就打印出来，不是就转换成'\uxxxx'
# print(ord('a'))
# print(ord('1'))
# print(ord('袁'))
#
# print(chr(34945))
#
# print(ascii('袁'))
# print(ascii('A'))




#all(iterable)   any(interable)
#all可迭代对象中有一个是false就是返回false
#any可迭代对象中有一个是True就是返回True
# print(all(['a','',123]))
# print(all(['a',123]))
# print(all([1,123]))
# print(all([0,123]))
#
# print(any(['',0,1]))
# print(any({'i'}))


#zip拉链  传入对象元素需要相等 如果不等则能匹配几个就匹配几个
# l=[12,14,56,55]
# l2=['a','b','c']
# l3={'k1':1,'k2':55}
# for i in zip(l,l2,l3):
#     print(i)

#filter 执行了filter之后，结果结合小于执行执行之前的个数
#filter只管筛选，并不会改变原来的值

# def is_odd(x):
#     return x%2==1
# ret=filter(is_odd,[1,2,4,5,67,7])
# print(ret)
# print(list(ret))
# rets=[i for i in [1,2,4,5,67,7] if i%2==1]
# print(rets)
#
#
# def is_str(x):
#     return type(x)==str
#
# ret01=filter(is_str,['nihao',12,'xu','yuanniu'])
# for j in ret01:
#     print(j)


#利用filter（）过滤出1-100的平方根是整数的数

#[1,4,5,16,25,36,49,64,81,100]

#import math
# def sqrt_01(x):
#     # x1=math.sqrt(x)%1
#     # if x1==0:
#     #     print(x1)
#     #     return x
#     return math.sqrt(x)%1==0
#
# # s=sqrt_01(100)
# # print(s)
# rs01=filter(sqrt_01,range(1,101))
# print(list(rs01))



#map 函数  执行前后 元素个数不变 值可能发生变化
# ret04=map(abs,[1,-9,8,-90])
# print(ret04)
# # for a in ret04:
# #     print(a)
#
# ret05=[abs(a) for a in [1,-9,8,-90]]
# print(ret05)
# print(list(ret04))



#sort和sorted区别
# sort实在元列表的基础上进行排序 不占内存
# sorted是直接重新生成一份列表 不改变原列表，占内存
# listb=[1,2,-6,-8,]
# # # listb.sort(key=abs)
# # # print(listb)
# # # listb1=[1,2,-6,-8,10]
# # # print(sorted(listb1,reverse=True,key=abs))


#列表按照每个一个元素的len排序
listc=['sdfsdf','524dsf','sdf55666666','abc']
# ret=sorted(listc,key=len)
# print(ret)


def sort_01(x):
    ret=sorted(x,key=len)
    return ret

print(sort_01(listc))
