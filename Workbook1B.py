#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "C:\Users\chris\Documents\Python\datasets\Crime.xls"
#add headers to imported data
df = pd.read_excel(Location)
df.head()

