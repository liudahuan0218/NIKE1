# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:23:20 2019

@author: 南陌欢少
"""
import pandas as pd
import numpy as np
import tensorflow as tf

#Step1:下载数据
#Step2:数据准备
ratings_df = pd.read_csv(open(r'C:\Users\南陌欢少\Desktop\python project\音乐推荐\movies_recommend_system-master\ratings.csv'))
#使用tail查看后几行数据，默认5行
#ratings_df.tail()

movies_df = pd.read_csv(open(r'C:\Users\南陌欢少\Desktop\python project\音乐推荐\movies_recommend_system-master\movies.csv'))
# movies_df.tail()



