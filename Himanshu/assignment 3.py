#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write a program that appends the square of each number to a new list.
# Example:
# Given x = [2,3,4,5,6,7,8]

# Expected output 
# Result: [4, 9, 16, 25, 36, 49, 64]


# In[34]:


x = [2,3,4,5,6,7,8]
y = []
for i in x:
    y.append(i**2)
print(y)


# In[24]:


# WAP(write a program) to separate positive and negative number from a list.
# Example:
# Given x = [23, 4, -6, 23, -9, 21, 3, -45, -8]

# Expected output 
# Result:
# Positive: [23, 4, 23, 21, 3] Negative: [-6, -45, -9, -8]


# In[75]:


x = [23, 4, -6, 23, -9, 21, 3, -45, -8]
pos = []
neg = []

for i in x:
    if (i>=0):
        pos.append(i)
    else:
        neg.append(i)
print(pos)
print(neg)


# In[ ]:


# Write a program that create a list with the type of elements from a  given list.
# Example
# Given x = [23, ‘Python’, 23.98]

# Expected output 
# Result:
# [<class 'int'>,<class 'str'>,<class 'float'>]


# In[98]:


x = [23, 'Python', 23.98]
y = []
for i in x:
    y.append(type(i))
print(y)
    


# In[ ]:


# Print a pattern as shown below:
# 012345
# 01234
# 0123
# 012
# 01


# In[112]:


x = 5
for i in range(x+1,1,-1):
    for j in range(0,i):
        print(j, end="")
    print("\n")


# In[ ]:




