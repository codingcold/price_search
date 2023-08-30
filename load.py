#!/usr/bin/env python
# coding: utf-8

# In[35]:


import requests
import pandas as pd


# In[33]:


df = pd.read_csv('cars.csv')


# In[37]:


data = df.set_index('car_ID').to_json(orient = 'index')


# In[41]:


requests.put("https://dsci551-7d492-default-rtdb.firebaseio.com/cars.json",data)

