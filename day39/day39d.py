'''

爬虫

'''

import re,time,os
from multiprocessing import Pool
from urllib.request import urlopen
import requests

def get_page(url,pattern):
    print(os.getpid())
    # respon=urlopen(url).read().decode('utf-8')
    respon=requests.get(url).content.decode('utf-8')
    print(respon)
    return pattern,respon

def reque_msg(url):
    return requests.get(url).content.decode('utf-8')

def parse_page(info):
    print(os.getpid())
    pattern,page_content=info
    print('od')
    res=re.findall(pattern,page_content)
    print('odd--',res)
    for i in res:
        dic_info={
            'index':i[0].strip(),
            'title':i[1].strip(),
            'acthor':i[2].strip(),
            'time':i[3].strip(),
        }
        print(dic_info)
def file_content(filename,pattern):
    with open(filename,'r',encoding='utf-8')as f:
        return pattern,f.read()

if __name__ == '__main__':
    '''
    如果网页中有换行符\ n 可以是用\s 匹配所有字符包含空格换行符和制表符
    '''
    regexs=r'<dd>.*?<.*?class="board-index.*?>(\d+)</i>.*?title="(.*?)".*?class="movie-item-info".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
    #regexs=r'\s<dd>\s*?\S*?<.*?\s*?.*?>(\d+)<.*?>'
    pattern1=re.compile(regexs,re.S)
    url_dic={
        'https://maoyan.com/board/7':pattern1,
    }
    p=Pool(5)
    res_l=[]
    for url,pattern in url_dic.items():
        res=p.apply_async(get_page,args=(url,pattern1),callback=parse_page)
        res_l.append(res)
    for i in res_l:
        i.get()
    #
    # # res = p.apply_async(file_content, args=('sss.html', pattern1), callback=parse_page)
    # # res_l.append(res)
    # p.close()
    # p.join()
    # print(res_l)