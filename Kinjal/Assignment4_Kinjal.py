#!/usr/bin/env python
# coding: utf-8

# ## Assignment 4

# In[2]:


# Question 1
# Write a program that appends the square of each number to a new list.
# Example:
# Given x = [2,3,4,5,6,7,8]

# Expected output 
# Result: [4, 9, 16, 25, 36, 49, 64]


# In[ ]:


x = [2,3,4,5,6,7,8]
num=[]
for num in x:
     x.append(num*num)
print(num)


# In[28]:


# Question 2
# WAP(write a program) to separate positive and negative number from a list.
# Example:
# Given x = [23, 4, -6, 23, -9, 21, 3, -45, -8]

# Expected output 
# Result:
# Positive: [23, 4, 23, 21, 3] Negative: [-6, -45, -9, -8]


# In[3]:


x = [2,3,4,5,6,7,8]
num = []
for j in x:
    num.append(j*j)
print(num)


# In[7]:


x = [23, 4, -6, 23, -9, 21, 3, -45, -8]
positive = []
negative = []
for i in x:
    if i >=0:
        positive.append(i)
    else:
        negative.append(i)
        
print(positive)      
print(negative)


# In[ ]:





# In[30]:


# Question 3
# Write a program that create a list with the type of elements from a  given list.
# Example
# Given 

# Expected output 
# Result:
# [<class 'int'>,<class 'str'>,<class 'float'>]


# In[3]:


x = [23, 'Python', 23.98]
y = []

for i in x:
    y.append(type(i))
print(y)


# In[31]:


# Question 4
# Print a pattern as shown below:
# 012345
# 01234
# 0123
# 012
# 01


# In[42]:


x = 5


# In[66]:


rows = 5
for i in range(x, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print('\r')

