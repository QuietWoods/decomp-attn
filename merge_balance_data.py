# -*- coding: utf-8 -*-
# @Time    : 2018/5/29 20:12
# @Author  : QuietWoods
# @FileName: balance_data.py
# @Software: PyCharm
# @Email    ：1258481281@qq.com
import sys

def merge_balance_data(inputpath1, inputpath2, outputpath):
    with open(inputpath1, 'r') as f1, open(inputpath2, 'r') as f2, open(outputpath, 'w') as w:
        for line1 in f1:
            w.write(line1)
        for line2 in f2:
            w.write(line2)
    print('merge done!')


if __name__ == '__main__':
    merge_balance_data(sys.argv[1], sys.argv[2], sys.argv[3])


