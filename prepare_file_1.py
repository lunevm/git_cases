#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('data/file_0.csv')


# In[4]:


df['b'] = [7,8,9]


# In[5]:


df.head()


# In[6]:


df.to_csv('data/file_1.csv', index=False)


# In[ ]:




