import requests



headers={}
respon_data=requests.get('https://www.syhealth.com/home/#/index')


print(respon_data.text)