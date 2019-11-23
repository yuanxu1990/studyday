'''
集合
    集合是无序的 不重复的数据集合，
   它里边的元素是可哈希的不可变类型
   但是集合本身是不可哈希的

'''

# sets=set({1,2,3,})
# setss={1,2,3,4,4}
# print(type(sets),sets)
# print(type(setss),setss)
#
# # 增 add  只能是不可更改的数据类型 str int bool
# set1={'nihao','dddd','set add'}
# set1.add('aaa')
# print(set1)
# # 增 update  循环添加
# set1.update('yuxa')
# print(set1)


#删除  pop 随机删除 有返回值
#删除  remove  按照元素删除 若没有则报错
#clear  del
# print(set1.pop())
# print(set1.remove('u'))
# print(set1.clear())
# del set1

#查 for
# for i in set1:
#     print(i)


# #求交集 反交集 差集
# set5={1,2,3,4,5,7,8}
# set6={0,'ni',3,4,5,}
# print(set5 & set6)
# print(set5.intersection(set6))
#
# print(set5 ^ set6)
# print(set5.symmetric_difference(set6))
#
# # 除去和set6交集  set5独有的就是差集
# print(set5-set6)
# #
#
# #求并集
# set7={1,2,3,4,5,7,8}
# set8={0,'ni',3,4,5,}
# print(set7|set8)
# print(set7.union(set8))

#子集和超集

# set9={1,2,3}
# set0={1,2,3,4,5,6}
# print(set9<set0)
# print(set9.issubset(set0)) # 这两个相同，都是说明set1是set2子集
#
# print(set0>set9)
# print(set0.issuperset(set9))#这两个相同，就是说明set0是set9的超集



#将集合变成不可变 数据类型
# s=frozenset('yuanx')
# print(s,type(s))