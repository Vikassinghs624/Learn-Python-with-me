#!/usr/bin/env python
# coding: utf-8

# In[1]:


def introduction():
    print("Hello, This is my first function")
introduction()


# In[3]:


def intro(first_name):
    print(first_name+", How are you?")
intro("Vikas")


# In[6]:


s="this is My First Python programming class and i am learNING python string and its function"
#1 . Try to extract data from index one to index 300 with a jump of 3 
print(s[1:300:3])


# In[7]:


#2. Try to reverse a string without using reverse function 
print(s[::-1])


# In[9]:


#3. Try to split a string after conversion of entire string in uppercase 
print(s.upper().split())


# In[10]:


#4. try to convert the whole string into lower case 
print(s.lower())


# In[11]:


#Try to capitalize the whole string 
print(s.capitalize())


# In[15]:


#Write a diference between isalnum() and isalpha()
s1 = "sud45hfsdf"
s1.isalnum()


# In[14]:


s1 = "sudhf45df"
s1.isalpha()# if string  is present in the variable then it will give you True otherwise it will not 


# In[ ]:


# Try to give an example of expand tab


# In[19]:


num1 = int(input("please enter the number 1 :"))
num2 = int(input("please enter the number 2 :"))
def add(t1, t2):
    return t1+t2
def sub(t1, t2):
    return t1-t2
def mul(t1, t2):
    return t1*t2
def div(t1, t2):
    return t1/t2
print(f"Addition of two value would be:{add(num1,num2)}")
print(f"Subtraction of two value would be:{sub(num1,num2)}")
print(f"Multiplication of two value would be:{mul(num1,num2)}")
print(f"division of two value would be:{div(num1,num2)}")


# In[21]:


def calculator():
    num1 = int(input("please enter the number 1 :"))
    num2 = int(input("please enter the number 2 :"))
    #add
    sum_result = num1+num2
    #diff
    sub_result = num1-num2
    #mul
    mul_result = num1*num2
    #div
    div_result = num1/num2
    return {
        "sum": sum_result,
        "sub": sub_result,
        "mul": mul_result,
        "div": div_result
    }
results = calculator()
print("Addition of two value would be:", results["sum"])
print("Subtraction of two value would be:", results["sub"])
print("Multiplication of two value would be:",results["mul"])
print("division of two value would be:",results["div"])


# In[23]:


def capitilize(str):
    print(str.title())
st = input("please provide the string to capitilize")
capitilize(st)


# In[24]:


#Lambda function
add = lambda x,y: x+y
print(add(5,4))


# In[25]:


concat = lambda x,y:x+y
print(add("Vikas", " Singh"))


# In[27]:


odd_even_check = lambda x: "even" if x%2==0 else "odd"
print(odd_even_check(5))


# In[28]:


max_number = lambda x,y: x if x>y else  y
print(max(6,9))


# In[35]:


str = "Vikas\tsingh\tsikarwar"
print(str.expandtabs())


# In[36]:


str = "     vikas     "
print(str.lstrip())
print(str.rstrip())
print(str.strip())


# In[39]:


s = "Vikas"
print(s.replace("Vikas", "Anju"))


# In[40]:


c = "Vikas"
c.center(10,"b")


# In[42]:


for i in range(5):
    for j in range(i+1):
        print("ineuron", end=" ")
    print("\r")


# In[52]:


k = 2
for i in range(5): 
    for j in range(k):
        print(end= " ")
    for h in range(k+1):
        print("i", end=" ")
    k-=1
    print("\r")


# In[55]:


l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
# Try to extract all the list entity
list_item = []
for i in l:
    if type(i) == list:
        list_item.append(i)
print(list_item)
        


# In[56]:


# Try to extract all the dict entity
list_item = []
for i in l:
    if type(i) == dict:
        list_item.append(i)
print(list_item)
        


# In[57]:


# Try to extract all the tuple entity
list_item = []
for i in l:
    if type(i) == tuple:
        list_item.append(i)
print(list_item)


# In[71]:


# Try to extract all the numerical data it may b a part of dict key and values 
l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
list_item = []
for i in l:
    if type(i) == tuple or type(i) == list or type(i) == set :
        for j in i:
            if type(j)== int:
                list_item.append(j)
    if type(i) == dict :
        for m in i.items():
            if type(m)== int:
                list_item.append(m)
print(list_item)


# In[ ]:





# In[77]:


# Try to extract all the numerical data it may b a part of dict key and values 
l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
list_item = []
for i in l:
    if type(i) == tuple or type(i) == list or type(i) == set :
        for j in i:
            if type(j)== int:
                list_item.append(j)
    if type(i) == dict :
        for m in i.items():
            for n in m:
                if type(n)== int:
                    list_item.append(n)
print(list_item)


# In[84]:


#Try to give summation of all the numeric data 
sum= 0
for g in list_item:
    sum+=g
print(sum)


# In[85]:


#Try to filter out all the odd values out all numeric data which is a part of a list 
for k in list_item:
    if k %2!=0:
        print(k)


# In[99]:


#Try to extract "ineruon" out of this data
l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
list_item = []
for i in l:
    if type(i) == tuple or type(i) == list or type(i) == set :
        for j in i:
            if j == "ineuron":
                list_item.append(j)
    if type(i) == dict :
        for m in i.items():
            for n in m:
                if n == "inueron":
                    list_item.append(n)
print(list_item)


# In[98]:


#Try to extract "ineruon" out of this data
l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
list_item = []
for i in l:
    if type(i) == tuple or type(i) == list or type(i) == set :
        for j in i:
                list_item.append(j)
    if type(i) == dict :
        for m in i.items():
            for n in m:
                    list_item.append(n)
print(list_item)


# In[103]:


#Try to find out a number of occurances of all the data 
list_item = [1, 2, 3, 4, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 45, 4, 5, 23, 'k1', 'sudh', 'k2', 'ineuron', 'k3', 'kumar', 3, 6, 7, 8, 'ineuron', 'data science ']
for o in set(list_item):
    print(o," : ",list_item.count(o))
    


# In[109]:


#Try to find out number of keys in dict element
l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
list_item = []
for i in l:
    if type(i) == dict :
        print(len(i))
    


# In[106]:


dic= {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8}
list_item = []
for m in i.keys():
            print(m)


# In[1]:


# Try to extract all the numerical data it may b a part of dict key and values 
l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
list_item = []
for i in l:
    if type(i) == tuple or type(i) == list or type(i) == set :
        for j in i:
            if type(j)== str:
                list_item.append(j)
    if type(i) == dict :
        for m in i.items():
            for n in m:
                if type(n)== str:
                    list_item.append(n)
print(list_item)


# In[6]:


#Try to Find  out alphanum in data
l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
list_item = []
for i in l:
    if type(i) == tuple or type(i) == list or type(i) == set :
        for j in i:
                list_item.append(j)
    if type(i) == dict :
        for m in i.items():
            for n in m:
                    list_item.append(n)
for p in list_item:
    if type(p)== str:
        if p.isalnum():
            print(p)
    


# In[16]:


#Try to find out multiplication of all numeric value in the individual collection inside dataset
l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
list_item = []

for i in l:
    mul = 1
    if type(i) == tuple or type(i) == list or type(i) == set :
        for j in i:
            if type(j)== int:
                    mul = mul*j
        print(type(i),":",mul)
    if type(i) == dict :
        for m in i.items():
            for n in m:
                if type(n)== int:
                        mul *=n
        print(type(i),":",mul)


# In[17]:


#q1 : Try to print this by using while loop 


# In[19]:


row = 8
i= 1
while i<=8:
    print("*"*(i), end= " ")
    i+=1
    print("\r")


# In[1]:


text=  """Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[36]

Python consistently ranks as one of the most popular programming languagesc""" 


i = 0
v = 'aeiou'
text = text.lower()
def
while i<=len(text):
    if text[i] in v:
        print(text[i])
    i+=1
    


# In[2]:


#write a code to get a time of your system 
import datetime
print(datetime.datetime.now())


# In[3]:


#q8 : Write a code to fetch date form your system 
import datetime
print(datetime.datetime.now().date())


# In[5]:


#Write a code to send a mail to your friend 
import smtplib
Email ="vikassirwar1996@gmail.com"
Password ="pwfpxthonpksufgw"
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(Email,Password)
server.sendmail(Email,'gemswar45@gamil.com','TEST EMAIL from Python')

print('Mail sent')


# In[5]:


#write a code to trigger alarm for you at scheduled time 
get_ipython().system('pip install playsound')

import time
import playsound

alarm_time = '10:22'
if time.asctime()[11:-8] == alarm_time :
    absolute_path = os.path.abspath("texttovoice.mp3")
    print(absolute_path)
    playsound.playsound(absolute_path)


# In[8]:


# write a code to check ip address of your system
import socket 
host = socket.gethostname()
ip = socket.gethostbyname(host)
print(ip, host)


# In[10]:


#Write a code to check a perticular installation in your system
get_ipython().system(' pip install winapps')
import winapps
list(winapps.list_installed())


# In[12]:


#Write a code to convert any text in to voice 
import gtts
from playsound import playsound
def text_to_voice(str1):
    tts= gtts.Gtts(str1)
    tts.save("hello.mp3")
    playsound("hello.mp3")
text_to_voice("Vikas")


# In[13]:


#you have to write a fun which will take string and return a len of it without using a inbuilt  fun len
s ="vikas"
count =0
for i in s:
    count +=1
print(count)


# In[2]:


# Write a fun which will take input as a dict and give me out as a list of all the values even in case of 2 level nesting it should work
d = {'k1' :"value" , "k2" : "values " ,"k3" : { "k12" : "sudh" , "k13"  : "gafasd"}}
def dict_to_list(d):
    l =[]
    for i in d.values():
        if type(i) != dict:
            l.append(i)
        if type(i) == dict:
            for j in i.values():
                l.append(j)
    return l
dict_to_list(d)


# In[4]:


#q19 : write a function whihc will be able to read a image file and show it to you .
get_ipython().system('pip install opencv-python')
import cv2
def read_img():
    a = cv2.imread('V:\IMG_0675.JPG')
    cv2.imshow("myimg",a)
    cv2.waitKey(5000)
    cv2.destroyWindow('myimg')


# In[5]:


read_img()


# In[ ]:


#write a function which will be able to shutdonw your system

import os
  
shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")
  
if shutdown == 'no':
    exit()
else:
    os.system("shutdown /s /t 1")


# In[4]:


#print the alphbet pyramid pattern

n=7
i=1
while i<=n:
    j=1
    k=i
    while j<=i:
        print(chr(64+k), end=" ")
        k=k+n-j
        j=j+1
    print("\r")
    i+=1


# In[1]:


print(chr(65))


# In[6]:


for i in range(6):
    if i <=3:
        n=i
    else:
        n =6-i
    print(("ineuron "*n).center(30," "))


# In[ ]:




