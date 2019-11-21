'''
求出 1-2+3-4....99的值
'''
import time
# counts=1
# sums=0
# while counts<100:
#     if counts == 88:
#         print("countss>>", counts)
#         counts = counts + 1#若不加这一句 则counts的值一直是88死循环
#         print("countss1>>", counts)
#         continue
#     else:
#         if counts%2==1:
#             sums=sums+counts
#         else:
#             sums=sums-counts
#     counts+=1
# print(sums)

i=0
j=-1
sums=0
while i<99:
    i=i+1

    if i==88:
        continue
    else:
        j = -j
        sums=sums+i*j
    '''
    1 第一次 j=-j j=1 第二次 j=-j j=-1一次类推
    '''
print(sums)
