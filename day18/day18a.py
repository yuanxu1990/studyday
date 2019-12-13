'''


超过最大递归限制的报错
只要写递归函数 必须要有结束条件

返回值问题
    1递归深度
    2不要只看到return就认为已经反悔了，
      要看返回操作实在递归到第基层的时候发生，
      然后返回给了谁
      如果不是返回给最外层函数，调用者就接受不到
      需要再分析，看如何把结果返回回来
'''


def fab_num(x):
    if x<=2:
        return 1
    elif x>2:
        return fab_num(x-2)+fab_num(x-1)

print(fab_num(4))

def fab_num01(n,l=[0]):
    l[0]+=1
    if n<=2:
        l[0]-=1
        return 1,1
    else:
        a,b=fab_num01(n-1)
        l[0]-=1
        if l[0]==0:
            return a+b
        return b,a+b
print(fab_num01(4))