'''

常用模块一
         time
'''

import time
#sleep  time()
# time.sleep(0.1)
# #时间戳  ------float  给计算机看的
# print(time.time())  #时间戳  从1970.1.1  00：00 开始按秒计算的偏移量，
#
#
# #时间字符串 格式化时间  给人看的
#
# print(time.strftime("%Y-%m-%d %X"))  #x代表本地时间
# print(time.strftime("%Y-%m/%d %H:%M:%S"))
# print(time.strftime("%m/%d %H:%M:%S"))
# print(time.strftime("%H:%M:%S"))
# print(time.strftime("%H:%M"))
#
#
# #结构化时间-----元组   计算用的
# struct_time=time.localtime()
# print(struct_time)
# print(struct_time.tm_year)


#时间戳和结构化时间转换    字符串时间和时间戳之间不能直接转换
# t=time.time()
# print(time.localtime())# 获取本地结构化年时间
# print(time.localtime(t))#将获取的时间戳转换成结构化时间
# print(time.gmtime())# 格林威治时间
# print(time.mktime(time.localtime()))#将本地结构换时间转换成时间戳


#结构化时间和字符传时间转换   字符串时间和时间戳之间不能直接转换

#字符串时间转结构化时间
# print(time.strptime('2019-12-14','%Y-%m-%d'))
# #结构化时间转字符串时间
# print(time.strftime('%m/%d/%Y %H:%M:%S',time.localtime(1600000000)))



# asctime(结构化时间) 如果不传入参数 直接返回当前时间的格式化串
# ctime（时间戳） 如果不传参数，直接返回当前时间的格式化串
# print(time.asctime(time.localtime()))
# print(time.ctime())


'''
random 模块
'''

import random

#随机小数 random返回一个大于0且小于1之间的小数      uniform大于n小于m的小数
# print(random.random())
# print(random.uniform(1,4))
#
#
# #随机整数  randint(1,5)大于等于1且小于等于5之间的整数
# print(random.randint(1,5))
# print(random.randrange(1,10,2))#返回等于1且小于10之间的奇数，2等于是步长
#
#
# #随机选择一个返回
# print(random.choice([1,'23',[4,5]]))
# #随机选择多个返回 返回的个数为函数的第二个参数
# print(random.sample([1,'23',[4,5]],2))


#打乱列表顺序
item=[1,2,5,7,9]
random.shuffle(item)
print(item)