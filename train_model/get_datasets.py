# coding: utf-8
import os
import sys

module_path = os.path.abspath(os.path.join('..'))
sys.path.append(module_path)

# remove warnings
import warnings

warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
from conf.configure import Configure
from utils import feature_utils, data_utils


def merge_datasets():
    train_data_id_label=pd.read_csv(Configure.train_label_path, encoding='ANSI')
    test_data=pd.read_csv(Configure.test_vid_path,encoding='ANSI',usecols=['vid'])
    print(train_data_id_label,test_data)
    # y_train = feature_utils.get_label(train)
    #
    # train_index = pd.Index(train['TERMINALNO'])
    # test_index = pd.Index(test['TERMINALNO'])
    # train_index = train_index.unique()
    # test_index = test_index.unique()
    #
    # # 取出训练与测试集中的用户列
    # train = pd.DataFrame(train_index, index=train_index)
    # test = pd.DataFrame(test_index, index=test_index)

    # 加载记载在configure列表中的特征，并且合并
    for feature_name in Configure.features:
        print('pd merge', feature_name)
        train_feature, test_feature = data_utils.load_features(feature_name)
        train = pd.merge(train, train_feature,
                         left_index=True,
                         right_index=True)
        test = pd.merge(test, test_feature,
                        left_index=True,
                        right_index=True)



if '__main__'=='__main__':
    merge_datasets()
    tmp=pd.read_csv(Configure.cleaned_path,encoding='ANSI')
    print(tmp.describe())
