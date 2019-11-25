'''

str 操作总结
'''

# study_str='yuan#Hanqing*'
# 大小写操作
# print(study_str.upper())
# print(study_str.lower())
# print(study_str.title())
# print(study_str.capitalize())
# print(study_str.swapcase())
# #计数和统计
# print(len(study_str))
# print(study_str.count("u"))
# #切割和去空格（也可指定用什么去除）
# print(study_str.split('#'))
# print(study_str.strip('*'))
# #居中  填充
# print(study_str.center(30,'^'))
# ss=study_str.expandtabs(30)
# print(study_str.expandtabs(30),len(ss))
# #替换
# print(study_str.replace('*','@'))
# #格式话输出
# print('{}formart{}'.format('这是','\ttest'))
# print('{0}formart{1}'.format('这是','\ttest'))
# print('{k1}formart{k2}'.format(k1='这是',k2='\ttest'))
# #is
# print(study_str.isdigit())
# print(study_str.isalnum())
# print(study_str.isalpha())
# #查
# print(study_str.index('H'))
# print(study_str.find('y'))
# for i in study_str:
#     print(i)


'''
list的操作
'''
# study_list=[1,2,'abc','666',{'name':'yuan','add':['qinghuayuan']}]

# 增
#
# study_list.append('append test')
# study_list.insert(2,'insert test')
# study_list.extend(['tt','ss'])
# study_list.extend('yuan')
# print(study_list)

# 删除 pop是传索引 返回删除对象
# study_list.pop(0)
# #study_list.clear()
# study_list.remove('abc')
# del study_list[0:3]
# print(study_list)
#
#
# #改
# study_list[len(study_list)-1]='update test'

# 查  index 是传值返回索引位置
# print(study_list[0:len(study_list)])
# print(study_list.index('update test'))
# for k in study_list:
#     print(k)

# 公共方法 len sort reverse count
# study_sort=[100,22,88,55]
# study_sort.sort()
# print(study_sort)
# study_sort.sort(reverse=True)
# print(study_sort)
# print(len(study_sort))
# print(study_list.count('a'))

'''
dict的操作
'''
# study_dict={'name':'yuan','age':18,'addr':['xiangcheng','shagnhai']}
# 增
# print('dict add')
# study_dict['add k']='add v'
# study_dict.setdefault('dandan','baobao')
# study_dict.setdefault('yingwu',None)
# print(study_dict)

# 删 3.5之后popitem默认删除最后一个
# print('dict del')
# print(study_dict.pop('name'))
# print(study_dict.popitem())
# del study_dict['age']
# #study_dict.clear()
# print(study_dict)

# 改  k查找后重新赋值  dic1.update(dic2)
# study_dict['dandan']='choubaobao'
# study_dicta={'niu':'bi','aoteman':'tailuo'}
# print(study_dict.update(study_dicta))
# print(study_dict)

# 查
# print(study_dict['addr'])
# print(study_dict.get('addr',None))
# print(study_dict.keys())
# print(study_dict.values())
# print(study_dict.items())
#
# for k,v in study_dict.items():
#     print(k,v)
# print('--------start------')
# for kk in study_dict:
#     print(kk)
# print(len(study_dict))


'''
tuple 元组又叫只读列表  有序 可重复 不可修改 
      儿子不可改  孙子可改
'''
# study_tuple=(1,2,'abc',[1,2,3,'abd'],{'name':'yuanbao'},)
# print(type(study_tuple[len(study_tuple)-2]))
# study_tuple[len(study_tuple)-2].append('2')
# print(study_tuple.index('abc'))
# print(study_tuple)
# for ab in study_tuple:
#     print(ab)

'''
set 集合 无序 不可重复 可修改
     可以理解成 dict的key的集合
     里边的元素只能是可哈希的类型  tuple str int bool
     但是set本身是不可哈希

'''
# True=bool(1) set本身有去重效果 所以set内如果有1 则会只显示一个
# study_set={12,'adb',11,2,3,'a',True,(111,222)}
# 增 add入参是元素   update入参是可迭代对象 update循环插入
# dict的update是将一个字典中的键值对更新到另外一个字典中
# set中的是将传入的可迭代数据循环插入到set中
# study_set.add(122)
# print(study_set)
# study_set.update(['nihao','dandan'])
# print(study_set)
# study_set.update({'name':122})
# print(study_set)


# 删  list的pop是传入index dict的pop是传入k set的pop为空随机删除
# study_set.pop()
# print(study_set)
# study_set.remove(11)
# study_set.remove('adb')
# print(study_set)
# #del study_set

# 查
# for kk in study_set:
#     if type(kk)==str:
#         if 'dandan' in kk:
#             print(kk)
#     else:
#         print('buzai')


# #差集
# study_set={12,'adb',11,2,3,'a',True,(111,222),4}
# study_seta={12,'adb','a',True,(111,222),5,7}
#
# study_setb=study_set-study_seta
# print('差集',study_setb)
# 交集 两个集合的相同元素
# study_setc=study_set&study_seta
# study_setd=study_set.intersection(study_seta)
# print('交集',study_setc)
# print('交集',study_setd)
# 反交集 两个集合去除相同元素后的剩余不同元素的并集
# 反交集 返回的set是做了排序的
# study_sete=study_set^study_seta
# study_setf=study_set.symmetric_difference(study_seta)
# print('反交集',study_sete)
# print('反交集',study_setf)

# 并集
# study_setg=study_set|study_seta
# study_seth=study_set.union(study_seta)
# print('并集',study_setg)
# print('并集',study_seth)

# 子集 <
# study_seti=study_seta<study_set
# study_setj=study_seta.issubset(study_set)
# print(study_seti)
# print(study_setj)
# 超集 >
# study_setk=study_seta>study_set
# study_setl=study_seta.issuperset(study_set)
# print(study_setk)
# print(study_setl)

# 冻结集合 入参必须是可迭代对象 单可迭代对象内必须是可哈希元素
# 如果是传入的字典 则只将k放入冻结set中 v则会被舍弃
# study_setm=frozenset('name')
# study_setn=frozenset(['name','ok',('set','forzenset')])
# study_setq=frozenset({'name1':'set1','age':18})
# print(study_setm)
# print(study_setn)
# print(study_setq)
# print(type(study_setq))

# 枚举 enumerate
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

'''
文件操作
   1 open 和with open区别
      open需要手动关闭文件对象(f.close()) with open不需要
   2 只能操作纯文本文件 word excel不是纯文本，除了字体外还有颜色等一些规则
   3 readlines（）执行后自动关闭文件
'''
# 读取 r以字符串读取 rb以二进制读取 r+先读后写
# 读取之后 光标处于文件的最后 在执行read 什么也读不到 必须要seek移动光标位置
# with open('testopen','r',encoding='utf8') as f:
#     print(f.read())#read的入参int类型 元素索引位置
#     f.seek(0)#字节位置
#              # 若在r模式下重新的定位的位置不能包含一个完整中文字符则报错
#              # rb模式下则不会，因为rb模式下读的是二进制
#     print('指定读取的位置》》',f.read())

# with open('testopen','rb')as f1:
#     print(f1.read().decode('utf8'))
#     f1.seek(5)
#     print(f1.read())
#     print(f1.tell())

# with open('testopen','r',encoding='utf-8')as f2:
#     print(f2.readline())
#     print(f2.readlines()[0].replace('\t',"^").replace('\n',"%"))
# with open('testopen','rb')as f3:
#     print(f3.readline())
#     print(f3.readlines())

# 先读后写 先读后光标处于整个文件的最后 所以再写的时候就不会将以前的
#数据清空 等于追加a
# with open('testopen', 'r+', encoding='utf-8')as f1:
#     print(f1.read())
#     print(f1.write('返回写入的元素总数'))
#     print(f1.tell())

#若先写 会覆盖 并不回清空
# with open('testopen', 'r+', encoding='utf-8')as f1:
#     print(f1.write('返回写入的元素总数覆盖'))
#     print(f1.tell())
#     print(f1.read())
#     print(f1.tell())

# with open('testopen', 'rb+')as f1:
#     print(f1.write(bytes('返回写入的元素总数覆盖',encoding='utf-8')))
#     print(f1.tell())
#     f1.seek(0)
#     print(f1.read().decode('utf-8'))
#     print(f1.tell())

# with open('testopen', 'rb+')as f2:
# #     print(f2.read())
# #     print(f2.write(bytes('返回写入的元素总数覆盖',encoding='utf-8')))
# #     print(f2.tell())
# #     f2.seek(0)
# #     print(f2.read().decode('utf-8'))
# #     print(f2.tell())

#写入 w wb w+ wb+ a
# with open('testopen', 'w',encoding='utf-8')as f1:
#     print(f1.tell())
#     f1.seek(0)
#     print(f1.write('nihao'))
#     print(f1.tell())



# with open('testopen', 'wb')as f3:
#     print(f3.tell())
#     f3.seek(0)
#     print(f3.write('nihao123'.encode('utf-8')))
#     print(f3.tell())

# with open('testopen', 'w+',encoding='utf-8')as f4:
#     print(f4.write('nihao12345'))
#     print(f4.tell())
#     f4.seek(0)
#     print(f4.read())

#在w+模式下  即使是先读后写  也会先清空文件内容，然后写入，并不像r+那样覆盖
# with open('testopen', 'w+',encoding='utf-8')as f4a:
#     print(f4a.read())
#     print(f4a.write('nihao12345aa'))
#     print(f4a.tell())
#     f4a.seek(0)
#     print(f4a.read())


# with open('testopen', 'wb+')as f5:
#     print(f5.write('nihao1234566'.encode('utf-8')))
#     print(f5.tell())
#     f5.seek(0)
#     print(f5.read())


#在wb+模式下  即使是先读后写  也会先清空文件内容，然后写入，并不像rb+那样覆盖
# with open('testopen', 'wb+')as f5a:
#     print(f5a.read())
#     print(f5a.write('nihao1234566'.encode('utf-8')))
#     print(f5a.tell())
#     f5a.seek(0)
#     print(f5a.read())


# with open('testopen', 'a',encoding='utf-8')as f6a:
#     print(f6a.write('mode=a test'))
#     print(f6a.tell())

# with open('testopen', 'a+',encoding='utf-8')as f6aa:
#     print(f6aa.write('mode=a+ test'))
#     print(f6aa.tell())
#     f6aa.seek(0)
#     print(f6aa.read())

# with open('testopen', 'ab')as f6aa:
#     print(f6aa.write('mode=ab test'.encode('utf-8')))
#     print(f6aa.tell())
#
# with open('testopen', 'ab+')as f6aa:
#     print(f6aa.write('mode=ab+ test'.encode('utf-8')))
#     print(f6aa.tell())
#     f6aa.seek(0)
#     print(f6aa.read())







