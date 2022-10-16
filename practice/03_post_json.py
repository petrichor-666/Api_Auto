'''

@File:03_post_json.py
@Datetime:2022/9/24 19:33
@Author:wangt
@Desc:
'''

"""
需求：
1. 请求微商城项目的登录接口，请求数据（ {"username":"admin123","password":"admin123"}） 
2. 登录接口URL：http://121.196.13.152:8080/admin/auth/login
"""
import requests

# 请求：请求为json数据类型
url = "http://121.196.13.152:8080/admin/auth/login"
data_login = {"username": "admin123", "password": "admin123"}
response = requests.post(url, json=data_login)
print(response.text)