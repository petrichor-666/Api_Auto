'''

@File:07_json.py
@Datetime:2022/9/24 21:10
@Author:wangt
@Desc:
'''
#  访问查询天气信息的接口，并获取JSON响应数据 2). 接口地址：http://www.weather.com.cn/data/sk/101010100.html

import requests

response = requests.get("http://www.weather.com.cn/data/sk/101010100.html")
response.encoding = 'utf-8'

text = response.text
json_data = response.json()
print("获取返回的文本类型：", type(text), text)
print("获取json数据：", type(json_data), json_data)      # json 类型容易获取到python中字典的键和值
city = json_data.get("weatherinfo").get("city")
print(city)