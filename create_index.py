#!/usr/bin/env python
# coding: utf-8

# In[16]:


import requests
import json
import re
import pandas as pd


# In[5]:


df = pd.read_csv('cars.csv')
column = ['CarName','car_ID']


# In[6]:


data = df[column]


# In[23]:


i = 0
name_dic = {}
while i < len(data):
    result = re.split(r'[，！() -]',data["CarName"][i])
    result = [j for j in result if j != '']
    name_dic[data['car_ID'][i]] = result
    i += 1


# In[53]:


index = []
for element in name_dic.values():
    for i in element:
        if i not in index:
            index.append(i)
##print(index)


# In[52]:


index_dic = {}
for i in index:
    result = []
    for k,val in name_dic.items():       
        if i in val:
            result.append(k)
    index_dic[i] = result
##print(index_dic)


# In[54]:


dff = pd.DataFrame(pd.Series(index_dic), columns=['car_ID'])
dff = dff.reset_index().rename(columns={'index':'keyword'})
##print(dff)


# In[55]:


data = dff.set_index('keyword').to_json(orient = 'index')


# In[51]:


requests.put("https://dsci551-7d492-default-rtdb.firebaseio.com/index.json",data)


# In[ ]:




