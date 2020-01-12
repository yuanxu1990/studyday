import copy
# lsta=['y6','y7','y8','y9','y10']
# sourcelst=['y1','y2','y3','y4','y5',lsta]
# copy_lst=copy.copy(sourcelst)
# print(sourcelst,id(sourcelst))
# print(copy_lst,id(copy_lst))
#
# sourcelst.append('y20')
# copy_lst.append('y21')
# print(sourcelst,id(sourcelst))
# print(copy_lst,id(copy_lst))
#
# sourcelst[0]='yx'
# print(sourcelst,id(sourcelst))
# print(copy_lst,id(copy_lst))
#
# lsta.append('test')
# print(sourcelst,id(sourcelst))
# print(copy_lst,id(copy_lst))
lsta=['y6','y7','y8','y9','y10']
sourcelst=['y1','y2','y3','y4','y5',lsta]
copy_lst=copy.deepcopy(sourcelst)
print(sourcelst,id(sourcelst))
print(copy_lst,id(copy_lst))


sourcelst.append('source')
copy_lst.append('copy')
print(sourcelst,id(sourcelst))
print(copy_lst,id(copy_lst))

lsta.append('lsta')
print(sourcelst,id(sourcelst))
print(copy_lst,id(copy_lst))

