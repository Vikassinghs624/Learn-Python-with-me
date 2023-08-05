#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


l=["Vikas",15,6,78,9,8]
np.array(l)


# In[3]:


np.array([1,5,6,8,3.5])


# In[5]:


a=np.array([[1,5],[4,8]])
a


# In[6]:


a[0][0]


# In[7]:


a[1][1]


# In[8]:


np.asarray([1,5,6,68,8])


# In[9]:


np.asanyarray([58,8,9,9,78])


# In[10]:


np.mat([1,5,9,9,9,21])


# In[12]:


np.asanyarray(np.mat([1,5,6,6,9]))


# In[13]:


np.fromfunction(lambda i,j: i==j,(3,3))


# In[14]:


np.fromfunction(lambda i,j: i*j,(4,4))


# In[16]:


np.fromfunction(lambda i,j,k: i*j*k,(3,4,2),dtype=int)


# In[18]:


np.fromfunction(lambda i,j,k,p: i*j*k*p,(3,2,4,2),dtype=int)


# In[19]:


a=np.fromfunction(lambda i,j,k: i*j*k,(3,4,2),dtype=int)
a


# In[20]:


a.ndim


# In[21]:


a.shape


# In[22]:


a.size


# In[23]:


a.dtype


# In[26]:


a=np.fromfunction(lambda i,j: i*j,(400,2),dtype=int)
a


# In[28]:


import pandas as pd
pd.DataFrame(a)


# In[29]:


np.random.rand(4,5)


# In[30]:


np.random.randint(4,50)


# In[31]:


np.random.randn(4,5)


# In[32]:


a=np.fromfunction(lambda i,j,k: i*j*k,(3,4,2),dtype=int)
a.reshape(6,4)


# In[33]:


pd.DataFrame(a.reshape(6,4))


# In[41]:


a.reshape(4,2,-1)


# In[40]:


a.reshape(6,2,-1566)


# In[42]:


list(range(4,10,2))


# In[43]:


list(range(4,12,0.2))


# In[47]:


b=np.arange(4,12,0.2)
b


# In[48]:


b[2:4]


# In[52]:


arr=np.random.rand(4,5)
arr


# In[53]:


arr[arr>0.5]


# In[54]:


arr[[1,2],[2]]


# In[55]:


arr[1:3,0:2]


# In[58]:


a=np.array([[1,2],[3,4]])
a


# In[59]:


b=np.array([[2,8],[2,5]])
b


# In[64]:


m=a@b
m


# In[63]:


m/0


# In[1]:


import numpy as np
np.zeros(5)


# In[2]:


np.zeros([3,4])


# In[4]:


np.zeros([3,4,5])


# In[5]:


np.ones([3,4])


# In[6]:


np.ones([2,4,2])


# In[7]:


4+np.zeros([2,4])


# In[8]:


np.empty([2,4])


# In[9]:


np.empty([2,4,3])


# In[12]:


np.linspace(2,6)


# In[13]:


np.linspace(2,6,10)


# In[17]:


a=np.linspace(2,6,10)
a


# In[18]:


a.reshape([2,5])


# In[19]:


#upper bound value will not be considered if you mark endpoint false
a=np.linspace(2,6,10,endpoint=False)
a


# In[20]:


#stepsize can be known by mentioning retstep as true
a=np.linspace(2,6,10,endpoint=False,retstep=True)
a


# In[23]:


np.logspace(2,4,10,base=10,endpoint=False)


# In[26]:


b=np.arange(4,40).reshape(6,6)
b


# In[27]:


b.max(axis=0)


# In[28]:


b.max(axis=1)


# In[29]:


b**2


# In[30]:


pow(b,2)


# In[31]:


a+b


# In[37]:


a=np.linspace(2,6,6)
a.reshape(1,-1).T


# In[38]:


a+b


# In[39]:


b


# In[40]:


np.sqrt(b)


# In[41]:


np.exp(b)


# In[42]:


np.log10(b)


# In[43]:


x=np.array([1,2,3])


# In[44]:


y=x


# In[45]:


y


# In[46]:


x


# In[47]:


z=np.copy(x)


# In[48]:


x[0]=100


# In[49]:


y


# In[50]:


z


# In[52]:


id(x)


# In[53]:


id(y)


# In[54]:


id(z)


# In[55]:


id(x[0])


# In[56]:


id(y[0])


# In[57]:


id(z[0])


# In[59]:


id(z[0])==id(y[1])


# In[ ]:




