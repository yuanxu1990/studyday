

from functools import wraps
def war(f):
    @wraps(f)
    def inner(*args,**kwargs):
        print('start')
        f(args,**kwargs)
        print('end')
    return inner


@war
def foo(name):
    """

    :param name: str 类型
    :return: 打印一句化
    """
    print('hello',name)



if __name__ == '__main__':
    foo('小强')
    print(foo.__doc__)