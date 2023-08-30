#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json
import pandas as pd
import sys

# In[14]:


df = pd.read_csv('cars.csv')
column = ['price','car_ID']


# In[20]:


data = df[column]
# In[22]:


m, n= int(sys.argv[1]), int(sys.argv[2])
result = []
i = 0
while i < len(data):
    if data["price"][i] <= n and data["price"][i] >= m:
        result.append(data['car_ID'][i])
    i += 1
if result == []:
    print('No cars found with the given range')
else:
    print(result)


# In[ ]:




