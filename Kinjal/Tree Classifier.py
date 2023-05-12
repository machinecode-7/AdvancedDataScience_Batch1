#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.tree import DecisionTreeClassifier


# In[2]:


from sklearn.model_selection import train_test_split


# In[3]:


import pandas as pd


# In[57]:


import numpy as np


# In[62]:


from sklearn.preprocessing import LabelEncoder


# In[19]:


data = pd.read_csv('iris.csv')


# In[20]:


data.head()


# In[100]:


data.columns


# In[101]:


x = data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
# x = data[data.columns[:-1]]
y = data['variety']


# In[102]:


binary = LabelEncoder()


# In[103]:


y_binary = binary.fit_transform(y)
print(y_binary)


# In[104]:


x_train, x_test, y_train, y_test = train_test_split(x,y_binary)


# In[105]:


x_train


# In[106]:


x_test


# In[107]:


y_train


# In[108]:


y_test


# In[109]:


dtf = DecisionTreeClassifier(max_depth=5)


# In[110]:


dtf.fit(x_train, y_train)


# In[111]:


y_pred = dtf.predict(x_test)


# In[112]:


from sklearn.metrics import accuracy_score


# In[113]:


accuracy_score(y_pred, y_test)*100


# In[114]:


for i in range(1,11):
    dtf = DecisionTreeClassifier(max_depth=i)
    dtf.fit(x_train, y_train)
    y_pred = dtf.predict(x_test)
    print(i , accuracy_score(y_pred, y_test))


# In[115]:


dtf.tree_.threshold


# In[116]:


dtf.tree_.feature


# In[117]:


from sklearn import tree


# In[118]:


tree.plot_tree(dtf)


# In[119]:


x_train.columns


# In[120]:


import numpy as np


# In[ ]:





# In[ ]:




