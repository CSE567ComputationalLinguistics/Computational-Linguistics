#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gensim.models import Word2Vec
import csv
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn import metrics
from itertools import chain
from sklearn.model_selection import train_test_split


# In[2]:


df=pd.read_csv('train.tsv',delimiter='\t')
s1=df.iloc[:,0].apply(lambda x : str(x).split(':')[1].lower())
s2=df.iloc[:,1].apply(lambda x : str(x).split(':')[1].lower())
s3=df.iloc[:,2]
tr_data=pd.concat([s1,s2,s3],axis=1)
tr_data.columns=['drugA','drugB','label']


# In[3]:


tr_pos=tr_data.loc[tr_data['label']==True]
tr_only_2cols_pos=tr_pos.drop('label',1)

tr_neg=tr_data.loc[tr_data['label']==False]
tr_only_2cols_neg=tr_neg.drop('label',1)


# In[4]:


l_pos=[]
l_neg=[]
l_pos=tr_only_2cols_pos.values.tolist()
l_neg=tr_only_2cols_neg.values.tolist()


# In[5]:


lfinal=[]
model_pos=Word2Vec(l_pos,min_count=1)
model_neg=Word2Vec(l_neg,min_count=1)
drugs=list(model_pos.wv.vocab)
for pair in l_pos:
    l1=[]
    l2=[]
    ld=[]
    l=[]
    l1=model_pos[pair[0]]
    l2=model_pos[pair[1]]
    l.append(l1)
    l.append(l2)
    ld=list(chain.from_iterable(l))
    lfinal.append(ld)


ht=len(l_pos)
target_pos=np.ones((ht,))
target_pos=target_pos.tolist()


# In[6]:


lfinall=[]
for pair in l_neg:
    l1=[]
    l2=[]
    l=[]
    l1=model_neg[pair[0]]
    l2=model_neg[pair[1]]
    l.append(l1)
    l.append(l2)
    ld=list(chain.from_iterable(l))
    lfinall.append(ld)


htt=len(l_neg)
target_neg=np.zeros((htt,))
target_neg=target_neg.tolist()


# In[7]:


temp=np.array(lfinal)
temp1=np.array(lfinall)
tp=np.array(target_pos)
tq=np.array(target_neg)


# In[8]:


temp3=np.concatenate((temp,temp1),axis=0)
tr=np.concatenate((tp,tq),axis=0)
print(temp3.shape)
print(tr.shape)


# In[11]:


X_train=temp3
Y_train=tr


# In[27]:


Y_train


# In[14]:


clf=SVC(kernel='rbf',C=0.5,gamma=2.0)
clf.fit(X_train,Y_train)


# In[15]:


y_pred=clf.predict(X_train)


# In[16]:


print('accuracy',metrics.accuracy_score(Y_train,y_pred))


# # Preparing Test Data

# In[54]:


ddf=pd.read_csv('test.tsv',delimiter='\t',header=None,names=['drugA','drugB','labels'])
ss1=ddf.iloc[:,0].apply(lambda x : str(x).split(':')[1].lower())
ss2=ddf.iloc[:,1].apply(lambda x : str(x).split(':')[1].lower())
#ss3=ddf.iloc[:,2]
ttr_data=pd.concat([ss1,ss2],axis=1)


# In[55]:


l_tst=[]
l_tst=ttr_data.values.tolist()


# In[56]:


tstfinal=[]
model_tst=Word2Vec(l_tst,min_count=1)
drugs=list(model_tst.wv.vocab)
for pair in l_tst:
    l1=[]
    l2=[]
    ld=[]
    l=[]
    l1=model_tst[pair[0]]
    l2=model_tst[pair[1]]
    l.append(l1)
    l.append(l2)
    ld=list(chain.from_iterable(l))
    tstfinal.append(ld)


ht=len(l_tst)
target_tst=np.ones((ht,))
target_tst=target_tst.tolist()


# In[57]:


temp=np.array(tstfinal)
X_tst=temp


# In[58]:


tst_pred=clf.predict(X_tst)


# In[60]:


#Test data with prediction label
ddf['Pred_Labels1']=tst_pred
ddf['Pred_Labels'] = np.where(ddf['Pred_Labels1']==1.0, 'False', 'True')
pred_df=ddf.drop(['Pred_Labels1','labels'],axis=1)


# In[63]:


pred_df.to_csv('Test_Pred2.tsv',header=None)

