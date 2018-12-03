#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


l=[]
with open('train.txt') as f: 
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


# In[3]:


#Removes empty strings and '\n' strings from the lists
l1=[list(filter(str.strip, lists)) for lists in l]


# In[4]:


#Cleaning false and true column values
l2=[]
for i in l1:
    k=['false' if i1.find('false')!=-1 else i1 for i1 in i]
    l2.append(k)
    
l3=[]
for i in l2:
    k=['true' if i1.find('true')!=-1 else i1 for i1 in i]
    l3.append(k)


# In[5]:


Final_list=l3


# In[6]:


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


# In[7]:


label=[]
WordList=[]
for T in wordLs:
    label.append(T[-1])
    WordList.append(T[:-1])


# In[8]:


#Creating Sentence by joining each word in the list for each row i.e list
Sentence_lst=[' '.join([str(v) for v in ls]) for ls in WordList]


# # Model Training

# In[9]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import scipy.sparse as sps


# In[10]:


# Splitting data into train and test sets
label_train=label[:25000]
label_test=label[25000:]
Sentence_lst_train=Sentence_lst[:25000]
Sentence_lst_test=Sentence_lst[25000:]


# In[11]:


vectorizer = CountVectorizer(lowercase=False)
Xp_train = vectorizer.fit_transform(Sentence_lst_train)

#print(vectorizer.get_feature_names())
li=vectorizer.get_feature_names()
print('length of extracted features from count vectorizer')
print(len(li))


# In[12]:


print('SVM Training started.....')
clf=SVC(kernel='linear',C=0.5,gamma=1)
clf.fit(Xp_train,label_train)
print('SVM Training ended')


# In[13]:


trainSample_pred=clf.predict(Xp_train)
print ("Train Accuracy :: ", accuracy_score(label_train, trainSample_pred))


# In[14]:


#Predicting and evaluating accuracy on test sample

Xp_test_sample = vectorizer.fit_transform(Sentence_lst_test)
li=vectorizer.get_feature_names()
print('length of extracted features from count vectorizer')
print(len(li))


# In[15]:


Xp_test_sample.shape


# In[16]:


# Since length of extracted features from count vectorizer for test $ Train sets are different
#Increasing the dimensions of sparse matrix by appending zero columns to make the dimensions of test data equal to train data on which model is trained
#If not done it will throw dimensionality error

import scipy.sparse as sps
Xp_test_sample_red = sps.csr_matrix((Xp_test_sample.data, Xp_test_sample.indices, Xp_test_sample.indptr), shape=(5853, 5083))

print('length of extracted features from count vectorizer for test data after redefining')
print(Xp_test_sample_red.shape[1])


# In[17]:


test_pred=clf.predict(Xp_test_sample_red)
print ("Test Accuracy :: ", accuracy_score(label_test, test_pred))


# # Model Training on whole Dataset

# In[18]:


vectorizer = CountVectorizer(lowercase=False)
Xp = vectorizer.fit_transform(Sentence_lst)
li=vectorizer.get_feature_names()
print('length of extracted features from count vectorizer')
print(len(li))


# In[19]:


print('SVM Training started.....')
clf=SVC(kernel='linear',C=0.5,gamma=1)
clf.fit(Xp,label)
print('SVM Training ended')


# In[20]:


train_pred=clf.predict(Xp)
print ("Train Accuracy on whole data:: ", accuracy_score(label, train_pred))


# # Preparing test Data

# In[21]:


t=[]
with open('test.txt') as f: 
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
            
        t.append(m)


# In[22]:


t1=[list(filter(str.strip, lists)) for lists in t]


# In[23]:


testWords=[]
for i in t1:
    m=[]
    for word in i:
        if word.find(':')!=-1:
            pass
        elif word.find('"')!=-1:
            m.append(word[:-1])
            
        else:
            m.append(word)
    testWords.append(m)


# In[24]:


#Removing ? present at the end of each line
# ? will be replaced with predicted variable 
TestWord=[T[:-1] for T in testWords]

#Joining lists to form sentences list
Tst_Sentence_lst=[' '.join([str(v) for v in ls]) for ls in TestWord]


# # Predicting Labels for test data 

# In[25]:


Test_Xp = vectorizer.fit_transform(Tst_Sentence_lst)


# In[26]:


#print(vectorizer.get_feature_names())

ti=[]
ti=vectorizer.get_feature_names()
print('length of extracted features from count vectorizer for test data')
print(len(li))


# In[27]:


# Since length of extracted features from count vectorizer for test $ Train is different i.e 2718!=5767
#Increasing the dimensions of sparse matrix by appending zero columns to make the dimensions of test data equal to train data on which model is trained
#If not done it will throw dimensionality error

import scipy.sparse as sps
Test_Xp_redefined = sps.csr_matrix((Test_Xp.data, Test_Xp.indices, Test_Xp.indptr), shape=(7026, 5767))

print('length of extracted features from count vectorizer for test data after redefining')
print(Test_Xp_redefined.shape[1])


# In[29]:


pred_labels=clf.predict(Test_Xp_redefined)


# In[30]:


pred_labels[100]


# In[31]:


file_name = 'optest.txt' #output test file with predicted labels

with open('test.txt','r') as fnr:
    text = fnr.readlines()

#Creating a list by concatenating each line from original file with predicted labels list
text1=list(zip(text,pred_labels))
#Removing ? from lines in Original file 
line1=[i[0][:-3]+'\t'+i[1] for i in text1]

#writing each line to a new file
with open(file_name, 'w') as filehandle:  
    filehandle.writelines("%s\n" % lines for lines in line1)

