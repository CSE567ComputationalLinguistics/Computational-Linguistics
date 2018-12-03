#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


l=[]
with open('kumkum.txt') as f: 
    for line in f: 
        words=line.split(",")
        a=[word.split(':')[1:] if word.find('DrugDDI')!=-1 else word for word in words]
        m=[]
        for i in a:
            if isinstance(i, list):
                m.append(i[0])
                m.append(i[-1])
            else:
                m.append(i)
            
        l.append(m)


# In[5]:


l


# In[6]:


#Removes empty strings and '\n' strings from the lists
l1=[list(filter(str.strip, lists)) for lists in l]


# In[7]:


l1


# In[8]:


#Cleaning false and true column values
l2=[]
for i in l1:
    k=['false' if i1.find('false')!=-1 else i1 for i1 in i]
    l2.append(k)
    
l3=[]
for i in l2:
    k=['true' if i1.find('true')!=-1 else i1 for i1 in i]
    l3.append(k)


# In[9]:


Final_list=l3


# In[10]:


Final_list


# In[12]:


#Removing Drug Id pair having :: and Final Word list is created
wordLs=[]
for i in Final_list:
    m=[]
    for word in i:
        if word.find(':')!=-1:
            pass
        elif word.find('"')!=-1:
            m.append(word[:-1])
            
        else:
            m.append(word)
        wordLs.append(m)


# In[13]:


wordLs


# In[14]:


label=[]
WordList=[]
for T in wordLs:
    label.append(T[-1])
    WordList.append(T[:-1])


# In[15]:


WordList


# In[16]:


#Creating Sentence by joining each word in the list for each row i.e list
Sentence_lst=[' '.join([str(v) for v in ls]) for ls in WordList]


# In[17]:


Sentence_lst


# In[18]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn import metrics


# In[19]:


vectorizer = CountVectorizer(lowercase=False)


# In[20]:


Xp = vectorizer.fit_transform(Sentence_lst)


# In[25]:


#print(vectorizer.get_feature_names())

li=[]
li=vectorizer.get_feature_names()
print(len(li))


# In[ ]:


clf=SVC(kernel='linear',C=0.5,gamma=1)
clf.fit(Xp,label)


# In[36]:





# In[ ]:




