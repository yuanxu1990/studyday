'''
1 昨日回顾

   list 增 append insert extend
        删  remove pop del clear
        改  直接索引找到元素后重新赋值
        查  index for 切片
        range 有序列表 顾头不顾尾


    元组 又叫只读列表  儿子不可改  孙子可能改

    sort 默认升序排序  指定参数 reverse=True为倒叙
    reverse 反转
    join  list----->str  s.join(iterable)---> li=[1,2,3]--->si=str(li)
    split str------>list s.split(' ')
    count  list.count(' ')


'''
# lis=[2,3,'k',['qwe',20,['k',['tt',3,'1'],89],'ab','adv']]
# 讲tt改成TT
# lis[3][2][1][0]=lis[3][2][1][0].upper()
# print(lis)



'''
2 字典
  数据类型划分，可变数据类型，不可变数据类型
  不可更改数据类型： tuple bool int str     可哈希
  可变数据类型：list dict  set本身可变单内元素不可变  不可哈希  
  
  
  
  dict 的key 必须是不可变数据类型  value是任意数据类型
  优势：
     1 将字段中的key 生成哈希表  在内存中存的是数字 一一对应  二分查找 
     2 储存大量的关系型数据
  特点：
      没有顺序，只是3.5之前无序  


'''


'''
3 字典的增删改查

'''
# 查
# dic={'name':['nihao','dandan'],
#      'py9':[{'num':78,'avg_age':18,}],
#      'addr':333
# }
# print(dic.get('name'))
# print(dic['name'])

# 增
# dic['ll']=44#如果没有则添加 如果有则查找  同样可以重新赋值 更改
# print(dic)
# #若不指定值 则默认值为none  键值对存在时不做任何改变，没有才添加
# dic.setdefault('ddd')#若不指定值 则默认值为none
# print(dic)
# dic.setdefault('dddd','赋值')
# print(dic)
#两种方法的区别一定要记清楚
#dic['k1']='v1'  这中用法 如若键值对存在则更新不存在则添加
#dic.setfault('k1','v2')这种用法 如若键值对存在则不会将v2覆盖现有的值中，如果没有则添加

# 删除 pop 无论字典还是列表都有返回值 若键不存在则报错，除非指定value位None
# 删除 popitem 随机删除 3.6之后删除最后一个
# 删除  clear
# 删除列表 del 也可以指定键值删除 若键不存在则报错 也可以直接删除字典
# dic.pop('addr')
# dic.pop('addr',None)# 若加None 则不报错
# print(dic.popitem())# 返回一个元组 删除的键值对
# print(dic)
# dict.clear()清空字典
# del.dic['name']

#改  1 取值重新赋值
#改  2 update
# dic1={'name':['nihao1','dandan1'],
#      'py9':[{'num':78,'avg_age':18,}],
#       'update':'将dic1中的键值对覆盖到dic2中'

# }
# dic2={'name':['nihao','dandan'],
#      'py9':[{'num':78,'avg_age':18,}],
#      'addr':333
# }
# dic2.update(dic1)# 将dic1中的键值对 更新到dic2中 若dic2中存在相同的键则将dic1中的值更新到2中，若没有则添加
# print(dic1)
# print(dic2)


# #查  dict['key'] dict.keys() dict.values() dict.iteam() dict.get('key',default value)
#
# print(type(dic2.keys()))
# print(dic2.values())
# print(dic2.items())#返回一个元组 里边是键值对
# 循环查找
# for i in dic2:
# #     print(i)
# # for ii in dic2.keys():
# #     print(ii)
# for iii in dic2.values():
#     print(iii)
# for iiii in dic2.items():
#
# print(dic2.get('name1',None))#若键存在则返回值 不存在则返回None


'''

4 字典的嵌套
'''

# dic3={
#     'name':['alex','wusir','taibai'],
#     'py9':{
#         'time':'1213',
#         'learn_money':19800,
#         'addr':'CBD'
#     },
#     'age':21
# }
#
# dic3['age']=98
# dic3['name'].append('wangdazhu')
# dic3.get('name','default')[1]=dic3['name'][1].upper()
# dic3.get('py9').setdefault('female',6)
# dic3.get('py9')['add']='test'
# print(dic3)

#
#
# info=input("str and num")
# for i in info:
#     if i.isalpha():
#         info=info.replace(i," ")
# print(info)
# new_info=info.split()
# print(len(new_info))

#
# b=0
# info=input("str and num")
# for a in info:
#     if a.isdigit():
#         b=b+1
#         print("isdigit")
#         print(b)
# print(b)


'''str是不可变类型 不可以直接改变字符串中的元素 只能通过其他方法 间接改变值
   即使切片重新赋值 也是一个全新的字符串 与原来的字符串没有任何关系
'''
# y=0
# info3=input("str and num")
# for c in info3:
#     if c.isdigit():
#         print(c)
#         print('y>>>>',info3[y])
#         c='*'
#         print('c2',c)
#     y = y + 1
# print(info3)


# dicr={'name':['nihao','dandan'],
#      'py9':[{'num':78,'avg_age':18,}],
#      'addr':333}
# for k,v in enumerate(dicr):
#     print(k,v)
#
# ss='abcdef'
# for s1,s2 in enumerate(ss):
#     print(s1,s2)
#
# sets={'ni','mei'}
# for set1,set2 in enumerate(sets):
#     print(set1,set2)
#
# tuples=(1,2,"nihao")
# for t1,t2 in enumerate(tuples):
#     print(t1,t2)


