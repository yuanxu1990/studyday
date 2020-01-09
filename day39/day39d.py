'''

爬虫

'''

import re
from multiprocessing import Pool
from urllib.request import urlopen

def get_page(url,pattern):
    respon=urlopen(url).read().decode('utf-8')
    return pattern,respon

def parse_page(info):
    pattern,page_content=info
    res=re.findall(pattern,page_content)
    for i in res:
        dic_info={
            'index':i[0].strip(),
            'title':i[1].strip(),
            'acthor':i[2].strip(),
            'time':i[3].strip(),
        }
        print(dic_info)
def file_content(filename):
    with open(filename,'r',encoding='utf-8')as f:
        return f.read()

if __name__ == '__main__':
    '''
    如果网页中有换行符\ n 可以是用\s 匹配所有字符包含空格换行符和制表符
    '''
    #regexs=r'<dd>.*?<.*?class="board=index.*?">(\d+)</i>.*?title="(.*?)".*?class="movie-item-info".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
    regexs=r'\s<dd>\s*?\S*?<.*?\s*?.*?>(\d+)<.*?>'
    msg_str=file_content('ss.txt')
    print(type(msg_str))
    #print(msg_str.strip(',').strip('\n'))
    re_msg = re.findall(regexs, msg_str)
    print(re_msg)

    # pattern1=re.compile(regex,re.S)
    # url_dic={
    #     'http://maoyan.com/board/7':pattern1,
    # }
    # p=Pool(5)
    # res_l=[]
    # for url,pattern in url_dic.items():
    #     res=p.apply_async(get_page,args=(url,pattern),callback=parse_page)
    #     res_l.append(res)
    # for i in res_l:
    #     i.get()