'''
昨日回顾
    dict
        增  dict[k]=v dict.setdefault(k,v)
        删  dict.pop(k) dict.popiteam()  del dict[k] dict.clear
        改  dict[k]=new v     dict2=update(dict1)
        查  dict[k]  dict.keys()  dict.values() dict.iteams() dict.get(k,defalult=None)



作业  元素分类 大于66的数字保存在字典的key1中，小于66的所有值保存在key2中
      li=[11,22,33,44,55,66,77,88,99,90]


# li_a=[11,22,33,44,55,66,77,88,99,90]
# dicts={}
# dicts.setdefault('key1',[])
# dicts.setdefault('key2',[])
# for a in li_a:
#     if a>66:
#         dicts['key1'].append(a)
#     elif a<66:
#         dicts['key2'].append(a)
# print(dicts)



输出商品列表，用户输入序号，显示用户选中的商品，
 商品 li=['手机'，'电脑','鼠标垫','游艇']
 要求  1 页面显示序列号+商品名称（例如 1 手机）
       2 用户输入选择的商品序列号，然后打印商品名称
       3 如果用户输入的商品序列号有无，则提示输入错误
       4 当用户输入Q或q是退出程序
'''

#lib=['手机','电脑','鼠标垫','游艇']
# while 1:
#     print('一下是商品列表 1 手机,2 电脑,3 鼠标垫,4 游艇')
#     selct=input('>>>>>')
#     if selct.isdigit():
#         if int(selct) <= len(lib) + 1:
#             print('a')
#             selct=int(selct)
#             if selct==1:
#                 print(lib[selct-1])
#             elif selct==2:
#                 print(lib[selct-1])
#             elif selct==3:
#                 print(lib[selct-1])
#             elif selct==4:
#                 print(lib[selct - 1])
#     elif selct.upper()=='Q':
#         break
#     else:
#         print('输入错误')


flag=True
while flag:
        li_b01 = ['手机', '电脑', '鼠标垫', '游艇']
        for i in li_b01:
            #print(li_b01.index(i)+1,i)
            print('{}\t{}'.format(li_b01.index(i) + 1, i))
        selct = input('>>>>>')
        if selct.isdigit():
            selct = int(selct)
            if selct <= len(li_b01) + 1 and selct>0:
                if selct==1:
                    print(li_b01[selct-1])
                elif selct==2:
                    print(li_b01[selct-1])
                elif selct==3:
                    print(li_b01[selct-1])
                elif selct==4:
                    print(li_b01[selct - 1])
        elif selct.upper()=='Q':
            break
        else:
            print('输入错误')

