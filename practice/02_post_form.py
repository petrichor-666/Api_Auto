'''

@File:02_post_form.py
@Datetime:2022/9/24 19:26
@Author:wangt
@Desc:
'''
"""
需求：
1. 请求TPshop项目的登录接口，请求数据（username: 13088888888, password: 123456,verify_code: 1234） 
2. 登录接口URL：http://localhost/index.php?m=Home&c=User&a=do_login
"""
# 1.导包
import requests

# 2.post请求,传递表单类型
url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {"username": "13088888888", "password": "123456", "verify_code": "1234"}
response = requests.post(url, data=login_data)
print(response.text)