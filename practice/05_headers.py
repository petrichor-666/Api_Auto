'''

@File:05_headers.py
@Datetime:2022/9/24 19:49
@Author:wangt
@Desc:
'''

"""
需求：
1. 请求IHRM项目的登录接口，URL： http://121.196.13.152:8080/admin/auth/login
2. 请求头： Content-Type: application/json
3. 请求体： {"username":"admin123", "password":"admin123"}"""
# 1.导包
import requests

# 2.post请求,传递表单类型
url = "http://121.196.13.152:8080/admin/auth/login"
login_data = {"username": "admin123", "password": "admin123"}

headers = {"Content-Type": "application/json"}
response = requests.post(url, json=login_data, headers=headers)
print(response.text)