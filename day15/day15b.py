'''
内部函数

      1某个方法属于某个数据类型 就用 . 调用例如  list.append()
      2对于相同可hash数据的hash值在一次程序的执行过程中总是不变的
       将可hash对象转化成一串数字

'''
# def func_01():
# #     return 1
# lista=["a","b","c"]
# listb=iter(lista)
# listc=next(listb)
# listc1=next(listb)
# listc2=next(listb)
# print(listc,listc1,listc2)
# print(callable(func_01))
# print(callable(print))
# help([])


#对于相同可hash数据的hash值在一次程序的执行过程中总是不变的
#将可hash对象转化成一串数字
#dict查找算法
# print(hash('sdfslklk'))
# print(hash(("name","age")))


#print
# print('nihao',end='')#指定输出的结束符
# # print('yuan')
# # print(1,2,3,4,sep='|')#指定输出多个值之间的分隔符
# # f=open('print test','w')
# # print('print test',file=f)
# # f.close()
#打印进度条 python打印进度条模块progress Bar
import time
# for i in range(0,101,2):
#     #time.sleep(0.1)
#     char_num=i//2
#
#     pet_str='\r%s%% :%s\n'%(i,'*'*char_num)if i ==100 else '\r%s%%:%s'%(i,'*'*char_num)
#     print(pet_str,end='',flush=True)
#




#exec和eval 都可以执行 字符串的代码 eval有返回值 而exec没有
#eval只能用在你明确知道你要执行的代码是什么
#eval适合有结果的简单计算 而exec适合处理简单的流程控制
# exec('print(1+2+3+4)')
# print(eval('print(1+2+3+4)'))
# code='for i in range(0,10):print(i)'
# compile1=compile(code,'print test','exec')
# exec(compile1)


#数据类型 bool int float complex
'''
复数=实数+虚数
实数： 有理数
       无理数π
虚数：不存在的数

'''
print((complex(19+16j)))


#进制转换 返回结果 0b 0o 0x分别代表2 8 16进制
# print(bin(10))
# print(oct(10))
# print(hex(10))

print(sum([1,2,3],10))

