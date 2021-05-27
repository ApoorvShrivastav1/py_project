#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


Maths = pd.read_excel('Python_Assignment.xlsx',sheet_name='Maths')


# In[3]:


Maths.head()


# In[4]:


Physics= pd.read_excel('Python_Assignment.xlsx',sheet_name='Physics')


# In[5]:


Physics.head()


# In[6]:


Physics['Physics%']=(((Physics['Theory Marks']+Physics['Numerical Marks']+Physics['Practical Marks'])/300)*100)


# In[7]:


Physics.head()


# In[8]:


Maths['Maths%']=(((Maths['Theory Marks']+Maths['Numerical Marks']+Maths['Practical Marks'])/300)*100)


# In[9]:


Maths.head()


# In[10]:


Maths.drop(['Theory Marks','Numerical Marks','Practical Marks'], axis=1)


# In[11]:


Physics.drop(['Theory Marks','Numerical Marks','Practical Marks'], axis=1)


# In[12]:


Hindi = pd.read_excel('Python_Assignment.xlsx',sheet_name='Hindi')


# In[13]:


Economics = pd.read_excel('Python_Assignment.xlsx',sheet_name='Economics')


# In[14]:


Music = pd.read_excel('Python_Assignment.xlsx',sheet_name='Music')


# In[15]:


Hindi['Hindi%']=(Hindi['Marks'])


# In[16]:


Hindi.head()


# In[17]:


Hindi.drop('Marks',axis=1)


# In[18]:


Economics.head()


# In[19]:


Economics['Economics%'] = (((Economics['Theory Marks']+Economics['Numerical Marks'])/200)*100)


# In[20]:


Economics.drop(['Theory Marks','Numerical Marks'],axis=1)


# In[21]:


Music.head()


# In[22]:


Music['Music%']=(((Music['Theory Marks']+Music['Practical Marks'])/200)*100)


# In[23]:


Music.drop(['Theory Marks','Practical Marks'],axis=1)


# In[24]:


all_subjects=pd.concat([Maths,Physics,Hindi,Economics,Music],axis=0,ignore_index=True)


# In[25]:


all_subjects


# In[26]:


all_subjects.shape


# In[27]:


Maths.drop(['Theory Marks','Numerical Marks','Practical Marks'], axis=1, inplace=True)
Maths.head()


# In[28]:


Physics.head()


# In[29]:


#Physics.drop(['Theory Marks','Numerical Marks','Practical Marks'], axis = 1, inplace=True)
Physics.head()


# In[30]:


Hindi.head()


# In[31]:


#Hindi.drop(['Marks'], axis=1, inplace= True)
Hindi.head()


# In[32]:


Economics.head()


# In[33]:


#Economics.drop(['Theory Marks','Numerical Marks'], axis=1, inplace=True)
Economics.head()


# In[34]:


Music.head()


# In[35]:


#Music.drop(['Theory Marks','Practical Marks'], axis= 1, inplace =True)
Music.head()


# In[36]:


df1= pd.merge(Maths,Physics, how='outer', on=['Roll No','Class'] )


# In[37]:


df1.head()


# In[38]:


df2= pd.merge(df1,Hindi, how='outer', on = ['Roll No','Class'])


# In[39]:


df3= pd.merge(df2,Economics, how='outer', on = ['Roll No','Class'])


# In[40]:


df=pd.merge(df3,Music, how='outer', on =['Roll No','Class'])


# In[41]:


df.head()


# In[42]:


df.shape


# In[43]:


df['Roll No'].count()


# In[44]:


df.dropna()['Roll No'].count()


# In[45]:


df['Class'].value_counts()


# In[ ]:




