'''

@File:requests_basic.py
@Datetime:2022/9/27 23:51
@Author:wangt
@Desc:
'''
import requests
import json

base_url = "http://httpbin.org"

# response = requests.get(base_url+"/get")
# print(response.status_code)
#
# response2 = requests.post(base_url+"/post")
# print(response2.status_code)

# 参数传递
# 1.传递url参数
# param_data = {"user": "zxw", "passwd": "4445"}
# response = requests.get(base_url+'/get', params=param_data)
# print(response.text)

# 2.传递body参数
# form_data = {"user": "zxw", "passwd": "4445"}
# response2 = requests.post(base_url+"/post", data=form_data)
# print(response2.text)

# 3.请求头定制
# form_data = {"user": "zxw", "passwd": "4445"}
# header = {"user-agent": "Mozilla/5.0"}
# r = requests.post(base_url+"/post",data=form_data, headers=header)
# print(r.text)

# 4.cookie设置
# cookie = {"user": "41zxw"}
# r = requests.get(base_url+ "/cookies", cookies=cookie, timeout=1)       # 响应超时
# print(r.json())

# 5.获取cookie
# r = requests.get("http://www.baidu.com")
# print(r.cookies)
# print(type(r.cookies))
# for key,value in r.cookies.items():
#     print(key+":"+value)

# 6.文件上传
# file = {"file": open("zxw_logo.png","rb")}
# r = requests.post(base_url+"/post",files=file)
# print(r.text)

# 7.会话对象 ,利用session可以模拟同一个会话，不用担心cookies的问题，通常用于模拟登录成功之后的下一步操作
# s = requests.session()
# r = s.get(base_url+"/cookies/set/user/51zxw")
# print(r.text)
#
# r = s.get(base_url+"/cookies")
# print(r.text)

# 8.证书验证
# r = requests.get("https://12306.cn", verify=False)      # 将验证关掉，正常显示
# print(r.text)

# 9.代理设置
# proxies = {"http": "http://219.141.153.41:80"}  # 设置代理ip
# r = requests.get(base_url+"/get", proxies=proxies)
# print(r.text)

# 10.身份认证
# from requests.auth import HTTPBasicAuth
# from requests.auth import HTTPDigestAuth

# r = requests.get(base_url+"/basic-auth/51zxw/8888", auth=HTTPBasicAuth("51zxw","8888"))
# print(r.text)

# r2 = requests.get(base_url+"/digest-auth/auth/zxw/6666",auth=HTTPDigestAuth('zxw','6666'))
# print(r.text

# 11.流式请求
r = requests.get(base_url+"/stream/10",stream=True)
if r.encoding is None:
    r.encoding = 'utf-8'        # #如果响应内容没有设置编码，则默认设置为 utf-8

for line in r.iter_lines(decode_unicode=True):      #对响应结果进行迭代处理
    if line:
        data = json.loads(line)
        print(data['id'])