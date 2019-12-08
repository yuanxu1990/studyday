'''

递归函数

     什么是递归函数
         在函数中调用自身函数 默认递归深度998
         py为了保护内存做的限制
         可以使用sys模块中的setrecursionlimit方法修改递归深度
          import sys
          sys.setrecursionlimit(1200)

     如果递归次数太多，就不适合使用递归来解决问题
     缺点：占内存
     优点：会让代码简单

     递   往下走 问题分析一次一次往下
     归   往上走  结果一次一次往上走
'''

#修改递归深度
# import sys
# sys.setrecursionlimit(1200)
#
# n=0
# def story():
#     global n
#     n+=1
#     print(n)
#     story()
#
# story()

#年龄递归求发

#yuan多大             n=1 age(1)=age(2)+2     age(n+1)+2
#yuan比mo大两岁
 #mo多大              n=2  age(2)=age(3)+2
#mo比wang大两岁
#wang多大             n=3  age(3)=age(4)+2
#wang比yong大两岁
#yong多大
#yong  40岁           n=4   age(4)=40

# def age_01(n):
#     if n==4:
#         return 40
#     elif n<4 and n>0:
#         return age_01(n+1)+2
#
# # ages=age_01(1)
# print(age_01(1))

#调用关系
# def age_01(1):
#     if 1==4:
#         return 40
#     elif 1<4 and 1>0:
#         return age_01(1+1)+2
# def age_01(2):
#     if 2==4:
#         return 40
#     elif 2<4 and 2>0:
#         return age_01(1+1+1)+2
# def age_01(3):
#     if 3==4:
#         return 40
#     elif 3<4 and 3>0:
#         return age_01(1+1+1+1)+2# 此时调用age(4)=40 那么就得出了age（3）=42以此类推就得出n=1的时候是多少
# def age_01(4):
#     if 4==4:
#         return 40    #返回给上一个调用的地方就是在n=3中返回结果
#     elif 4<4 and 4>0:#为假  不在执行
#         return age_01(1+1+1+1)+2

#算法  计算的方法
# 查找：找到数据
# 排序：
# 最短路径：百度地图 滴滴打车

#二分查找算法  先排序 在从中间取值对比目标
# lista=[2,3,4,5,6,55,66,77,88,99,100]
# def finds(l,aim):
#     mid_index=len(l)//2
#     if l[mid_index]<aim:
#         new_l=l[mid_index+1:]
#         finds(new_l,aim)
#     elif l[mid_index]>aim:
#         new_l=l[0:mid_index]
#         finds(new_l,aim)
#     else:
#         print('pass',mid_index,l[mid_index])
#
# finds(lista,66)

listb=[2,3,4,5,6,55,66,77,88,99,100]
def finds_01(l,aim,start=0,end=None):
    #如果这里end写成len（l）则下边递归函数再次调用的时候
    #等于给end赋值还是原长度，那么下边递归函数传值的end
    #就没有用处 在第一次调用的时候 已经肯定了end的值就是
    #列表的长度
    end=len(l) if end is None else end
    mid_index=(end-start)//2+start
    if start<=end:
        if l[mid_index]<aim:
            res1=finds_01(l,aim,start=mid_index+1,end=end)
            return res1
        elif l[mid_index]>aim:
            res2=finds_01(l,aim,start=start,end=mid_index)
            return res2
        else:
            print('找到了',mid_index,l[mid_index])
            return mid_index
    else:
        print('找不到这个值')
        return '找不到这个值1q'



s=finds_01(listb,66)
print(s)

'''
斐波那契数列  第n个斐波那契shu是多少
阶乘  3!=3*2*1
'''

