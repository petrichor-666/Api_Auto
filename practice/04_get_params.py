'''

@File:04_get_params.py
@Datetime:2022/9/24 19:39
@Author:wangt
@Desc:
'''
"""
需求：
1. 访问TPshop搜索商品的接口，通过查询字符串的方式传递搜索的关键字 iPhone ，并查看响 应数据
2. 请求路径格式为： http://localhost/Home/Goods/search.html?q=iPhone
"""
import requests
# 1.将url全部传递
# response = requests.get("http://localhost/Home/Goods/search.html?q=iPhone")
# print(response.text)

# 2.把url和查询参数分开，params接受的是字符串
# url = "http://localhost/Home/Goods/search.html"
# q = "q=iphone"
# response = requests.get(url, params=q)
# print(response.text)

# 3.把url和查询参数分开，params接受的是字典
url = "http://localhost/Home/Goods/search.html"
dq = {"q": "iphone"}
response2 = requests.get(url, params=dq)
print(response2.text)