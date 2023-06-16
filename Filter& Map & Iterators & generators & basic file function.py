#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=[1,2,3,45,6]
for i in l:
    print(i)


# In[2]:


next(l)


# In[4]:


#if the object is iterable then it can become the iterators

next(45)


# In[5]:


iter(45)


# In[6]:


#list item is iterable not iterator by default
for i in 4566:
    print(i)


# In[7]:


s="vikas"
next(s)


# In[8]:


b= iter(s)


# In[10]:


next(b)


# In[11]:


s="vikas"
b= iter(s)
next(b)


# In[12]:


def square_fun(n):
    x=[i*i for i in range(n)]
    return x
square_fun(5)


# In[13]:


list(range(4))


# In[15]:


def square_fun2(n):
    x=[i*i for i in range(n)]
    yield x
square_fun2(6)


# In[16]:


for j in square_fun(5):
    print(j)


# In[18]:


def genfin(n):
    a=1
    b=1
    l=[]
    for i in range(n):
        l.append(a)
        a,b= b,a+b
    return l
genfin(5)


# In[20]:


def genfin(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b= b,a+b
 


# In[21]:


def fib(n):
    if n==1 or n==0:
        return n
    else:
        result= n+fib(n-1)
        return result
fib(3)


# In[22]:


next(5)


# In[25]:


#file operation
f=open("music/vikas.txt",'r')
print(f.read())


# In[31]:


f=open("music/vikas.txt",'w')
f.write("vikas here you for writing by python")


# In[33]:


f=open("music/vikas.txt",'w')
l=[1,2,5,465]
f.write(str(l))
f.close()


# In[34]:


f3= open("vikas2.txt",'w')
f3.write("Vikas singh sikarwar ")
f3.close()


# In[35]:


get_ipython().run_cell_magic('writefile', 'test5.text', 'this is my python program\n')


# In[36]:


f.read()


# In[37]:


f4 =open("vikas4.txt",'w')
f4.write("here you go arsn sfidfv ldsgs adfg.adf gofgdfg adfgdfgdf dffadfsf dfg dfl;kng dfg dfg")
f4.close()


# In[38]:


f5=open("vikas4.txt")
f4.read()


# In[39]:


f4.name


# In[40]:


f4.close


# In[41]:


f4.mode


# In[42]:


f4.closed


# In[43]:


f4.seek(5)


# In[45]:


f= open("vikas4.txt")
print(f.read())


# In[46]:


f.seek(5)


# In[47]:


f.tell()


# In[48]:


print(f.read(25))


# In[49]:


f.close()


# In[50]:


print(f.read())


# In[51]:


l =[1,2,3,4,5]
l1=[]
for i in l:
    l1.append(i**2)
print(l1)


# In[52]:


#map function will map on each element over the iterable or sequence & given the value on it. 

l =[1,2,3,4,5]
def sqr(n):
    return n**2
list(map(sqr,l))


# In[55]:


#Reduce function takes first argument which is function other one is sequence & make sure that function should always take two argument otherwise it will throw the error
from functools import reduce
reduce(lambda a,b:a*b,l)


# In[56]:


reduce(lambda a,b,c:a*b,l)#throwing the error as we have taken the consideration of third argument


# In[1]:


#Filter function : it will try to filter out the dataset on specific condition
l5 =[1,2,65,46,5,6]
list(filter(lambda x: x%2==0, l5))


# In[1]:


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nEven numbers from the said list:")
even_nums = list(filter(lambda x: x%2 == 0, nums))
print(even_nums)
print("\nOdd numbers from the said list:")
odd_nums = list(filter(lambda x: x%2 != 0, nums))
print(odd_nums)


# In[ ]:




