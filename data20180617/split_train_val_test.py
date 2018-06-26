#/usr/bin/env python
#coding=utf-8
#import jieba
import sys
import numpy as np
import random

#jieba.load_userdict('mydict/mydict.txt')
# 把语料切分成三份，train valid test 8:1:1

def process(inpath, trainpath, validpath, testpath):
    # 首先随机文本数据集
    text_data = []
    with open(inpath, 'r') as fin:
        for line in fin:
            text_data.append(line)
    shuffled_ix = np.random.permutation(np.arange(len(text_data)))
    text_data_ar = np.array(text_data)
    text_shuffled = text_data_ar[shuffled_ix] # 随机文本数据集
    
    sim_text = []
    dif_text = []

    for item in text_shuffled:
        lineno, sent1, sent2, label = item.strip().split('\t')
        if label == '1':
            sim_text.append(item)
        elif label == '0':
            dif_text.append(item)
        else:
            print('error label')
            #text_data.append(line)
    sim_len = len(sim_text)
    dif_len = len(dif_text)
    sim_ix_0 = sim_len * 0.8
    sim_ix_1 = sim_ix_0 + sim_len * 0.1
    dif_ix_0 = dif_len * 0.8
    dif_ix_1 = dif_ix_0 + dif_len *0.1

    sim_ix_0 = int(sim_ix_0)
    sim_ix_1 = int(sim_ix_1)
    dif_ix_0 = int(dif_ix_0)
    dif_ix_1 = int(dif_ix_1)
    #print(type(sim_ix_0))
    #print(type(dif_ix_0))
    #分割数据集 train:valid:test 8:1:1
    sim_train, sim_dev, sim_test = sim_text[:sim_ix_0], sim_text[sim_ix_0:sim_ix_1], sim_text[sim_ix_1:]
    dif_train, dif_dev, dif_test = dif_text[:dif_ix_0], dif_text[dif_ix_0:dif_ix_1], dif_text[dif_ix_1:]
    
    print("8:1:1 sim_train sim_dev sim_test split: {:d}:{:d}:{:d}".format(len(sim_train), len(sim_dev), len(sim_test)))
    print("8:1:1 dif_train dif_dev dif_test split: {:d}:{:d}:{:d}".format(len(dif_train), len(dif_dev), len(dif_test)))
    sim_train.extend(dif_train)
    sim_dev.extend(dif_dev)
    sim_test.extend(dif_test)
    # 打乱列表序列
    random.shuffle(sim_train)
    random.shuffle(sim_dev)
    random.shuffle(sim_test)
    print("8:1:1 train dev test split:{:d}:{:d}:{:d}".format(len(sim_train),len(sim_dev), len(sim_test)))
    
 
    #with open(trainpath, 'w') as wtrain, open(validpath, 'w') as wvalid, open(testpath, 'w') as wtest:        
    with open(trainpath, 'w', encoding='utf-8') as wtrain:
        for item in sim_train:
            wtrain.write(item)
    with open(validpath, 'w', encoding='utf-8') as wvalid:
        for item in sim_dev:
            wvalid.write(item)
    with open(testpath, 'w', encoding='utf-8') as wtest:
        for item in sim_test:
            wtest.write(item)

    #np.savetxt(trainpath, train, fmt='%s', delimiter='', encoding='utf8') #指定存储数据类型为字符串，分隔符无
    #np.savetxt(validpath, valid, fmt='%s', delimiter='', encoding='utf8')
    #np.savetxt(testpath, test, fmt='%s', delimiter='', encoding='utf8')


if __name__ == '__main__':
    process(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

