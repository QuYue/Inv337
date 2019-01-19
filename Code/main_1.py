# -*- coding: utf-8 -*-
"""
@Author: QuYue
@Time  : 2019/1/19 14:22
@File  : main_1.py
"""

#%% Import Packages
import numpy as np
import pandas as pd
import torch

import Inv337
#%% Hyper Parameter 超参数（调试部分）
class Parameter:
    # Class for the Hyper Parameter 超参数类
    def __init__(self):
        self.Time = 3  # set bin size 设置多少年为一段（默认3年一段）

        self.Path = '../data/raw_data/'  # data path 数据路径
        self.Data = '337_Data.csv'  # data name 数据名字
#%%
PARM = Parameter()
[data, c_company, u_company] = Inv337.data_input(PARM)
