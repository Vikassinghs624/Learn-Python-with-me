#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

#Read the excel file & it will give the DataFrame
df = pd.read_excel('V:\database/Attribute Dataset.xlsx')
df


# In[5]:


#type of output
print(type(df))


# In[11]:


#read the excel work book separately otherwise by defaul it will read first sheet in workbok in excel
df1= pd.read_excel("V:\database/Dress Sales.xlsx",sheet_name="data3")
df1


# In[15]:


#by default first row would be considered as Header or column header as mentioned above cells
df2= pd.read_excel("V:\database/Dress Sales.xlsx",sheet_name="data3",header=None,names=["A","B","C"])
df2


# In[17]:


#head() function will give first 5 row or record
df.head()


# In[18]:


#tail() function will last 5 record or row
df.tail()


# In[21]:


# read the csv file
df3 = pd.read_csv('V:\database/haberman.csv',sep="@")
df3


# In[23]:


#read the data from github repository
pd.read_csv("https://github.com/selva86/datasets/blob/master/Smarket.csv")


# In[25]:


#Read the html file 
a = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2015_totals.html")
a


# In[27]:


type(a)


# In[28]:


a[0]


# In[31]:


#Read a JSON file 
js=pd.read_json("https://api.github.com/repos/pandas-dev/pandas/issues")
js


# In[35]:


js.columns


# In[36]:


js["user"][0]


# In[7]:


df = pd.read_excel('V:\database/Attribute Dataset.xlsx')
df


# In[38]:


df.to_json("attribute.json")


# In[39]:


pwd


# In[6]:


df.to_csv("V:/database/attribute.csv",sep="#",index=False)


# In[ ]:


#MYSQL
1. Create a table attribute dataset and dress dataset
2. Do a bulk load for these two table for respective dataset
3. read these dataset in pandas as a dataframe for both table which you have created in step 2
4. Convert attribute dataset in json format
5. store this dataset into mongodb
6. in sql task try to perform left join operation with attribute dataset and dress dataset on column Dress_ID
7. write a sql query to find out how many unique dress that we have based on dress id
8. try to find out how many dress is having recommendation is 0
9. try to find total dress sell for individual dress id
10. try to find out a third highest most selling dress


# In[8]:


#check the type of each column to perform arithmetic operation
df.dtypes


# In[9]:


df.columns


# In[10]:


df


# In[18]:


#want to access single column from dataframe
df["Dress_ID"]


# In[17]:


print(type(df["Dress_ID"]))


# In[22]:


#want to access more than one column from data frame
df5=df[["Dress_ID","Style"]]
df5


# In[23]:


type(df5)


# In[27]:


df[["Dress_ID"]]


# In[28]:


df.keys()


# In[29]:


#find the all sheet name in workbook
df.sheet_names


# In[33]:


df = pd.read_excel('V:\database/Attribute Dataset.xlsx',sheet_name=None)
df


# In[45]:


type(df.keys())


# In[48]:


for i in list(df.keys()):
    d = pd.read_excel('V:\database/Attribute Dataset.xlsx',sheet_name=i)
    print(d)


  
    


# In[49]:


ls


# In[50]:


import os
os.getcwd()


# In[62]:


d="""{
    "name":"Vikas Singh",
    "email":"vikas@google.com",
    "tech":["ML","DL","CV"],
    "Platform":["techneuron","idsneuron","ineuron"]
}"""


# In[63]:


# Conversion to json data 
import json

result= json.loads(d)


# In[64]:


result


# In[57]:


type(result)


# In[60]:


type(d)


# In[65]:


#Convert json data to DataFrame in which make sure length of list in dict should be same otherwise it will throw the error
pd.DataFrame(result)


# In[66]:


pd.DataFrame(result["name"])


# In[67]:


pd.DataFrame(result["tech"])


# In[68]:


d = {"packetType":"D","data":{"checkEngineLightFlag":"F","batteryVoltageStableTime":0,"batteryVoltageStable":"0","batteryVoltageOff":"12.42","batteryCrankParamTN":"-0.08","batteryCrankParamVN":"0.00","batteryCrankParamTP":"-0.08","batteryCrankParamVP":"0.00","batteryCrankParamTT":"-0.00008","batteryCrankParamV0":"0.00","batteryVoltageMaxOn":"13.05","batteryVoltageMinOn":"12.97","batteryVoltageMaxOff":"12.46","batteryVoltageMinOff":"12.36","batteryVoltageOnAverage":"13.02","engineLoadMax":"84","engineLoadAverage":"39.98","rpmMax":"3487","rpmAverage":"1431.29","gpsSpeedAverage":"21.99","vssMax":"53.44","vssAverage":"23.06","tcuTemperatureMin":"82.40","tcuTemperatureMax":"109.40","tcuTemperatureAverage":"104.87","coolantMin":"158.00","coolantMax":"188.60","coolantAverage":"180.20","packetStartLocal":1508143346000,"tripStartLocal":1508143346000,"milIndicator":"F","monitorsNotReady":0,"imei":"60DF5417","gatewayTs":1515613306592,"diagnosticTroubleCodeData":[],"diagnosticPidData":[[64768,47,100],[64768,1,517376],[64800,1,262144],[64768,5,125]]},"header":{"iwrapVer":"1.9.20","sourceSystem":"CDP","configVer":"1.1","oemName":"HUM","unitType":0,"cpVer":"7.50.1.9","igpsVer":"1.3.7","messageType":"Notification","pomVer":"1.0","headerVer":"V6","timestamp":0,"deviceType":"InDrive","visorVer":"1.4.35","transactionId":"53098471-7787-4160-94b3-cd69dcc70416","deviceSerialNo":"60DF5417","subOrganization":"HUM","organization":"HUM","imei":"60DF5417","operation":"Notification"}}


# In[74]:


d2=pd.DataFrame(d)
d2["data"]


# In[75]:


del d2["data"]["diagnosticTroubleCodeData"]


# In[76]:


d2["data"]


# In[77]:


d2["data"]["diagnosticPidData"]


# In[79]:


#read a json file
j=pd.read_json("https://api.github.com/repos/pandas-dev/pandas/issues")
j


# In[80]:


import requests
conn=requests.get("https://api.github.com/repos/pandas-dev/pandas/issues")
conn


# In[81]:


data=conn.json()


# In[82]:


data


# In[84]:


len(data)


# In[90]:


for i in range(len(data)):
    print(data[i]["user"]['url'])


# In[94]:


user5=pd.DataFrame(data,columns=["url",'repository_url','labels_url',"user"])
user5


# In[98]:


user5["user"].to_dict


# In[ ]:




