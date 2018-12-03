#!/usr/bin/env python
# coding: utf-8

# In[7]:


from gensim.models import Word2Vec
import csv
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn import metrics
from itertools import chain
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
#from keras.utils import np_utils
from scipy import spatial
from sklearn.feature_extraction.text import CountVectorizer


# In[8]:


df=pd.read_csv('train3.tsv',delimiter='\t')
s3=df.iloc[:,2]
Tar=s3.values.tolist()
for i in range(len(Tar)):
    Tar[i]=int(Tar[i])
print(len(Tar))


# In[9]:


df = pd.read_csv('drugLabels.csv')
dfList = df.values.tolist()
#print(dfList)
vectorizer = CountVectorizer(tokenizer=lambda doc: doc, lowercase=False)

X = vectorizer.fit_transform(dfList)
#print(vectorizer.get_feature_names())
#print(X)

Xp=X.toarray()


# In[11]:


clf=SVC(kernel='rbf',C=0.5,gamma=2.0)
clf.fit(Xp,Tar)


# In[12]:


y_pred=clf.predict(Xp)
print('accuracy',metrics.accuracy_score(Tar,y_pred))


# # Preparing Test Data

# In[13]:


ddf=pd.read_csv('test.tsv',delimiter='\t',header=None,names=['drugA','drugB','labels'])
ss1=ddf.iloc[:,0].apply(lambda x : str(x).split(':')[1].lower())
ss2=ddf.iloc[:,1].apply(lambda x : str(x).split(':')[1].lower())
ttr_data=pd.concat([ss1,ss2],axis=1)


# In[14]:


tstList = ttr_data.values.tolist()
vectorizer1 = CountVectorizer(tokenizer=lambda doc: doc, lowercase=False)
Xt = vectorizer.fit_transform(tstList)


# In[21]:


# Since length of extracted features from count vectorizer for test $ Train is different i.e 2718!=5767
#Increasing the dimensions of sparse matrix by appending zero columns to make the dimensions of test data equal to train data on which model is trained
#If not done it will throw dimensionality error

import scipy.sparse as sps
Test_Xt_redef = sps.csr_matrix((Xt.data, Xt.indices, Xt.indptr), shape=(7026, 2225))

print('length of extracted features from count vectorizer for test data after redefining')
print(Test_Xt_redef.shape[1])


# In[23]:


Xtst=Test_Xt_redef.toarray()
Xtst.shape


# In[24]:


tst_pred=clf.predict(Xtst)


# In[28]:


ddf['Pred_Labels1']=tst_pred
ddf['Pred_Labels'] = np.where(ddf['Pred_Labels1']==0, 'False', 'True')
pred_df=ddf.drop(['Pred_Labels1','labels'],axis=1)


# In[30]:


pred_df.to_csv('Test_Pred1.tsv',header=None)

