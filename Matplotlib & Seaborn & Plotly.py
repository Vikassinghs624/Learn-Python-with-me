#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import matplotlib as plt
df= pd.DataFrame(np.random.randn(1000),columns=['data'],index=pd.date_range('2023/03/26',periods=1000))
df


# In[10]:


df.plot()


# In[11]:


df.plot(figsize=(20,10))


# In[12]:


d=pd.read_csv("https://raw.githubusercontent.com/venky14/Machine-Learning-with-Iris-Dataset/master/Iris.csv")


# In[13]:


d


# In[15]:


d.plot(figsize=(20,10))


# In[18]:


del d['Id']


# In[19]:


d


# In[21]:


d.plot(figsize=(20,10))


# In[22]:


d.plot(kind='bar',figsize=(20,10))


# In[26]:


d.iloc[5:11].plot(kind='bar',figsize=(20,10))


# In[27]:


d.iloc[:1].plot(kind='bar',figsize=(20,10))


# In[28]:


d.iloc[5:11].plot(kind='barh',figsize=(20,10))


# In[29]:


d.iloc[5:11].plot(kind='hist',figsize=(20,10))


# In[30]:


d["SepalLengthCm"].plot(kind="hist",figsize=(20,10))


# In[ ]:


d["SepalLengthCm"].plot(kind="hist",figsize=(20,10),)


# In[32]:


d.hist(figsize=(20,10),color='g')


# In[35]:


d.hist(figsize=(20,10),color='g',alpha=.1)


# In[36]:


d.plot(kind='box',figsize=(20,10))


# In[37]:


d.describe()


# In[39]:


d.plot(kind='box',figsize=(20,10),color={'boxes':'g','whiskers':'r'})


# In[40]:


d.plot(kind='box',figsize=(20,10),color={'boxes':'g','whiskers':'r'},vert=False)


# In[41]:


d.plot(kind="area",figsize=(20,10))


# In[47]:


d.plot(kind='area',figsize=(20,10),alpha=.4,stacked=True)


# In[48]:


d


# In[50]:


d.plot.scatter(x="SepalLengthCm",y='PetalLengthCm',c='SepalWidthCm')


# In[59]:


d.plot.scatter(x="SepalLengthCm",y='PetalLengthCm',c='SepalWidthCm',s=d['PetalWidthCm']*500)


# In[56]:


d


# In[71]:


del d["Species"]


# In[ ]:





# In[72]:


d.iloc[0]


# In[70]:


d.iloc[0].plot(kind='pie')


# In[73]:


get_ipython().system('pip install plotly')


# In[1]:


import cufflinks as cf


# In[3]:


get_ipython().system('pip install cufflinks')


# In[4]:


import cufflinks as cf


# In[6]:


d


# In[8]:


import pandas as pd
d=pd.read_csv("https://raw.githubusercontent.com/venky14/Machine-Learning-with-Iris-Dataset/master/Iris.csv")


# In[9]:


d


# In[10]:


d.iplot()


# In[11]:


cf.go_offline()


# In[14]:


del d['Id']


# In[15]:


d


# In[18]:


d.iplot()


# In[19]:


d.iplot(x='SepalLengthCm',y='PetalLengthCm',mode='markers')


# In[23]:


d.iplot(mode='markers',kind='scatter',size=4)


# In[25]:


d.iplot(kind='bubble',x='SepalLengthCm',y='PetalLengthCm',size='SepalWidthCm')


# In[26]:


d.scatter_matrix()


# In[27]:


d


# In[29]:


d.iplot(kind='scatter3d',x='SepalLengthCm',y='PetalLengthCm',z='SepalWidthCm')


# In[30]:


d.head().iplot(kind='scatter3d',x='SepalLengthCm',y='PetalLengthCm',z='SepalWidthCm')


# In[1]:


import seaborn as sns


# In[2]:


import pandas as pd
d=pd.read_csv("https://raw.githubusercontent.com/venky14/Machine-Learning-with-Iris-Dataset/master/Iris.csv")


# In[3]:


d


# In[7]:


sns.scatterplot(x=d.SepalLengthCm,y=d.PetalLengthCm)


# In[6]:


import matplotlib.pyplot as plt


# In[10]:


plt.plot(d.SepalLengthCm,d.PetalLengthCm,'o')


# In[12]:


plt.plot(d.SepalLengthCm,d.PetalLengthCm,'o')
plt.xlabel('sep_length')
plt.ylabel('petal_length')


# In[14]:


plt.hist(d.SepalLengthCm,alpha=0.5)


# In[15]:


sns.distplot(d.SepalLengthCm)


# In[17]:


d1=sns.load_dataset('tips')
d1


# In[18]:


sns.scatterplot(x=d1.total_bill,y=d1.tip)


# In[20]:


d1.smoker.value_counts()


# In[22]:


sns.relplot(x=d1.total_bill,y=d1.tip,data=d1,hue='smoker')


# In[44]:


d1[d1.total_bill==d1.total_bill.max()]['smoker']


# In[45]:


sns.relplot(x=d1.total_bill,y=d1.tip,data=d1,style='smoker')


# In[46]:


sns.relplot(x=d1.total_bill,y=d1.tip,data=d1,style='size')


# In[49]:


sns.relplot(x=d1.total_bill,y=d1.tip,data=d1,size='size')


# In[50]:


sns.relplot(x=d1.total_bill,y=d1.tip,data=d1,kind='line')


# In[51]:


sns.relplot(x=d1.total_bill,y=d1.tip,data=d1,col='time')


# In[52]:


sns.relplot(x=d1.total_bill,y=d1.tip,data=d1,col='size')


# In[54]:


sns.catplot(x=d1.day,y=d1.tip,data=d1)


# In[56]:


sns.catplot(x=d1.day,y=d1.tip,data=d1,kind='swarm')


# In[57]:


sns.catplot(x=d1.day,y=d1.tip,data=d1,kind='box')


# In[60]:


sns.pairplot(d1)


# In[61]:


t=sns.load_dataset('titanic')


# In[62]:


t


# In[63]:


t.iplot(x='sex',y='survived',kind='bar')


# In[64]:


t.head()


# In[67]:


t.plot(x='sex',y='survived',kind="bar")


# In[68]:


import cufflinks as cf
cf.go_offline()


# In[70]:


t.iplot(x='sex',y='survived',kind="bar")


# In[ ]:




