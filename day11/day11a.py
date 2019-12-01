# a=10
# # # # b=20
# # # # def test_01(a,b):
# # # #     print(a,b)
# # # #
# # # #
# # # # c=test_01(b,a)
# # # # print(c)

#
# a=10
# b=20
# def test_02(a,b):
#     a=3
#     b=5
#     print(a,b)
#
# c=test_02(b,a)
# print(c)

'''

写函数，写入传入字符串中 数字 字母空格以及其他的个数 并且返回结果
'''
#
# def sum_str(s):
#     # a=0
#     # b=0
#     # c=0
#     # d=0
#     dics={'a':0,'b':0,'c':0,'d':0}
#     for i in s:
#         if i.isdigit():
#             # a+=1
#             dics['a']+=1
#         elif i.isalpha():
#             #b+=1
#             dics['b'] += 1
#         elif i.isspace():
#             #c+=1
#             dics['c'] += 1
#         else:
#             #d+=0
#             dics['d'] += 1
#     # return '{}个数字,{}个字母,{}个空格,{}个其他'.format(a,b,c,d)
#     return dics


# a=sum_str('sadf 3333')
# print(a)



# def func_01(a):
#     if type(a)==str and a:
#         for i in a:
#             if i.isspace:
#                 return True
#     if type(a)==list and a:
#
#         for ii in a:
#             if not ii:
#                 return True
#
#     if type(a)==tuple and a:
#         for iii in a:
#             if not iii:
#                 return True
#
#     if not a:
#         return True
#
#
# print(func_01([]))
#
#
# dicts={'name':55,'age':555}
# for kk in dicts:
#     print(kk)



'''
三元运算  变量=条件返回True的结果 if 条件 else 条件返回False的结果
  1 必须有结果
  2 必须要有if和else
  3 简单的条件判断
'''
# a=1
# b=5
# c=a if a>b else b
# print(c)

# def max_test(a,b):
# # #     return a if a>b else b
# # #
# # # print(max_test(3,50))


'''
写函数  ，用户传入修改的文件名和将要修改的内容 
执行函数 完成整个文件的批量修改操作
'''
def func_file(filename,old,new):
    with open(filename,encoding='utf8')as f,open('%s.bak'%filename,"w",encoding='utf-8')as f2:
        for lin in f:
            if old in lin:
                lin=lin.replace(old,new)
            f2.write(lin)
    import os
    os.remove(filename)
    os.rename('%s.bak'%filename,filename)

func_file('a123','yuan','YUAN')