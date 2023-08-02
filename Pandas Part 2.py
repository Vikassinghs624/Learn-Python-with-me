#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df


# In[ ]:





# In[4]:


type(df)


# In[5]:


df.head(4)


# In[6]:


df.head(4)


# In[7]:


df.tail()


# In[14]:


df.dtypes =="object"


# In[9]:


df.info()


# In[10]:


df.describe()


# In[16]:


list(df.columns[df.dtypes=="object"])


# In[18]:


list(df.dtypes[df.dtypes=="object"].index)


# In[19]:


df[df.columns[df.dtypes=="object"]]


# In[21]:


df[df.columns[df.dtypes=="object"]].describe()


# In[24]:


df["ineuron"]="Vikas"


# In[25]:


df


# In[27]:


df["Name"]


# In[33]:


df["Name"][::-1]


# In[39]:


df["Age"].isnull() ==True


# In[40]:


df[df["Age"].isnull() ==True]


# In[41]:


df[df["Age"].isnull() ==True].describe()


# In[42]:


df[df["Age"].isnull() ==True].index


# In[46]:


df.loc[df[df["Age"].isnull() ==True].index]


# In[49]:


df[df["Age"].isnull()]


# In[53]:


df["Fare"].max()


# In[57]:


df[df["Fare"]==df["Fare"].max()]["Name"]


# In[61]:


df["Sex"].count()


# In[63]:


#Find out how many male passenger we have

df[df["Sex"]=="male"]["Name"].count()


# In[172]:


df["Sex"].value_counts()


# In[64]:


#Find out how many female passenger we have
df[df["Sex"]=="female"]["Name"].count()


# In[66]:


#How many Survivor we have 
df[df["Survived"]==1]["Name"].count()


# In[ ]:


#How many casuality we have 
df[df["Survived"]==0]["Name"].count()


# In[67]:


df[df["Age"].max()==df["Age"]]["Name"]


# In[68]:


#How many passenger do we have in first class
df[df["Pclass"]==1]["Name"].count()


# In[69]:


#How many passenger do we have in Second class
df[df["Pclass"]==2]["Name"].count()


# In[70]:


#How many passenger do we have in Third class
df[df["Pclass"]==3]["Name"].count()


# In[177]:


#How many person we have whose name starts with "s"
df


# In[171]:


#Try to create a new column which is summation of "SibSp" and "parch"
df["PaSi"]=df["Parch"]+df["SibSp"]
df


# In[137]:


#how many person do we have below age of 25
len(df[df["Age"]<25]["Age"])


# In[ ]:





# In[183]:


#how many person died whose age was less than 40
len(df[(df["Survived"]==0) & (df["Age"]<40)])


# In[152]:


#from a cabin column seperate text & Numeric value
df["Cabin"]


# In[185]:


df["Str_cabin"]=df["Cabin"].str.replace((A-za-z),"")


# In[87]:


#New data set to practice Purpose
import pandas as pd1
df2=pd1.read_csv("V:\Bank.csv",sep=";")
df2


# In[102]:


#How many compaign available in this dataset
len(list(df2['campaign'].unique()))


# In[107]:


#How many users do we have with housing & Personal loan
len(df2[df2["housing"]=="yes"]["loan"]=="yes")


# In[110]:


#how many person do we have whose age is more than 60
len(df2[df2["age"]>60]["age"])


# In[ ]:


#which month we have received most of that customer


# In[115]:


#which mode of call is giving the result
len(df2[df2["contact"]=="cellular"]["contact"])
#Answer: Cellular


# In[116]:


len(df2[df2["contact"]=="unknown"]["contact"])


# In[118]:


df2["contact"].unique()


# In[119]:


len(df2[df2["contact"]=="telephone"]["contact"])


# In[120]:


df2=pd1.read_csv("V:\Bank.csv",sep=";")
df2


# In[124]:


#How many Entrepreneur do we have in the list
len(df[df2["job"]=="entrepreneur"])


# In[126]:


#how many customer do we have in the list whose balance is negative
len(df2[df2["balance"]<0]["balance"])


# In[130]:


#Prepare the group of data based on the education level
ed = df2.groupby("education")


# In[132]:


ed.first()


# In[178]:


import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df


# In[181]:


df[df["Name"].str.startswith("S")]["Name"]


# In[3]:


import pandas as pd
df2=pd.read_csv("V:\Bank.csv",sep=";")
df2


# In[9]:


d= df2.groupby(["contact","y"]).count()
d


# In[14]:


d.loc["cellular","yes"][0]


# In[13]:


d.loc["telephone","yes"][0]


# In[12]:


d.loc["unknown","yes"][0]


# In[15]:


max(d.loc["cellular","yes"][0],d.loc["telephone","yes"][0],d.loc["unknown","yes"][0])


# In[17]:


df2["education"].unique()


# In[24]:


l=[]
for i in df2["education"].unique():
    l.append(df2[df2["education"]==i])


# In[25]:


for j in l:
    print(j)


# In[26]:


import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df


# In[27]:


df.dropna()


# In[30]:


df.dropna()


# In[31]:


df


# In[28]:


df=df.dropna()


# In[29]:


df


# In[32]:


df.dropna(axis=1)


# In[33]:


import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df.dropna(axis=1)


# In[35]:


df.dropna(inplace=True)


# In[36]:


import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df


# In[38]:


df.dropna(inplace=True)
df


# In[39]:


df


# In[40]:


df.isnull()


# In[43]:


import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df.isnull().sum()


# In[46]:


df.dropna(axis=1,how="all")


# In[47]:


df.fillna(value="vik")


# In[52]:


f=df.fillna(value=df["Age"].mean())
f


# In[53]:


f["Age"].isnull()


# In[55]:


df.groupby("Survived").describe()["PassengerId"]


# In[56]:


df.groupby("Survived").describe()["PassengerId"].T


# In[57]:


l=[]
for i in df2["education"].unique():
    l.append(df2[df2["education"]==i])


# In[59]:


Df1=l[0].head()
Df2=l[1].head()


# In[61]:


pd.concat([Df1,Df2])


# In[63]:


Df1=Df1[["education","balance","contact"]]
Df2=Df2[["education","balance","contact"]]


# In[66]:


df5=pd.concat([Df1,Df2],axis=1)
df5


# In[68]:


df5["balance"]


# In[72]:


df5.iloc[[4,5],[0,5]]


# In[76]:


Df1=Df1[["education","balance","contact"]]
Df2=Df2[["education","balance","contact"]]


# In[78]:


pd.merge(Df1,Df2, on="balance")


# In[79]:


Df1=l[0].head()
Df2=l[1].head()


# In[80]:


Df1


# In[81]:


Df2


# In[82]:


pd.merge(Df1,Df2, on="age")


# In[83]:


pd.merge(Df1,Df2,on="age",how="right")


# In[84]:


pd.merge(Df1,Df2,on="age",how="outer")


# In[85]:


Df1


# In[88]:


Df2 = Df2.set_index("age")
Df1 = Df1.set_index("age")


# In[92]:


Df1=Df1[["job","marital"]]
Df1


# In[93]:


Df2=Df2[["job","marital"]]
Df2


# In[95]:


Df2=Df2.rename(columns={"job":"job1","marital":"marital1"})
Df2


# In[97]:


Df1.join(Df2,on='age')


# In[98]:


Df1.join(Df2,on='age',how="inner")


# In[101]:


import pandas as pd
t=pd.DataFrame({"col1":[1,2,3,4,5],
             "col2":[15,48,6,89,9],
             "col3":"Vikas singh sikarwar rajput Dholpur".split(" ")
             })
t


# In[104]:


t["col4"]=t["col1"]**2


# In[105]:


t


# In[106]:


t["col5"]=t["col3"].str[0]


# In[107]:


t


# In[108]:


t[t["col5"].str[0]=="s"]


# In[110]:


sqr =lambda x: x**2
t["col4_4"]=t["col1"].apply(sqr)


# In[111]:


t


# In[112]:


def dchange(str):
    if str =="s":
        return "s"
    else:
        return "z"


# In[115]:


t["col6"]=t["col5"].apply(dchange)
t


# In[116]:


t["col6_6"]=t["col6"].apply(lambda a: "s" if a=="s" else "z")
t


# In[118]:


t["col7"]=t["col3"].apply(len)
t


# In[122]:


import math
t["col8"]=t["col2"].apply(math.log)
t
                          


# In[ ]:




