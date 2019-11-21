'''
1 昨日内容以及作业
   ascii  字母 数字 特殊字符 1个字节 8位
   unicode 起初无论什么英文还是中文都是16位  2个字节 后来 升级32位 四个字节
   utf-8 最少一个字节8位表示  英文字母 8位 一个字节
                               欧洲16位  2个字节
                                中文24位 3个字节
    gbk 中文2个字节，英文字母1个字节

'''


'''
列表 
   增删改查
   列表的循环
   列表的嵌套
   32位python能容5亿多的元素  64位的更多
   之所以叫 有序集合 就是因为有索引位置  和元组有什么区别？

'''
# 切片
# lista=['yuan','xy','age','addr']
# print(lista[0:3])
# print(lista[-1:-3:-1])
#
# #增加 追加 append
# lista.append('nihao')
# lista.append('add')
# print(lista)
# #增加 插入insert
# lista.insert(2,'insert')
# print(lista)
# # 增加 迭代插入 extend 入参是可迭代对象 将对象中的元素循环插入目标列表 追加到最后
# lista.extend([1,2,3,4])
# print(lista)
#
#
# #删除 pop 入参是索引值 默认删除最后一个 return被删除的元素值
# listb=['yuan','xy','age','addr']
# # print(listb.pop(2))
# print(listb)


#删除 remove 入参是元素值 value 没有返回值
# print(listb.remove('addr'))
# print(listb)

#删除 clear 清空列表
# print(listb.clear())

#删除 del list    切片删除
# del listb[0:2]
# print(listb)
#


#更改 索引变更
# listc=['nihao','bwm','aoti','yingwu']
# listc[-1]='aoteman'
# listc[-2]=[1,2,5]
# print(listc)
# #更改 切片变更
# listc[0:3]='袁旭dslkfjsd'  #拿到0:3的索引位置的值 保留后边的 然后将新传入的值迭代的传入
# print(listc)

#
# #查
# listd=['222','safd','sadf','ffgf']
# for i in listd:
#     print(i)



# hr新增人员  追加 append  插入insert
# list_hr=[]
# while 1:
#     name=input(">>>>>>>name")
#     if name.upper()=='Q':
#         break
#     else:
#         list_hr.append(name)
#
# print(list_hr)
#
#
# #公共方法
# liste=['wefwe','dfgdg','werwer','fff']

# #len 测量长度
# print(len(liste))

# #count 计算传入的值在列表中的次数
# print(liste.count('fff'))

# #index 返回传入的值在列表中的索引值 若没有则报错 没有find
# print(liste.index('fff'))

# sort排序
# listf=[2,31,44,1]
# listf01=listf.sort()
# print(listf)
# #倒叙  reversed 指定排序模式
# print(listf.sort(reverse=True))

#反转  reverse
# ni=listf.reverse()
# print("ni>>>",ni)

#列表的嵌套
# liste=['袁旭','222','dfgfd','asdf']
# name=liste[0][0]+'yyy'
# liste[0]=name
#
# liste[2]=liste[2].replace('d','g')
# print(liste)


'''
元组 tuple 可循环产讯 可切片 
  只读列表 儿子不能变 孙子可变（直属内含元素不可该变 元素内的元素可以改变）

   不可删除，不可更改，只能插入
'''

# tu=('taibai','yingwu','aoteman',["nihao",'dandan'])
# print(tu)
# tu[3][0]=tu[3][0].upper()
# print(tu)


# 公共方法  join 入参必须是可迭代对象
# ss='yuanhanqing'
# ss1='*'.join(ss)
# print(ss1)
#
# listee=['袁旭','222','dfgfd','asdf']
# ss2='--'.join(listee)
# print(ss2)

# #range
# for i in range(0,12):
#     print(i)
# for a in range(10,-1,-2):
#     print(a)
# 循环打印
# listeee=['袁旭','222','dfgfd','asdf',['袁旭','222','dfgfd','asdf']]
# for b in range(len(listeee)):
#     if type(listeee[b])==list:
#         for bb in listeee[b]:
#             print(bb)
#     else:
#         print(b)



