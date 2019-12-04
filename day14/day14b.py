'''

生成器表达式和列表推倒式
#括号不一样
#返回值不一样


列表推倒式
[每一个元素或则和元素相关的操作 for元素 in 可迭代数据类型] 遍历后挨个处理
[满足条件的元素相关的操作 for 元素 in 可迭代对象 if 元素相关的条件] 筛选条件

'''

#列表推倒式  最前边放想要放到列表的值 后边跟for循环

# egg_list=['鸡蛋%s'%i for i in range(10)]
# print(egg_list)


# #生成器表达式
# g_03=(i for i in range(10))
# print(g_03)
# for i in g_03:
#     print(i)



#10内数字的平方列表
# g_04=(i*i for i in range(10))
# #g_04=(i*i for i in range(10))并没有直接执行，是下方的for循环开始后才调用.__next__方法的
# for i in g_04:
#     print(i)

#30以内能被3整除的数
# lista=[i for i in range(30) if i%3==0]
# print(lista)
#
# #30以内能被3整除的数的平方
# listb=[ii*ii for ii in range(30) if ii%3==0]
# print(listb)


#查找嵌套列表内 含有2个e字母的元素
# names=[['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe'],['Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']]
#
# ret=[name for lst in names for name in lst if name.count('e')==2]
# print(ret)



#字典推倒式

# dict_01={'a':10,'b':34}
# dict_02={dict_01[k]:k for k in dict_01}
# print(dict_02)

#合并大小写对应的value值 将k统一成小写
# dict_03={'a':10,'b':34,'A':7,'Z':3}
# dict_04={k.lower():dict_03.get(k.lower(),0)+dict_03.get(k.upper(),0) for k in dict_03}
# print(dict_04)




#集合推倒式
# set_01={x**2 for x in [1,-1,2]}
# print(set_01)