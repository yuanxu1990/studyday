import requests
from multiprocessing import Pool
from urllib.request import urlopen

def open_msg(url):
    ret=urlopen(url)
    return ret.read().decode('utf-8')

def get_msg(url):
    '''
    子进程请求函数
    :param url:
    :return:
    '''
    res_msg = requests.get(url)
    if res_msg.status_code==200:
        return url,res_msg.content.decode('utf-8')
def re_msg(args):
    '''
    主进程回调函数
    :param args:
    :return:
    '''
    url,content=args
    print(url,len(content))

if __name__ == '__main__':
    url_list=[
        'http://www.cnblogs.com/',
        'http://www.baidu.com',
        'https://www.sogou.com',
        'http://www.sohu.com'
    ]
    p=Pool(5)
    for i in url_list:
        p.apply_async(get_msg,args=(i,),callback=re_msg)
    p.close()
    p.join()
