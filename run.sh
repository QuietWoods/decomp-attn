#!/bin/bash
# 初始化语料库
python3 process-snli.py  --data_folder data --out_folder output

# 数据预处理
python preprocess.py --srcfile output/src-train.txt --targetfile output/targ-train.txt --labelfile output/label-train.txt --srcvalfile output/src-dev.txt --targetvalfile output/targ-dev.txt --labelvalfile output/label-dev.txt --srctestfile output/src-test.txt --targettestfile output/targ-test.txt --labeltestfile output/label-test.txt --outputfile data/entail --glove glove/vectors.txt 
# 转成词向量
python get_pretrain_vecs.py --glove glove/vectors.txt --outputfile data/glove.hdf5 --dictionary data/entail.word.dict 
# 模型训练

th train.lua -data_file data/entail-train.hdf5 -val_data_file data/entail-val.hdf5 -test_data_file data/entail-test.hdf5 -pre_word_vecs data/glove.hdf5 
 
# 处理测试数据
#bash predic_handle_test.sh data/atec_1.0_test.csv 

# 模型预测
th predict.lua -sent1_file sen1.txt -sent2_file sen2.txt -model model.t7 -word_dict data/entail.word.dict -label_dict data/entail.label.dict -output_file pred.txt


