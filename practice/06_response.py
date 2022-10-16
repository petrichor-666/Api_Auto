'''

@File:06_response.py
@Datetime:2022/9/24 21:03
@Author:wangt
@Desc:
'''

"""
1. 访问百度首页的接口 http://www.baidu.com ，获取以下响应数据
2. 获取响应状态码
3. 获取请求URL
4. 获取响应字符编码
5. 获取响应头数据
6. 获取文本形式的响应内容
"""
import requests
response = requests.get("http://www.baidu.com")
print(response.url, response.status_code, response.encoding, response.headers)
print(response.text)
# 设置编码
response.encoding = 'utf-8'
print("编码后的数据：", response.text)
