#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[21]:


df = pd.read_csv('desktop/advertising_and_sales_clean.csv')


# In[7]:


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


# In[22]:


df


# In[23]:


features = df[["tv","radio","social_media"]]


# In[25]:


features


# In[26]:


target = df[["sales"]]


# In[27]:


target


# In[28]:


print(features.shape)
print(target.shape)


# In[42]:


Lreg = LinearRegression()


# In[43]:


Lreg.fit(features, target)


# In[44]:


Lreg.coef_


# In[45]:


Lreg.intercept_


# In[72]:


from sklearn.model_selection import train_test_split


# In[75]:


x_train, x_test, y_train, y_test = train_test_split(features, target, test_size = 0.30)


# In[76]:


x_train.shape


# In[78]:


x_train


# In[79]:


x_test


# In[80]:


y_train


# In[81]:


y_test


# In[82]:


reg = LinearRegression()


# In[83]:


type(x_train)


# In[84]:


type(x_train.values)


# In[86]:


reg.fit(x_train.values, y_train)


# In[87]:


reg.coef_


# In[88]:


y_pred = reg.predict(x_test.values)


# In[89]:


y_pred


# In[90]:


mean_squared_error(y_pred, y_test)

