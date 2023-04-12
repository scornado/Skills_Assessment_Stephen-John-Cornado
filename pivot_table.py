#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv(r'D:\Selenium\skill_test_data.csv')


# In[3]:


df.head()


# In[4]:


df_pivot = pd.pivot_table(df,index='Platform (Northbeam)', values =['Spend','Imprs','Attributed Rev (1d)','Visits','New Visits','Transactions (1d)','Email Signups (1d)'], aggfunc='sum')


# In[5]:


df_pivot.head()


# In[6]:


df_pivot.to_excel (r'D:\Selenium\pivot_output.xlsx')


# In[ ]:




