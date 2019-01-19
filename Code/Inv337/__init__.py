# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 18:40:18 2018

@author: QuYue
"""
#%% Import Package 加载模块 
import pandas as pd
import numpy as np
import re
#%% Functions
def data_input(PARM):
    """This Function can input the data
    """
    # Read Data 读取数据
    data = pd.read_csv(PARM.Path+PARM.Data, index_col=0)
    # Split the string to list 将字符串变成list
    data['Patent Nos.'] = data['Patent Nos.'].apply(split_data)
    data['Complainants'] = data['Complainants'].apply(split_data)
    data['Respondents'] = data['Respondents'].apply(split_data)
    # Delete the Useless Data 删除无用的数据
    data['useful'] = data.apply(choose_data, axis = 1)
    data = data[data['useful'] == 1]
    data = data.drop(columns=['useful', 'Data']).reset_index(drop=True)
    # Get ID 将公司名字变成ID号
    [data['Complainants'], c_company] = get_ID(data['Complainants'])
    [data['Respondents'], u_company] = get_ID(data['Respondents'])
    return data, c_company, u_company

def split_data(string):
    """This Function can split a string like "['a', 'b']" to a list like ['a', 'b']
    """
    if string == '[]':
        name = []
    else:
        string = string[2:-2]
        name = re.split(r"['|\"], ['|\"]", string)
    return name

def choose_data(inv):
    """This Function can choose the useful investigations
    """
    if (2000<= inv['Start Year'] <=2017 # the Start Year between 2000 and 2017 开始年份在2000和2017年之间
    and len(inv['Complainants'])  != 0  # the Complainants need no empty 起诉公司非空
    and len(inv['Respondents'])  != 0): # the Respondents need no empty 被起诉公司非空
        return 1
    else:
        return 0

def get_ID(company):
    """This Function can get the ID of the company
    """
    company_dict = {}       # company dict(name to ID) 建立公司名字和ID号的对应字典
    company = list(company) # change series to list(more faster) 将Series变成list(迭代更快)
    count = 0
    for i in range(len(company)):
        temp = []
        data = company[i]
        for j in data:
            if j in company_dict:
                temp.append(company_dict[j])
            else:
                company_dict[j] = count
                temp.append(company_dict[j])
                count += 1
        company[i] = temp
    company_dict = pd.DataFrame({'ID': list(company_dict.values()), 'Name': list(company_dict.keys())})
    return company, company_dict