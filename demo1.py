'''

@File:demo1.py
@Datetime:2022/10/12 10:11
@Author:wangt
@Desc:
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}\t",end='')
    print()