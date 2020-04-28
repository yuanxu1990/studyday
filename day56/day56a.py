def foo(arg,li=[]):
    li.append(arg)
    return li


list1=foo(21)
list2=foo(21,[1,])
list3=foo(28)


print(list1)
print(list2)
print(list3)
n=0
while n<10:
    n+=1
    if n==2:
        continue