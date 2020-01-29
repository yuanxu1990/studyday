'''
作业
 1 用map函数来处理字符串列表 把列表中所有人都变成ss例如alex_ss
 2 用filter函数处理数字列表，将列表中所有的偶数筛选出来


'''
# # 1 用map函数来处理字符串列表 把列表中所有人都变成ss例如alex_ss
# name=['alex','wupeiq','wang','yong','mei']
# print(list(map(lambda x:x+'_ss',name)))
#
# #2 用filter函数处理数字列表，将列表中所有的偶数筛选出来
# num=[1,2,3,5,6,8,10]
# print(list(filter(lambda x:x%2==0,num)))

#3一写一个20行以上的文件
#运行程序，现将内容读取的内容中，用列表储存
#模拟用户输入页码，每页5条，仅输出当前页的内容
# def file_read(filename):
#     with open(filename,encoding='utf-8')as f:
#         ret=f.readlines()
#         return ret
#
#
# def filter_num(ret_num):
#     if ret_num>0:
#         ret_num=ret_num*5-5
#         ret_con=file_read('examtest')
#         #ret=[x for x in ret_con  lambda x:x[ret_num:ret_num+5]]
#         ret=filter(lambda x:ret_con[ret_num::],ret_con)
#         return ret
#
# ret=filter_num(2)
# print(list(ret))


# with open('examtest',encoding='utf-8')as f1:
#     l=f1.readlines()
# page_num=input('页码')
# page_num=int(page_num)
# pages,mod=divmod(len(l),5)
# if mod:
#     pages+=1
# if page_num>pages or page_num<=0:
#     print('输入有误')
# elif page_num==pages and mod!=0:
#     for i in range(mod):
#         print(l[(page_num-1)*5+i].strip())
# else:
#     for i in range(5):
#         print(l[(page_num-1)*5+i].strip())



# 4 如下 每个小字典的name对应股票名字 shares对应多少股 price对应价格
# portfolio=[{'name':'IBM','shares':100,'price':91.1},
#            {'name':'AAPL','shares':50,'price':543.22},
#            {'name':'FB','shares':200,'price':21.09},
#            {'name':'HPQ','shares':35,'price':31.75},
#            {'name':'YHOO','shares':45,'price':16.35},
#            {'name':'ACME','shares':75,'price':115.65}]
# # 4.1 计算购买每只股票的的总价
# ret=map(lambda dic:{dic['name']:dic['shares']*dic['price']},portfolio)
# print(list(ret))
#
# #4.2 用filter过滤出 单价大于100的股票有那些
# ret0=filter(lambda dict:dict['price']>100,portfolio)
# print(list(ret0))