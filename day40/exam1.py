import time

list3 = [
    {'name': 'alex', 'hobby': '抽烟'},
    {'name': 'alex', 'hobby': '养马'},
    {'name': 'alex', 'hobby': '喝酒'},
    {'name': 'alex', 'hobby': '烫头'},
    {'name': 'egon', 'hobby': '喊麦'},
    {'name': 'egon', 'hobby': '跳舞'},
]

list4=[{'name':'alex','hobby_list':[]}]
count=0
for item in list3:
    for dic in list4:
        if item['name'] == dic['name']:
            dic['hobby_list'].append(item['hobby'])
            break
        else:
            if count==1:
                break
            list4.append({'name':item['name'],'hobby_list':[]})
            count+=1

print(list4)

