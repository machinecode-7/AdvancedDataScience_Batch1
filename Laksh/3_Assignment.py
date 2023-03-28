#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Take a value greater than 1 from user (You can put it in any variable)
# Print the sum of all numbers from 1 to that number
#for eg: num=3
#output should be 6 (since 1+2+3 is 6
#Try implementing it with *For* as well as *While* Loop


# In[20]:


num = int(input("Enter the number of pattern:"))
sum =0
for i in range (1, num+1):
    sum += i
print(sum)


# In[23]:


num = int(input("Enter the number of pattern:"))
k =0
sum=0
while k <= num:
    sum += k
    k+=1
print(sum)


# In[ ]:


# Use a loop to display elements from a given list present at odd index positions
# my_list = [10,20,11,22,33,44,66,76,87,98,20,30,40,50,23,45,67,89]


# In[44]:


my_list = [10,20,11,22,33,44,66,76,87,98,20,30,40,50,23,45,67,89]
x=0
for i in my_list:
    if x%2 != 0:
        print(i)


# In[ ]:


#print pattern in the output as shown below, if the user input(or your variable value) is 4
*
**
***
****
***
**
*
# the variable value represents the max value of stars


# In[1]:


num = int(input("Enter the number of pattern:"))
for i in range(0,num):
    for j in range(1,i+1):
        print("*",end="")
    print('')
    
for i in range(num +1,0,-1):
    for j in range(0,i-1):
        print("*", end="")
    print('')


# In[ ]:


# concept: Factorial of 5 is 5*4*3*2*1 = 120
# Find the factorial of any number provided by user


# In[17]:


m = 6
z = 1
for i in range(1,m+1):
    z *= i
    print(z)


# In[2]:


# Display numbers from -10 to -1 using While and For Loop


# In[6]:


for i in range(-10,0):
    print(i)


# In[7]:


l = -10
while l < 0:
    print(l)
    l = l+1


# In[ ]:




