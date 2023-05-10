#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Assignment


# In[ ]:


# Perform the same execise as above with all the features individually:
#Aim of this activity is to get used to coding and understand data better.


# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('diabetes_clean.csv')


# In[3]:


from sklearn.linear_model import LogisticRegression


# In[4]:


#model initiate (storing model in a variable)
Logreg = LogisticRegression()


# In[5]:


df


# In[6]:


#data prep


# In[7]:


type(df)


# In[8]:


type(df['pregnancies'])


# In[9]:


x = np.array(df['pregnancies']).reshape(-1,1)
y = df['diabetes'] 


# In[10]:


#model train


# In[11]:


Logreg.fit(x,y)


# In[12]:


Logreg.predict([[17]])


# In[13]:


pregnancies = np.array(list(range(0,18))).reshape(-1,1)
predictions_on_pregnancies = Logreg.predict(pregnancies)


# In[14]:


data = {
    'pregnancies' : np.array(list(range(0,18))),
    'pred' : predictions_on_pregnancies
}


# In[ ]:


data


# In[ ]:


pred_df = pd.DataFrame(data)


# In[15]:


import matplotlib.pyplot as plt


# In[ ]:


plt.figure(figsize=(18,6))
plt.scatter(pred_df['pregnancies'], pred_df['pred'])


# In[ ]:


sorted(df['glucose'].unique())


# In[21]:


Logreg = LogisticRegression()
type(df['glucose'])
x = np.array(df['glucose']).reshape(-1,1)
y = df['diabetes'] 
Logreg.fit(x,y)
glucose = np.array(list(range(44,199))).reshape(-1,1)
predictions_on_glucose = Logreg.predict(glucose)
data = {
    'glucose' : np.array(list(range(44,199))),
    'pred' : predictions_on_glucose
}
pred_df = pd.DataFrame(data)
plt.figure(figsize=(20,6))
plt.scatter(pred_df['glucose'], pred_df['pred'])


# In[ ]:


sorted(df['diastolic'].unique())


# In[23]:


Logreg = LogisticRegression()
x = np.array(df['diastolic']).reshape(-1,1)
y = df['diabetes'] 
Logreg.fit(x,y)
diastolic = np.array(list(range(24,122))).reshape(-1,1)
predictions_on_diastolic = Logreg.predict(diastolic)
data = {
    'diastolic' : np.array(list(range(24,122))),
    'pred' : predictions_on_diastolic
}
pred_df = pd.DataFrame(data)
plt.figure(figsize=(18,6))
plt.scatter(pred_df['diastolic'], pred_df['pred'])


# In[27]:


sorted(df['triceps'].unique())


# In[28]:


Logreg = LogisticRegression()
x = np.array(df['triceps']).reshape(-1,1)
y = df['diabetes'] 
Logreg.fit(x,y)
triceps = np.array(list(range(0,100))).reshape(-1,1)
predictions_on_triceps = Logreg.predict(triceps)
data = {
    'triceps' : np.array(list(range(0,100))),
    'pred' : predictions_on_triceps
}
pred_df = pd.DataFrame(data)
plt.figure(figsize=(18,6))
plt.scatter(pred_df['triceps'], pred_df['pred'])


# In[29]:


sorted(df['insulin'].unique())


# In[30]:


Logreg = LogisticRegression()
x = np.array(df['insulin']).reshape(-1,1)
y = df['diabetes'] 
Logreg.fit(x,y)
insulin = np.array(list(range(0,847))).reshape(-1,1)
predictions_on_insulin = Logreg.predict(insulin)
data = {
    'insulin' : np.array(list(range(0,847))),
    'pred' : predictions_on_insulin
}
pred_df = pd.DataFrame(data)
plt.figure(figsize=(18,6))
plt.scatter(pred_df['insulin'], pred_df['pred'])


# In[31]:


sorted(df['bmi'].unique())


# In[ ]:


Logreg = LogisticRegression()
x = np.array(df['bmi']).reshape(-1,1)
y = df['diabetes'] 
Logreg.fit(x,y)
insulin = np.array(list(range(0,70))).reshape(-1,1)
predictions_on_bmi = Logreg.predict(insulin)
data = {
    'bmi' : np.array(list(range(0,70))),
    'pred' : predictions_on_bmi
}
pred_df = pd.DataFrame(data)
plt.figure(figsize=(18,6))
plt.scatter(pred_df['bmi'], pred_df['pred'])


# In[ ]:


# Assignment 2


# In[ ]:


# perform all the steps which we use to do with Linear Regression like:
# 1) Imports
# 2) data prep
# 3) train-test split
# 4) train
# 5) test (find accuracy)


# In[52]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[81]:


x = df.iloc[:, :-1] 
y = df['diabetes']


# In[86]:


logreg = LogisticRegression(max_iter = 200)


# In[87]:


logreg.fit(X_train, y_train)


# In[88]:


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=40)


# In[89]:


y_pred = logreg.predict(X_test)


# In[90]:


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

