'''
open 函数只能打开纯文本文件
     word 和 excel并不是纯文本文件  word是文字和一些格式 文字规则的集合  excel也是一样

'''
'''


'''

# 只读取r rb r读取的都是字符串 rb读取的都是bytes
# f= open(r'e:\ss.txt',mode='r',encoding='gbk')
# # f) = open('e:\\testopen',mode='r',encoding='gbk')
# print('文件以打开')
# # content = f.read()
# # content=f.readline()
# content=f.readlines()
# print(type(content),content[len(content)-1])
# # f.close()

#只写入 w wb a ab    a w写入的都是字符串  wb ab写入的都是bytes
# e=open('testopen',mode='ab')
# e.write(content[len(content)-1].encode('utf-8'))



#读写r+(先读后写 追加)   r+b(先读后写 )  w+(先写后读 先清除)
# import random
# randoms=str(random.randint(1,5))
#
# e=open('testopen',mode='r+',encoding='utf-8')
# print(e.read())
# e.write('r+'+randoms)
# print(e.read())
# e.close()
#
# ee=open('testopen',mode='r+b')
# print(ee.read())
# ee.write(('r+b'+randoms).encode('utf-8'))
# print(ee.read())
# ee.close()
#
# e=open('testopen',mode='w+',encoding='utf-8')
# print(e.read())
# e.write('w+111')#写入后 光标移动到文件的最后 所以后边读不到
# e.seek(0)#将光标跳入文件开始位置
# print(e.read())
# e.close()
# #


#功能详解
# 1 read 函数指定参数  读取到指定长度的字符 直接打印
# 2 seek 函数指定参数 移动光标位置（按照字节读 若恰好是中文可根据编码格式推算） 读取光标之后的字符
#         需要和read（）函数配合
# 3 tell 光标的位置 返回的是字节的 位置
# 4 readable writeable返回bool
# 5 readline读一行  readlines每一行当成列表中的一个元素添加到列表全部读完
# 6  truncate( )   参数指定截取位置 对源文件操作
# 7 with open 和 open区别  with open 不需要写close 但是open需要
s=open('testopen','r',encoding='utf-8')
# if s.readable()==False:
#     print(s.read(3))
#     #s.seek(3)
#     print(s.tell())
#     print(s.read())
# else:
#     print('readable test')
# s.truncate(2)
# for line in s:
#     print(line)
# s.close()


#先注册 在登录

