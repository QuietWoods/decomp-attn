#/usr/bin/env python
#coding=utf-8
import jieba
import sys
jieba.load_userdict('mydict/mydict.txt')

def process(inpath):
    sen1w = open('sen1.txt', 'w')
    sen2w = open('sen2.txt', 'w')

    with open(inpath, 'r') as fin:
        for line in fin:
            #print(line.strip().split('\t'))
            lineno, sen1, sen2, _  = line.strip().split('\t')
            stopwords = '，。！？*'
            words1 = [w for w in jieba.cut(sen1) if w.strip() and w not in stopwords]
            words2 = [w for w in jieba.cut(sen2) if w.strip() and w not in stopwords]
            sen1w.write(' '.join(words1))
            sen1w.write('\n')
            sen2w.write(' '.join(words2))
            sen2w.write('\n')
    sen1w.close()
    sen2w.close()

if __name__ == '__main__':
    process(sys.argv[1])

