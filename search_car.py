#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import pandas as pd
import re
import sys

# In[3]:


r = requests.get("https://dsci551-7d492-default-rtdb.firebaseio.com/index.json")


# In[7]:


a = r.json()


# In[38]:


m = sys.argv[1]
result = re.split(r'[，！() - " ]',m)
result = [j for j in result if j != '']


# In[41]:


id_list = []
for i in result:
    id_list = id_list + a[i]['car_ID']
b = {}
for i in id_list:
    if id_list.count(i)>0:
        b[i] = id_list.count(i)
b = sorted(b.items(), key=lambda item:(item[1],item[0]), reverse = True)
#print (b)


# In[42]:


final_list = []
for i in b:
    final_list.append(i[0])
print(final_list)

