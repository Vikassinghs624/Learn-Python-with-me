#!/usr/bin/env python
# coding: utf-8

# In[1]:


a= int(input("enter the first number"))
b = int(input("enter the second number"))
c =a/b
print(c)


# In[ ]:


#why should we use exception handling
#Answer: 1. it will stop further execution of code 
#2. it is not user friendly as we will be getting the error which will not be intrepreted by user. 
# We will be using five keyword in order to handle the exception handinling
   # try
   # except
   #else
   #raise
   #final
    


# In[8]:


a= int(input("enter the first number"))
b = int(input("enter the second number"))
try:
    c =a/b
except ZeroDivisionError:
    print("b should not be a zero")
    

print(e)


# In[13]:


a = int(input("enter the first number"))
b = int(input("enter the second number"))
try:
    c =a/b
    print(c)
except:
    print("Wrong syntax")
    

print(e)


# In[14]:


a = input("enter the first number")
b = input("enter the second number")
try: 
    c =int(a)/int(b)
    print(c)
except ZeroDivisionError:
    print("b should not be 0")
except: 
    print("enter the integer value")

    
    


# In[17]:


a = input("enter the first number")
b = input("enter the second number")
try: 
    c =int(a)/int(b)
    print(c)
    d=a+b
    print(d)
except ZeroDivisionError:
    print("b should not be 0")
except ValueError: 
    print("enter the integer value")


# In[20]:


while True:
    try:
        a=int(input("enter the first number"))
        b=int(input("enter the second number"))
        c=a/b
        print(c)
        break
    except ValueError:
        print("please enter the number in integer format")
    except ZeroDivisionError:
        print("Value should not be Zero")


# In[ ]:


import sys
while True:
    try:
        a= int(input("enter the first number"))
        b=int(input("enter the second number"))
        c=a/b
        print("div:",c)
        break
    except:
        a,b,c=sys.exc_info()
        print("exception class",a)
        print("exception message",b)
        print("line number",c.tb_lineno)
        


# In[22]:


import sys
while True:
    try:
        a= int(input("enter the first number"))
        b=int(input("enter the second number"))
        c=a/b
        print("div:",c)
        break
    except ZeroDivisionError as e:
        print(e)


# In[2]:


#traceback
import traceback
while True:
    try:
        a= int(input("enter the first number"))
        b=int(input("enter the second number"))
        c=a/b
        print("div:",c)
        break
    except:
        print(traceback.format_exc())
        


# In[1]:


while True:
    try:
        a= int(input("enter the first number"))
        b=int(input("enter the second number"))
        if a<0 or b<0:
            raise Exception("negative number is not allowed")
        c=a/b
        print("div is ",c)
        break
    except ValueError:
            print("Please provide the integer value only")
    except ZeroDivisionError:
        print("Please enter the non zero denominator value")
    except Exception as e:
        print(e)


# In[7]:


try:
    a= int(input("enter the first number"))
    b=int(input("enter the second number"))
    if a<0 or b<0:
        raise Exception("negative number is not allowed")
    c=a/b
    print("div is ",c)
    
except ValueError:
    print("Please provide the integer value only")
except ZeroDivisionError:
    print("Please enter the non zero denominator value")
except Exception as e:
    print(e)
else:
    print("Finally we have reached over here")


# In[ ]:




