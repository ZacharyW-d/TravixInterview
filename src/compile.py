#!/usr/bin/env python
# coding: utf-8



import csv
import pandas as pd
import os
import datetime 
import re
import math

from currency_formatter import Currency



file_list = [file.path for file in os.scandir('../Data/')]

data = pd.DataFrame()

for file_path in file_list:
    temp = pd.read_csv(file_path, header=4, sep=';')
    temp_info = pd.read_csv(file_path, header=None, nrows=2).iloc[1,0]
    temp['created_on'] = re.search('Created on;(.*);;;;;;;;;;;;;', temp_info).group(1)
    temp['from_file'] = file_path
    
    data = data.append(temp)
    
data.reset_index(inplace=True)

data.to_csv('combined_data.csv', sep=';')

