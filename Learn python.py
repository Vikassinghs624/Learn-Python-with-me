#!/usr/bin/env python
# coding: utf-8

# In[1]:


set1 ={"UK","US","Germany"}
print(set1)


# In[2]:


#Set can not have duplicates value 
set1 ={"UK","US","Germany","Germany"}
print(set1)
print(len(set1))


# In[3]:


#Once the union will be executed then its output will be updated in new set3 
set1 ={"UK","US","Germany","Germany"}
set2 = {10,20,30,50}
set3 = set2.union(set2)
print(set3)


# In[4]:


# once the update will be executed then its output will be updated in existing set1
set1 ={"UK","US","Germany","Germany"}
set2 = {10,20,30,50}
set1.update(set2)
print(set1)


# In[5]:


row = 6
for i in range(row):
    for j in range(i):
        print("*", end ="")
    print()


# In[6]:


row = 6
for i in range(row-1,0,-1):
    for j in range(i):
        print("*",end="")
    print()


# In[7]:


## Once the intersection_update execution will be done then its output will be updated in existing set1

set1 ={"UK","US","Germany","Germany"}
set2 ={"KSA","Italy","Germany","india"}
set1.intersection_update(set2)
print(set1)


# In[8]:


# Once the intersection execution will be done then its output will be created in new set3
set1 ={"UK","US","Germany",}
set2 ={"KSA","Italy","Germany","india"}
set3 = set1.intersection(set2)
print(set3)


# In[9]:


#Just to keep only the Unique values
set1 ={"UK","US","Germany"}
set2 ={"KSA","Italy","Germany","india"}
set1.symmetric_difference_update(set2)
print(set1)


# In[10]:


set2 ={"KSA","Italy","Germany","india"}
for j in set2:
    print(j)


# In[18]:


dic1 ={"name":"Vikas", "Age":28,"City":"Banglore","City":"delhi","City":"mumbai"}
print(dic1)
print(dic1.keys())
ky = dic1.keys()
dic1["name"] ="Anju"
print(dic1)
for i in ky:
    print(i)


# In[15]:


# dic() constructor
d1 = dict(name="vikas", age =28)
print(d1)


# In[23]:


#Update the specific key with another value or you can add the new key-value pair to it.
dic1 ={"name":"Vikas", "Age":28,"City":"Banglore"}
dic1["City"] ="berlin"
dic1["job"] ="Data Analyst"
print(dic1)
dic1.update({"City":"NewYork"})#if the key is not there then it will add a key and value otherwise it updates the existing key
print(dic1)


# In[27]:


# del is used to delete the specific key-value pair & otherwise if you do not assign any key to it then it will delete the entire dictionary
dic1 ={"name":"Vikas", "Age":28,"City":"Banglore"}
print(dic1)
del dic1["Age"]
print(dic1)


# In[26]:


#Clear function will the clear the data from dictionary 
dic1 ={"name":"Vikas", "Age":28,"City":"Banglore"}
print(dic1)
dic1.clear()
print(dic1)


# In[32]:


# Loop in dictionary
dic1 ={"name":"Vikas", "Age":28,"City":"Banglore"}
for key in dic1: # for loop on the value of dictionary
    print(dic1[key])
for key in dic1:# for loop on the key of dictionary
    print(key)


# In[33]:


#copy methods
dic1 ={"name":"Vikas", "Age":28,"City":"Banglore"}
dic2 = dic1.copy()
print(dic2)


# In[37]:


#Nested dictionary
d ={ "user1": {"name":"Vikas", "Age":28}, "user2":{"name":"Amit","Age":27}, "user3": {"name":"Vian","Age":24}}
print(d)


# In[39]:


print(d["user3"]["Age"])


# In[41]:


#User defined function
def MyFirstFunction():
    """
    This will print the output
    """
    print("Hello...................")
#Calling the function
MyFirstFunction()


# In[42]:


print(int(5/2))


# In[ ]:


# Check the prime number
def is_check_prime(n):
    if n < 1:
        print(f"{n} is not prime number")
    else:
        for i in range(2,n):
            if n%i==0:
                print(f"{n} is not prime number")
                break
        else:
                print(f"{n} is a prime number")
                
n = int(input("please provide the number to check whether it is prime or not"))
is_check_prime(n)


# In[ ]:


#User defined function to add two values
def add(a,b):
    c =a+b
    print(f"addition of two value is {c}")
a = int(input("enter the value of a"))
b = int(input("enter the value of b"))
add(a,b)


# In[47]:


add(4,5)


# In[2]:


# Check the prime number
def is_check_prime(n):
    if n < 1:
        print(f"{n} is not prime number")
    else:
        for i in range(2,n):
            if n%i==0:
                print(f"{n} is not prime number")
                break
        else:
            print(f"{n} is a prime number")
            
    
                
n = int(input("please provide the number to check whether it is prime or not"))
is_check_prime(n)


# In[ ]:





# In[ ]:




