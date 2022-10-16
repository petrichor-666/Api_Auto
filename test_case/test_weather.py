'''

@File:test_weather.py
@Datetime:2022/9/28 21:28
@Author:wangt
@Desc:
'''
import unittest

import pytest
import requests
from urllib import parse
from time import sleep

class WeatherTest(unittest.TestCase):
    """天气接口测试"""

    def setUp(self):
        self.url = "https://v0.yiketianqi.com/api"
    @pytest.mark.smoke
    def test_weather_beijing(self):
        """北京天气测试"""
        param = {"appid": "91186593", "appsecret": "fckbO7y5", "version":"v9", "city":"北京", "unescape":"1"}
        city = parse.urlencode(param).encode('utf-8')
        response = requests.get(self.url, params=city)
        response_data = response.json()

        self.assertEqual(response_data['city'],'北京')
        self.assertEqual(response_data['cityid'],'101010100')
        sleep(3)

    def test_weather_wrong(self):
        """输入错误城市测试"""
        param = {"appid": "91186593", "appsecret": "fckbO7y5", "version":"v9", "city":"555", "unescape":"1"}
        # city = parse.urlencode(param).encode('utf-8')  # 参数是数字不需要用此方法
        response = requests.get(self.url, params=param)
        response_data = response.json()

        self.assertEqual(response_data['errcode'], 100)
        self.assertEqual(response_data['errmsg'],'city不存在')
        sleep(3)

    def test_weather_null(self):
        """输入空参数测试"""
        response = requests.get(self.url)
        response_data = response.json()

        self.assertEqual(response_data['errcode'], 100)
        sleep(3)


if __name__ == '__main__':
    unittest.main()