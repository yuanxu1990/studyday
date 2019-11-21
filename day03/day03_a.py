'''

数据类型

int 1,2,3用于计算
bool  True False 用于判断
str   ""  '' 用于储存少量数据，进行操作
list   [1,2,3,"他哥"，'22222',[1,2,3],{"name":"nihao"}]储存量大能达到亿万级别
dict   {“name”:"nihao"}也可以储存大量数据，关系型数据{“yuanxu”：[{"age":"18"},{"addr":"xiangcheng"}]
set     {1,2,3}
float   小数点
tuple  和列表一样用（）组成，元祖又叫只读列表
'''


'''
str  所引和切片
'''

# s='ADCDTHTYUJ4RTF'
# #索引
# s1=s[0]
# print(s1)# s1和s 没有任何关系 切片后形成一个新的字符串
#
# s2=s[0:4]
# print(s2)#顾头不顾尾  切片的特性
#
# s3=s[-2]
# print(s3)
#
# s4=s[-4:]
# print("s4>>",s4)
#
# s5=s[0:-1]
# print(s5)
#
# s6=s[0:]
# print(s6)
#
#
# s7=s[0:6:2]
# print(s7)  # 可以指定步长  若步长为负 则是倒着取



'''
str 的操作
'''
# msg='stuDy'
#
#
# # 首字母大写  capitalize
# msg1=msg.capitalize()
# print(msg1)
#
# #全部变成大写
# msg2=msg.upper()
# print(msg2)
#
#
# #全部变成小写
# msg3=msg.lower()
# print(msg3)
#
# #大小写翻转   swapcase()
# msg4=msg.swapcase()
# print(msg4)
#
#
# #标题首字母大写 title()  但是需要有间隔隔开可以是特殊字符 空格 数字也算特殊字符
# message='yuan*xu age'
# msg5=message.title()
# print(msg5)
#
#
# #居中  第一个参数指定长度 第二个指定 填充物
# msg6=message.center(20,"*")
# print(msg6)
#
#
# # 补全 默认补全8位
# message_01="yu\txuu"
# msg7=message_01.expandtabs(tabsize=8)
# print(len(msg7),msg7)
# print(len(message_01))
#
#
# #切割
# # msg7=message.split('*')
# # print(msg7)

# '''公共方法
#    字符串和 列表  都可以用
#
# '''
# #长度     len()
# #以什么什么开头  startswich() 以什么什么结尾 endswith()
# message_02="yuanxuy"
# msg8=message_02.startswith('yu')
# print(msg8)
# msg9=message_02.endswith('xu')
# print(msg9)
#
#
#
# '''
# 查找某个元素  find 返回的是
# 1元素的索引位置
# 2若查找多个则返回第一个
# 3若元素重复 则只返回找到的第一个元素的索引
# 4找不到 则返回-1
#
# 查到某个元素 也可以使用index 用法和find一样也是返回元素下标
# 但不同点是  index找不到元素 则会报错
# '''
# msg10=message_02.find('y')
# print(msg10)
# msg11=message_02.find('yu')
# print(msg11)
# msg12=message_02.find('YU')
# print(msg12)


'''
去除空格或则某一个元素 strip（） 
1只能去除首尾的
2 rstrip
3 lstrip
'''
# message_03='  dajin 0304*** '
#
# msg13=message_03.strip("*")
# msg13_a=message_03.strip()
# msg13_b=message_03.rstrip()
# msg13_c=message_03.lstrip()
# print(msg13)
# print(msg13_a)
# print(msg13_b)
# print(msg13_c)
#
# '''
# 统计count
'''

message_04='dajin 0304daijin'
msg14=message_04.count("da")
print(msg14)


# '''
# 切割  split
#      1 默认以空格分割  也可以指定分割对象
#      2  分割后结果是一个列表
#      3 一分为2
# #     '''
# message_05='*dajin*0304*daijin'
# msg15=message_05.split('*')
# print(msg15)


'''
格式化输出  format 三种方法
'''
# message_06='我叫{},今年{},爱好{}'.format('yuan','18','code')
# print(message_06)
# message_06a='我叫{0},今年{1},爱好{2},再说一遍我叫{0}'.format('yuan','18','code')
# print(message_06a)
# message_06b='我叫{name},今年{age},爱好{hobby},再说一遍我叫{name}'.format(age=18,name='yuan',hobby='code')
# print(message_06b)


'''
替换    replace  
  1 默认替换所有
  2 可以指定替换次数
'''
# message_07='yuanxudaijinyuanxudaijin'
# message_07a=message_07.replace('yuan','bao')
# print(message_07a)
# message_07b=message_07.replace('yuan','bao',1)
# print(message_07b)# 指定替换次数

'''
is系列
 1  isalnum  字符串由字母和数字组成
 2  isdigit   字符串只由数字组成
 3  isalpha   字符串只由字母组成
'''
# message_08='yuanxudaijinyuanxudaijin111'
# print(message_08.isalnum())
# print(message_08.isdigit())
# print(message_08.isalpha())
# print(message_08.isupper())
# print(message_08.islower())


'''
for循环 有限循环
'''
#
# s='fkldjlka'
# for i in s:
#     print(i)
#
# if 'kl' in s:git
#     print("kl 被包含在字符串中")
# if 'nihao' not in s:
#     print('nihao不包含在字符串中')



#bool int str的互相转化
print(bool(1))
print(bool(0))
print(int(True))
print(int(False))
print(bool(''))#空字符串 False
print(bool('ssss'))#非空字符串 True