'''

@File:phpwind_index.py
@Datetime:2022/9/28 23:59
@Author:wangt
@Desc:
'''
import requests
from urllib import parse
import time

# 1.验证首页接口用例
base_url = "http://43.226.74.244/phpwind/index.php"
session = requests.session()        # 将请求统统放在一个会话session中，就不需要在每次输入cookie
response = session.get(base_url)
# print(response.text)
if "Powered" in response.text:
    print("用例1：验证首页接口成功")
# s9R_lastvisit = response.cookies["s9R_lastvisit"]
# s9R_visitor = response.cookies["s9R_visitor"]
csrf_token = response.cookies["csrf_token"]     # 从首页接口响应中获取csrf_token鉴权码

# 2.检查用户名接口用例
headers = {                     # 此接口必传参数headers
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With":"XMLHttpRequest"
}
params = {                       # 必传参数
    "username":"chen123",
          "csrf_token":csrf_token
}
response2 = session.post(base_url+"?m=u&c=login&a=checkname",data=params, headers=headers)
# print(response2.text)
res = response2.json()
if res["state"] == "success":
    print("用例2：检查用户名用例成功")

# 3.登录接口用例
headers = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest"
}
params = {
    "username": "chen123",
    "password": "chen123",
    "csrf_token":csrf_token
    # "backurl": "http://47.107.116.139/phpwind/"
}
response3 = session.post(base_url+"?m=u&c=login&a=dorun",data=params,headers=headers)
res3 = response3.json()
if res3["state"] == "success":
    print("用例3：验证登录接口用例成功")

# 4.验证重定向referer接口地址
referer = res3["referer"]
referer_url = parse.unquote(referer)      # 转义url
# print(referer_url)
response4 = session.get(referer_url)
# print(response4.text)
if "Powered" in response4.text:
    print("用例4：验证重定向首页接口成功")

# 5.验证发帖接口
now = time.strftime('%Y-%m-%d %H_%M_%S')
params = {
    "fid": "2",
    "atc_title": f"发帖test{now}",
    "atc_content": f"{now}发帖test",
    "csrf_token": csrf_token,
    "reply_notice": "1",
    "special": "default",
}
response5 = session.post(base_url+'?c=post&a=doadd&_json=1&fid=2',data=params)
# print(response5.text)
res5 = response5.json()
# res5_str = parse.unquote(str(res5))
# print(res5_str)
referer = res5["referer"]
referer_url = parse.unquote(referer)      # 转义url
# print(referer_url)
tid = referer_url[42:45]            # 切片获取refer_url中 tid的值
# print(tid)
if res5["state"] == "success":
    print("用例5：验证发帖接口用例成功")
time.sleep(3.1)

# 6.验证回帖接口
params = {
    "atc_content": f"{now}回帖test",
    "csrf_token": csrf_token,
    "tid": int(str(tid))
}
response6 = session.post(base_url+'?c=post&a=doadd&_json=1&fid=2', data=params)
print(response6.text)
res6 = response6.json()
if res6["state"] == "fail":
    print("用例6：验证回帖接口用例成功")