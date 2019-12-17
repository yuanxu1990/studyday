'''
面向对象

类是 抽象的  能知道有什么属性， 但是不能知道属性具体的值


'''

def Person(name,blood,aggr,sex):
    person={
        'name':name,
        'blood':blood,
        'aggr':aggr,
        'kind':sex
    }
    def attack(dog):
        dog['blood']-=person['aggr']
        print('%s被打了，掉了%s的血'%(dog['name'],person['aggr']))
    person['attack']=attack
    return person


def Dog(name,blood,aggr,kind):
    dog={
        'name':name,
        'blood':blood,
        'aggr':aggr,
        'kind':kind
    }
    def bite(person):
        person['blood']-=dog['aggr']
        print('%s被咬了，掉了%s的血'%(person['name'],dog['aggr']))
    dog['bite']=bite
    return dog

li=Dog('蛋蛋',100,2,'皮卡丘')

pr=Person('元宝',100,1,'儿童')
print(li['bite'](pr))
print(pr['attack'](li))

#dog函数和person函数，都是定义了以类食物
#调用函数，赋值了之后才真的有了一个实实在在的人或则狗
# def attack(person,dog):
#     '''
#     人打狗
#     :param person: 人
#     :param dog: 狗
#     :return: None
#     '''
#     dog['blood']-=person['aggr']
#     print('%s被打了，掉了%s的血'%(dog['name'],person['aggr']))
#
#
# def bite(dog,person):
#     '''
#     狗咬人
#     :param dog:
#     :param person:
#     :return:
#     '''
#     person['blood']-=dog['aggr']
#     print('%s被咬了，掉了%s的血'%(person['name'],dog['aggr']))

