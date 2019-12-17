addr={
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':
                {
                    '爱奇艺':{},
                    'youku':{},
                    '汽车之家':{},
                },
            '上地':
                {
                    '百度':{},
                }
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回笼觉':{},
        }
    },
    '上海':{
        '闵行':{
            '闵行':{
                '岱劲':'长三角电商中心',
                '七宝':'万科'
            },
            '闸北':{
                '火车占':{},
                '地铁':{}
            }
        }
    },
    '河南':{
        '郑州':{
            '河农大':'文化路',
            '河南财经大学':'东风路',
        },
        '项城':{
            '袁世凯故里':'王明口'
        }
    }
}


#递归实现 三级菜单
# print(not addr.get('北京').get('昌平').get('回笼觉'))
def threeLM(dic):
    while True:
        for k in dic:
            print(k)
        key=input('input').strip()
        if key=='b' or key=='q':
            return key
        elif key in dic.keys() and dic[key]:
            ret=threeLM(dic[key])
            if ret=='q':
                return 'q'
        elif (not dic.get(key)) or (not dic[key]):
        #elif dic.get(key)==None or dic[key]==None:
            print(123)
            continue
threeLM(addr)

#堆栈实现
# l=[addr]
# while l:
#     for key in l[-1]:
#         print(key)
#     k=input('input>>>').strip()
#     if k in l[-1].keys() and l[-1][k]:
#         l.append(l[-1][k])
#     elif k=='b':
#         l.pop()
#     if k=='q':
#         break