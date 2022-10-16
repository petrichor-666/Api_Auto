'''

@File:unittest_frame.py
@Datetime:2022/9/29 23:58
@Author:wangt
@Desc:
'''
import unittest

# 自定义类，继承TestCase
class ApiTest(unittest.TestCase):       # TestCase测试用例

    def setUp(self) -> None:        # 每执行一个用例前执行一次此方法，注：期待返回类型为None
        print('hello')

    def tearDown(self) -> None:     # 每执行一个用例后执行一次此方法
        print('world')

    @classmethod
    def setUpClass(cls) -> None:    # 整个程序运行前执行
        print('123')

    @classmethod
    def tearDownClass(cls) -> None: # 整个程序运行后执行
        print('456')

    # 用例：就是一个方法，该方法必须以Test开头
    # 注：单元测试框架中，用例的执行顺序跟方法名有关
    def test_demo2(self):
        print('demo2')

    def test_demo1(self):
        print('demo1')

# 主程序执行
if __name__ == '__main__':
    # 批量执行用例（固定写法）
    unittest.main()