# x=43
# ch='A'
# y=1
# print(x>=y and ch<'b' and y)


# k=1000
# while k>1:
#     print(k)
#     k=k/2

# kk=range(100)
# # print(list(kk[0:3]))
# print(list(kk[-2:-1]))
# print(list(kk[98:-1]))
# print(list(kk[-10:]))
#
# dicta={'name':55}
# print('n' in dicta)


#求除斐波那契数列
def fib_list(max):
    a=0
    b=1
    while max>0:
        a,b=b,a+b
        max-=1
        yield a

list_fibs=[]
for i in fib_list(40):
    list_fibs.append(i)
print(max(list_fibs),len(list_fibs))


# def fib_func01(n):
#     if n==1:
#         return [1]
#     if n==2:
#         return [1,1]
#     fibs=[1,1]
#     for i in range(2,n):
#         fibs.append(fibs[-1]+fibs[-2])
#     return fibs
# print(fib_func01(10))
