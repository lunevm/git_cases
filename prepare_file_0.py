#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.DataFrame({'a':[1,2,3]})


# In[4]:


df


# In[8]:


df.to_csv('data/file_0.csv', index=False)


# In[10]:


pd.read_csv('data/file_0.csv')


# In[ ]:




