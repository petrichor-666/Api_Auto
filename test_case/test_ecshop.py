'''

@File:test_ecshop.py
@Datetime:2022/9/30 1:15
@Author:wangt
@Desc:
'''
import unittest
from ddt import ddt
import requests
from ddt import file_data
import logging

@ddt
class EcshopTest(unittest.TestCase):
    """Ecshop测试"""
    @file_data('../data/ecshop_data.yaml')       # 远程加载yaml文件    ../表示上一级，  ./表示同级
    def test01_login(self, **kwargs):
        """Ecshop登录测试"""
        logging.info('test01_login')
        url = "http://43.226.74.244/ecshop/user.php"
        data = {
            "username": kwargs['user'],
            "password": kwargs["pwd"],
            "act": "act_login",
            "back_act": "http://43.226.74.244/ecshop/",
            "submit": ""
        }
        response = requests.post(url=url,data=data)
        self.assertIn(kwargs["res"],response.text)


if __name__ == '__main__':
    unittest.main()

# 数据驱动
# 步骤：
# 1、安装yaml数据格式模块： pip install pyyaml
# 2、构建yaml数据源（相当于postman中的json/csv文件）
# 3、安装ddt数据驱动模块：pip install ddt
# 4、写注解关键字（python注解就是在类或方法的头上写@）