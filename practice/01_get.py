'''

@File:01_get.py
@Datetime:2022/9/24 19:18
@Author:wangt
@Desc:
'''

# 1.导包
import requests
# 2.请求百度
response = requests.get("http://www.baidu.com")
print(response.text)

