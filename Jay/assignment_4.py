#!/usr/bin/env python
# coding: utf-8

# In[27]:


# Write a program that appends the square of each number to a new list.
# Example:
# Given x = [2,3,4,5,6,7,8]

# Expected output 
# Result: [4, 9, 16, 25, 36, 49, 64]


# In[28]:


x = [2,3,4,5,6,7,8]
squares = []
for i in x:
    squares.append(i**2)
print(squares)
    


# In[29]:


# WAP(write a program) to separate positive and negative number from a list.
# Example:
# Given x = [23, 4, -6, 23, -9, 21, 3, -45, -8]

# Expected output 
# Result:
# Positive: [23, 4, 23, 21, 3] Negative: [-6, -45, -9, -8]


# In[30]:


x = [23, 4, -6, 23, -9, 21, 3, -45, -8]

Positive= []
Negative = []
for i in x:
    if (i >= 0):
        Positive.append(i)
    else:
        Negative.append(i)
print(Positive) 
print(Negative)


# In[31]:


# Write a program that create a list with the type of elements from a  given list.
# Example
# Given x = [23, ‘Python’, 23.98]

# Expected output 
# Result:
# [<class 'int'>,<class 'str'>,<class 'float'>]


# In[32]:


x = [23, 'Python', 23.98]
output = []
for elements in x:
    output.append(type(elements))
print(output)


# In[33]:


# Print a pattern as shown below:
# 012345
# 01234
# 0123
# 012
# 01


# In[34]:


rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end='')
    print('\r')


# In[ ]:





# In[ ]:




