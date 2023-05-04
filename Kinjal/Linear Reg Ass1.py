#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


from sklearn.linear_model import LinearRegression


# In[4]:


from sklearn.metrics import accuracy_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split


# In[5]:


data = pd.read_csv('advertising_and_sales_clean.csv')


# In[6]:


data.info()


# In[7]:


df = pd.DataFrame(data)


# In[8]:


df


# In[9]:


features = df[["tv","radio","social_media"]]


# In[10]:


features


# In[11]:


target = df[["sales"]]


# In[12]:


target


# In[31]:


X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.20)


# In[33]:


X_train.shape


# In[34]:


X_train


# In[35]:


X_test


# In[36]:


y_train


# In[18]:


y_test


# In[19]:


Lreg = LinearRegression()


# In[20]:


Lreg.fit(X_train.values, y_train.values)


# In[21]:


Lreg.coef_


# In[22]:


Lreg.intercept_


# In[25]:


y_pred = Lreg.predict(X_test.values.reshape(-1,3))


# In[28]:


y_pred


# In[30]:


mean_squared_error(y_pred, y_test)


# In[ ]:





# In[ ]:




