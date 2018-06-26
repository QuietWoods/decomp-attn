# -*- coding: utf-8 -*-
# @Time    : 2018/5/29 20:12
# @Author  : QuietWoods
# @FileName: balance_data.py
# @Software: PyCharm
# @Email    ：1258481281@qq.com
import sys
import random


def balance_data(inputpath, outputpath):
    sample0 = []
    sample1 = []
    with open(inputpath, 'r') as f:
        for line in f:
            lineno, sen1, sen2, label = line.strip().split('\t')
            if label == '0':
                sample0.append(line)
            elif label == '1':
                sample1.append(line)
            else:
                print("不正确的标签：{}".format(line))
    size0 = len(sample0)
    size1 = len(sample1)
    print(size0)
    print(size1)
    biger_sample = sample0 if (size0 - size1) else sample1
    rate = (len(biger_sample) - size0) / size0
    print(rate)
    if not rate:
        rate = (len(biger_sample) - size1) / size1
        sample1 = sample1 * int(rate + 1)
    else:
        sample0 = sample0 * int(rate + 1)
    print(len(sample0))
    print(len(sample1))
    sample0.extend(sample1)
    random.shuffle(sample0)
    print(len(sample0))
    with open(outputpath, 'w', encoding='utf-8') as w:
        w.write(''.join(sample0))


if __name__ == '__main__':
    balance_data(sys.argv[1], sys.argv[2])
