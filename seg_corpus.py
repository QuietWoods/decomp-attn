#/usr/bin/env python
#coding=utf-8
import jieba
import sys
jieba.load_userdict('mydict/mydict.txt')

def process(inpath, outpath):
    with open(inpath, 'r') as fin, open(outpath, 'w') as fout:
        for line in fin:
            #print(line.strip().split('\t'))
            lineno, sen1, sen2, _  = line.strip().split('\t')
            stopwords = '，。！？*'
            words1 = [w for w in jieba.cut(sen1) if w.strip() and w not in stopwords]
            words2 = [w for w in jieba.cut(sen2) if w.strip() and w not in stopwords]
            union = words1 + words2
            fout.write(' '.join(union))
            fout.write(' ')

if __name__ == '__main__':
    process(sys.argv[1], sys.argv[2])

