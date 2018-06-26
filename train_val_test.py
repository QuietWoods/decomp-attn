#/usr/bin/env python
#coding=utf-8
import jieba
import sys
import numpy as np

jieba.load_userdict('mydict/mydict.txt')
# 把语料切分成三份，train valid test 8:1:1

def process(inpath, trainpath, validpath, testpath):
    text_data = []

    with open(inpath, 'r') as fin:
        for line in fin:
            text_data.append(line)

    shuffled_ix = np.random.permutation(np.arange(len(text_data)))
    text_data_ar = np.array(text_data)
    text_shuffled = text_data_ar[shuffled_ix] # 随机文本数据集
    #分割数据集 train:valid:test 8:1:1
    ix_cutoff = int(len(text_shuffled) * 0.8)
    ix_cutoff2 = ix_cutoff + int(len(text_shuffled)*0.1)
    train, valid, test = text_shuffled[:ix_cutoff], text_shuffled[ix_cutoff:ix_cutoff2], text_shuffled[ix_cutoff2:]
    print("8:1:1 train valid test split: {:d}:{:d}:{:d}".format(len(train), len(valid), len(test)))
    #with open(trainpath, 'w') as wtrain, open(validpath, 'w') as wvalid, open(testpath, 'w') as wtest:        
    with open(trainpath, 'w', encoding='utf-8') as wtrain:
        for item in train:
            wtrain.write(item)
    with open(validpath, 'w', encoding='utf-8') as wvalid:
        for item in valid:
            wvalid.write(item)
    with open(testpath, 'w', encoding='utf-8') as wtest:
        for item in test:
            wtest.write(item)

    #np.savetxt(trainpath, train, fmt='%s', delimiter='', encoding='utf8') #指定存储数据类型为字符串，分隔符无
    #np.savetxt(validpath, valid, fmt='%s', delimiter='', encoding='utf8')
    #np.savetxt(testpath, test, fmt='%s', delimiter='', encoding='utf8')


if __name__ == '__main__':
    process(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

