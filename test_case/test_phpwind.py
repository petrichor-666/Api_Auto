'''

@File:test_phpwind.py
@Datetime:2022/9/29 0:54
@Author:wangt
@Desc:
'''
import unittest

import pytest
import requests
from urllib import parse
import time
import logging

class PhpwindTest(unittest.TestCase):
    """Phpwind测试"""
    # 类属性,可直接被类方法调用
    session = requests.session()
    base_url = "http://43.226.74.244/phpwind/index.php"
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest"
    }
    # def setUp(self):
    #     self.base_url = "http://43.226.74.244/phpwind/index.php"

    @pytest.mark.smoke
    def test01_index(self):     # 首页接口用例
        """首页接口测试"""
        logging.info('test01_index')
        # url = "http://43.226.74.244/phpwind/index.php"
        response1 = self.session.get(self.base_url)
        # csrf_token = response1.cookies["csrf_token"]
        # s9R_lastvisit = response1.cookies["s9R_lastvisit"]
        # s9R_visitor = response1.cookies["s9R_visitor"]
        self.assertIn('Powered',response1.text)

    def test02_checkname(self):     # 检查用户名用例
        """检查用户名测试"""
        logging.info('test02_checkname')
        url = f"{self.base_url}?m=u&c=login&a=checkname"
        params = {
            "username": "chen123",
            "csrf_token": self.session.cookies['csrf_token']
        }
        response2 = self.session.post(url=url,data=params,headers=self.headers)
        data = response2.json()
        self.assertEqual("success",data["state"])

    # 3.登录接口用例
    def test03_login(self):
        """登录接口测试"""
        logging.info('test03_login')
        url = f"{self.base_url}?m=u&c=login&a=dorun"
        params = {
            "username": "chen123",
            "password": "chen123",
            "csrf_token": self.session.cookies['csrf_token']
            # "backurl": "http://47.107.116.139/phpwind/"
        }
        response3 = self.session.post(url=url, data=params, headers=self.headers)
        self.res3 = response3.json()
        self.assertEqual(self.res3["state"], "success")

    # 4.验证重定向referer接口地址
    def test04_referer(self):
        """重定向referer接口测试"""
        # print(referer_url)
        logging.info('test04_referer')
        self.test03_login()     # 调用类中的其他函数，需要先调用函数
        referer = self.res3["referer"]
        referer_url = parse.unquote(referer)  # 转义url
        response4 = self.session.get(referer_url)
        # print(response4.text)
        self.assertIn("Powered",response4.text)

    # 5.验证发帖接口
    def test05_post(self):
        """发帖接口测试"""
        logging.info('test05_post')
        url = f"{self.base_url}?c=post&a=doadd&_json=1&fid=2"
        params = {
            "fid": "2",
            "atc_title": f"发帖test{self.now}",
            "atc_content": f"{self.now}发帖test",
            "csrf_token": self.session.cookies['csrf_token'],
            "reply_notice": "1",
            "special": "default",
        }
        self.response5 = self.session.post(url=url, data=params)
        # print(response5.text)
        self.res5 = self.response5.json()
        # res5_str = parse.unquote(str(res5))
        # print(res5_str)
        self.referer = self.res5["referer"]
        self.referer_url = parse.unquote(self.referer)  # 转义url
        # print(referer_url)
        self.tid = self.referer_url[42:45]  # 切片获取refer_url中 tid的值
        # print(self.tid)
        self.assertEqual(self.res5["state"], "success")
        time.sleep(3.1)

        # 6.验证回帖接口
    @pytest.mark.skip(reason="跳过回帖接口测试")
    def test06_return(self):
        """回帖接口测试"""
        logging.info('test06_return')
        url = "http://43.226.74.244/phpwind/index.php?c=post&a=doadd&_json=1&fid=2"
        self.now = time.strftime('%Y-%m-%d %H_%M_%S')

        self.test05_post()
        params = {
            "atc_content": f"{self.now}回帖test",
            "csrf_token": self.session.cookies['csrf_token'],
            "tid": self.tid           # 注：此参数需在这地方转化为整数类型
        }
        response6 = self.session.post(url=url, data=params)
        print(response6.text)
        res6 = response6.json()
        self.assertEqual(res6["state"], "fail")


if __name__ == '__main__':
    unittest.main()

