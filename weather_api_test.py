'''

@File:weather_api_test.py
@Datetime:2022/9/28 20:53
@Author:wangt
@Desc:
'''
import requests
from urllib import parse

base_url = "https://v0.yiketianqi.com/api"
param = {"appid": "91186593", "appsecret": "fckbO7y5", "version":"v9", "city":"北京", "unescape":"1"}
city = parse.urlencode(param).encode('utf-8')

response = requests.get(base_url,params=city)
# response.encoding = 'utf-8'
# print(response.text)
response_data = response.json()
print(response_data['city'])
print(response_data['cityid'])

# print(response_data["data"][0]["day"])
# print(response_data['data'][0]['date'])
# print(response_data['data'][0]['week'])
# print(response_data['data'][0]['wea'])
# print(response_data['data'][0]['tem'])