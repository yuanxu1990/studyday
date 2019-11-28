'''

函数
    特点：
         1 不得以关键字或则数字开头
         2 定义之后，可以在任何需要他的地方调用

    返回值 ：
           没有返回值：
           1 没有定义返回值  不写return
           2 只写return  只要函数内部执行到return 就不向下执行了结束一个函数
             注意和break的区别
           3 return None
           有返回值
            1 返回一个值 可已返回任何数据类型，只要返回就可以接受
            2 返回多个值  有多少返回值就要用多少个变量去接受或则用定义一个变量接受，那么这个变量时一个元组
                  数据拆包
            传多个参数
     站在实参的角度上：（函数调用时传入的参数）
            1 按照位置传参
            2 按照关键字传参
        @@3 混着用也可以，但是必须先按照位置传参
            再按照关键字传参（想想open函数的encoding参数以及mode参数），不能给同一个变量传多个值

     站在形参的角度上：
        位置参数：必须传，且有几个参数就传几个值

只有调用函数的时候：
      按照位置传参：  直接写参数的值
      按照关键字： 关键字=值
      @@@：调用函数传入的值必须和函数定义的参数相对应，位置参数必须在关键字参数之前，即使关键字有默认值也可以按照位置传参
定义函数的时候，
                位置参数，直接定义参数、
                默认参数，关键字参数=值
                动态参数，
                       1 必须带*号 *args是习惯性编写但只能接受位置传参
                       2 **kwargs 是习惯性编写，但是只能接受关键字参数
                       3 另类动态传参 传参的序列可以用*号打散
                顺序： 必须先定义位置参数，后定义默认参数

函数的注释：
         这个函数实现了什么功能
         参数1简介
         参数2简介
         return 返回值说明



'''
#s='sdffds'
# def my_len():  #自定义函数
#     i=0
#     for k in s:
#         i=i+1
#     print(i)
#     return i   #返回值
# my_len()
# legth=my_len()
# print(my_len())

# def retur_test():
#     I=[1,2,9,'ad','nihao','dandan']
#     for ii in I:
#         if ii=='nihao':
#             break#nihao在列表的倒数第二个 即使是break也只是跳出for循环依然回执行下边的print
#         if ii=='dandan':
#             return ii
#     print('return 和 break 的区别')
#
# test_return=retur_test()
# print(test_return)

# def func_02():
#     return 1,2#等于返回的（1,2） python解释器
#
# r1,r2=func_02()
# print(r1,r2)
#
# lista=func_02()
# print(type(lista))

# #数据拆包  dict list tuple set都可以
# name,age={'name':123,'age':222}
# print(name,age)
# # set无序 无法确定赋值给那个变量
# name1,age1={'name','age'}
# print(name1,age1)




'''
传多个参数
     站在实参的角度上：（函数调用时传入的参数）
            1 按照位置传参
            2 按照关键字传参
        @@3 混着用也可以，但是必须先按照位置传参
            再按照关键字传参（想想open函数的encoding参数以及mode参数），不能给同一个变量传多个值
     
     站在形参的角度上：
        位置参数：必须传，且有几个参数就传几个值
     
只有调用函数的时候：
      按照位置传参：  直接写参数的值
      按照关键字： 关键字=值
      @@@：调用函数传入的值必须和函数定义的参数相对应，位置参数必须在关键字参数之前，即使关键字有默认值也可以按照位置传参
定义函数的时候，
                位置参数，直接定义参数、
                默认参数，关键字参数=值
                顺序： 必须先定义位置参数，后定义默认参数
     
'''

# def my_sum(a,b=2):
#     print(a,b)
#     res=a+b
#     return res
#
# #位置传参和按照关键字传参  但是必须要先按照位置传参，
#   在定义函数入参时也必须将位置参数放在前边
# #下边的传参如果只传a 而不指定b 则回报错
# ress=my_sum(1,b=2)
# print(ress)
#
# def classmate(name,sex='man',addr='shanghai'):
#     print("{},{},{}".format(name,sex,addr))
#
# classmate('袁大宝')
# classmate('袁翰卿')
# classmate('袁淑华','women',addr='hunan')



#接收多个参数  动态参数 参数名之前必须加*号  默认是*args
# 动态传参 按照位置传参
# def sums(*args):
#     n=0
#     #b=0#b需要定义到for循环外部 如果定义到内部则回被重新赋值
#     for a in args:
#         b=a
#         n=b+n
#         #n+=a  # 这一句等于上边2句
#         print(a,b,n)
#     return n
# # print(sums(1,2,3))
# print(sums(1,2,3))
# #
# def suma(*args):
#     n=0
#     for a in args:
#
#         if isinstance(a,int) or isinstance(a,float):
#             print(a)
#             n+=a
#     return n
#
# print(suma(1,2,'abd',7,1.1))


# 动态参数 关键字传参
# def fuc_01(**kwargs):
#     print('a',kwargs)
#
# fuc_01(a=1,b=2,m=5)
# fuc_01(a=['nihao'],n=9)


# 动态传参   *args 必须在 *kwargs前边
# def func_02(*args,**kwargs):
#     print(args,kwargs)
#
#
# func_02(1,2,3,4,a=33,b='sadf',c={'a':123})

# 动态传参 最终形态  *args 必须在 *kwargs前边
# def func_03(a,*args,default=1,**kwargs):
#     print(a,args,kwargs,default)
# func_03(1,2,3,4,default=33,b='sadf',c={'a':123})

#动态传参的 另外一种传参方式
# def func_04(*args): #占在形参的角度上，给变量加上*，就是组合所有传来的值
#     print(args)
#
# lista=[1,2,5,6]
#func_04(*lista)#站在实参的角度上，给序列加上* 就是将这个序列按照顺序打散且
##a,b,c,d=*lista   无法用变量接受包含其他数据类型 且无法迭代


# def func_05(**kwargs):
#     print(kwargs)
#
# func_05()
# func_05(a=1,m=0)
# dd={'name':1,'age':88}
# func_05(**dd)
#



'''
1 函数的定义
2 函数的调用
3 函数的返回值
4 函数的参数 
        形参    位置参数  必须传值
                *args     可以接受任意多个位置参数
                默认参数（关键字参数）  可以不传
                **kwargs   可以接受任意多个关键字参数
        实参    按照位置传参 按照关键字传参
'''