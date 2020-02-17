import requests

head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0'}
url='http://dig.chouti.com/'
post_data={
    "phone":'86'+'15518006700',
    'password':'yuanxu1989',
    'oneMonth':1
}
response=requests.get(url=url,headers=head)
r1_cookie=response.cookies.get_dict()
print(r1_cookie)


