import requests
from bs4 import BeautifulSoup


response=requests.get('https://www.autohome.com.cn/news/')
response.encoding='gbk'
'''
html.parser 内置的解析器 html字符串 解析成soup对象

'''
soup=BeautifulSoup(response.text,'html.parser')

#  find 找到以第一个符合标准的div
div=soup.find(name='div',attrs={'id':'auto-channel-lazyload-article'})
# print(div)
li_list=div.find_all(name='li')


for li in li_list:
    title=li.find(name='h3')
    if not title:
        continue
    p=li.find(name='p')
    a=li.find(name='a')
    print(title.text)
    print(a.attrs.get('href'))
    print(p.text)
    img=li.find(name='img')
    src=img.get('src')
    src='https:'+src
    print(src)
    #再次请求地址
    file_name=src.rsplit('/',maxsplit=1)[1]
    ret_img=requests.get(src)
    with open(file_name,'wb')as f:
        f.write(ret_img.content)