# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 04:08:32 2019

@author: Exam
"""

import pandas as pd
df=pd.read_csv("D:\\Automobile_data.csv")
#df.head(5)
#df.tail(5)
#df[1:10]
#df[1:10:2]
#df["company"]
#df[["company","price"]]
df.loc[[1,2],["company","price"]]