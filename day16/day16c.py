

dicts={'id':0,'name':1,'age':2,'phone':3,'job':4}
def filter_01(condition):
    '''条件筛选'''
    print(condition)
    condition=condition.strip()
    if '>' in condition:
        col,val=condition.split('>')
        userinfo=get_line('userinfo')
        for info_list in userinfo:
            info_list=info_list.strip().split(',')

            if int(info_list[dicts[col]])>int(val):
               print('info-->',info_list)
               yield info_list

def views(view_lst,staff_g):
    if '*' in view_lst:
        view_lst=dicts.keys()
    '''展示对象'''
    for staff_info in staff_g:
        for i in view_lst:
            print(staff_info[dicts[i]],end=' ')
        print('')





#读取文件
def get_line(filename):
    '''读取文件'''
    with open(filename,encoding='utf-8')as f1:
        for line in f1:
            line=line.strip()
            lst=line.strip(',')
            yield lst

#get_line('userinfo')

# ret=input('>>>>>')
# ret='select name,age where age>22'
# view,condition=ret.split('where')
# print(view,condition)
# # view_list=view.split('select ')
# # view_list.pop(0)
# # print(view_list)
# view=view.replace('select','').strip()
# view_list=view.split(',')
# print(view_list,condition)
def user_inputs(content):
    print(content)
    view,condition=content.split('where')
    view=view.replace('select','').strip()
    view_list=view.split(',')
    return view_list,condition
conlist,condition=user_inputs('select name,age where age>22')
res=filter_01(condition)
views(conlist,res)