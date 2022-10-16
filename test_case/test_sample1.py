'''

@File:test_sample1.py
@Datetime:2022/10/3 23:52
@Author:wangt
@Desc:
'''
import pytest

def inc(x):
    return x + 1

def test_answer01():
    assert inc(3) == 5


@pytest.mark.run(order=1)
def test_answer02():
    assert inc(5) == 6

@pytest.mark.run(order=2)
def test_answer03():
    assert inc(4) == 5

def test_answer04():
    assert inc(6) == 7


if __name__ == '__main__':
    pytest.main(['-vs','test_sample1.py'])