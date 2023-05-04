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


# In[5]:


data = pd.read_csv('advertising_and_sales_clean.csv')


# In[6]:


data


# In[7]:


df = pd.DataFrame(data)


# In[8]:


df


# In[9]:


Lreg = LinearRegression()


# In[10]:


features = df[['tv','radio','social_media']]


# In[11]:


features


# In[12]:


target = df[['sales']]


# In[13]:


target


# In[14]:


print(features.shape)
print(target.shape)


# In[15]:


Lreg.fit(features,target)


# In[16]:


#Lreg.coef_


# In[17]:


#Lreg.intercept_


# In[18]:


from sklearn.model_selection import train_test_split


# In[85]:


x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.95)


# In[86]:


x_train.shape


# In[87]:


x_train


# In[89]:


x_test


# In[90]:


y_train


# In[91]:


y_test


# In[92]:


Lreg = LinearRegression()


# In[93]:


Lreg.fit(x_train.values, y_train.values)


# In[94]:


Lreg.coef_


# In[95]:


Lreg.intercept_


# In[96]:


y_pred = Lreg.predict(x_test.values.reshape(-1,3))


# In[97]:


y_pred


# In[98]:


mean_squared_error(y_pred, y_test)


# In[ ]:




