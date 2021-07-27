#!/usr/bin/env python
# coding: utf-8

# In[9]:


n = int(input("enter the no of rows"))

for i in range(n,0,-1):
    for j in range(0,i):
        print("5",end=" ")
    print(" ")
        
        


# In[15]:


for i in range(5,0,-1):
    for j in range(0,i+1,1):
        print (j,end=" " )
    print(" ")


# In[17]:


for i in range(1,11,2):
    for j in range(0,i,2):
        print(i,end=" ")
    print(" ")    


# In[18]:


for i in range(1,6,1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print(" ")    


# In[19]:


n = int(input())
a = 0
for i in range (1,n+1):
  a+=i
  k = a
  for j in range(i):
    print(k,end=" ")
    k-=1
  print()


# In[20]:


n = int(input())
for i in range(n):
    print(' '*(n-i), end=' ')
    print(' '.join(map(str, str(11**i))))


# In[21]:


n = int(input())
for i in range(0,n):
  k=1
  for j in range(1,n):
    if j <= i:
      print(i, end=' ')
    else:
        print(j, end=' ')
  print()


# In[22]:


n = int(input())
for i in range(1,n):
  for j in range(1,i+1):
    print(i * j, end=" ")
  print()


# In[23]:


n = int(input()) 
k = 2 * n - 2  
for i in range(n, -1, -1):   
  for j in range(k, 0, -1):  
    print(end=" ")  
  k = k + 1   
  for j in range(0, i + 1):  
    print("*", end=" ")
  print("")


# In[24]:


n = int(input()) 
k = 2 * n - 2  
for i in range(0,n):   
  for j in range(0,k):  
    print(end=" ")  
  k = k-1   
  for j in range(0, i + 1):  
    print("*", end=" ")
  print(" ")


# In[25]:


n = int(input())
for i in range(0,n):
    for j in range(0,i):
        print("*",end=" ")
    print()
print()
for i in range(n,0,-1):
  for j in range(i-1):
    print("*",end=" ")
  print()


# In[26]:


n = int(input())
for i in range(0,n):
    for j in range(0,i):
        print("*",end=" ")
    print()
for i in range(n,1,-1):
  for j in range(1,i-1):
    print("*",end=" ")
  print()


# In[27]:


n = int(input())
for i in range(0, n):
    for j in range(n-i):
      print(" ", end=' ')
    for j in range(0,i):
      print("*", end=" ")
    print("")

for i in range(n, 0, -1):
    for j in range(n-i):
      print(" ", end=' ')
    for j in range(0,i):
      print("*", end=' ')
    print("")


# In[28]:


n = int(input()) 
k = 2 * n - 2  
for i in range(n, -1, -1):   
  for j in range(k, 0, -1):  
    print(end=" ")  
  k = k + 1   
  for j in range(0, i + 1):  
    print("*", end=" ")
  print("")
for i in range(0,n):   
  for j in range(1,k):  
    print(end=" ")  
  k = k-1   
  for j in range(0, i + 1):  
    print("*", end=" ")
  print("")


# In[30]:


n = int(input())
print("*"*n, end="\n")
i = (n//2) - 1
j = 2
while i != 0:
  while j <= (n-2):
    print("*"*i, end="")
    print("_"*j, end="")
    print("*"*i, end="\n")
    i = i - 1
    j = j + 2


# In[ ]:





# In[ ]:


16

