#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Write a program that appends the square of each number to a new list.
# Example:
# Given x = [2,3,4,5,6,7,8]

# Expected output 
# Result: [4, 9, 16, 25, 36, 49, 64]


# In[16]:


x = [2,3,4,5,6,7,8]
l = []
for i in x:
    l.append(i*i)
print(l)


# In[ ]:


# WAP(write a program) to separate positive and negative number from a list.
# Example:
# Given x = [23, 4, -6, 23, -9, 21, 3, -45, -8]

# Expected output 
# Result:
# Positive: [23, 4, 23, 21, 3] Negative: [-6, -45, -9, -8]


# In[18]:


x = [23, 4, -6, 23, -9, 21, 3, -45, -8]
p = []
n = []
for i in x:
    if i >=0:
        p.append(i)
    else:
        n.append(i)
print(p)
print(n)


# In[2]:


# Write a program that create a list with the type of elements from a  given list.
# Example
# Given x = [23, ‘Python’, 23.98]

# Expected output 
# Result:
# [<class 'int'>,<class 'str'>,<class 'float'>]


# In[11]:


x = [23,'Python' ,23.98]

t = []

for r in x:
    t.append(type(r))
print(t)
    


# In[3]:


# Print a pattern as shown below:
# 012345
# 01234
# 0123
# 012
# 01
# 0


# In[4]:


for i in range (6,0,-1):
    for j in range(0,i):
        print(j,end="")
    print('')


# In[ ]:




