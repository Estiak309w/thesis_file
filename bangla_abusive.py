
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# # 1:  READ DATA FILE & MAKE LIST OF EACH TYPE

# In[2]:


path_slang = "thesis_code/abusive_slang.txt"
path_religious = "thesis_code/abusive_religious.txt"
path_attack = "thesis_code/abusive_attack.txt"
path_celebrity = "thesis_code/abusive_celebrity.txt"

def read_file(path):
    sent =[]
    sent.clear()
    with open(path, "r",encoding="utf-8") as f:
        for line in f:
            sent.append(line)
    return sent
slang_sent = read_file(path_slang)
religious_sent = read_file(path_religious)
attack_sent = read_file(path_slang)
celebrity_sent = read_file(path_celebrity)


# In[3]:


for i in range(3):
    print(slang_sent[i])
for i in range(3):
    print(religious_sent[i])


# # 2. REMOVE ALL BAD CHARECTER

# In[4]:


import re
def digit_remover(text):
    text = re.sub(r'[\d]','',text)
    text = re.sub(r'[?\!\‛\’\(\)\.\।]+','',text)
    text = re.sub(r'[/\-\,]',' ',text)
    text = text.rstrip("\n\r")
    return text


# In[5]:


print(digit_remover("হত্যাকাণ্ড/খারাপ,অদৃশ্য-কাল্পনিক,ধর্মের/ধার্মিকদের,0"))


# In[6]:


def remover(sent):
    for i in range(len(sent)):
        sent[i] = digit_remover(sent[i])
    return sent
slang_sent = remover(slang_sent)
religious_sent = remover(religious_sent)
attack_sent = remover(attack_sent)
celebrity_sent = remover(celebrity_sent)


# In[7]:


for i in range(7):
    print(celebrity_sent[i])


# # ADD COLUMN AND LABEL EACH TYPE OF DATA

# In[8]:


slang_df = pd.DataFrame({'col':slang_sent})
slang_df['label'] = 2%2
religious_df = pd.DataFrame({'col':religious_sent})
religious_df['label'] = 1
attack_df = pd.DataFrame({'col':attack_sent})
attack_df['label'] = 2
celebrity_df = pd.DataFrame({'col':celebrity_sent})
celebrity_df['label'] = 3


# In[9]:


attack_df.head()


# # CONCATENATE EACH TYPE OF DATA AND SUFFLE THEM

# In[10]:


frames = [slang_df, religious_df,attack_df,celebrity_df]
result = pd.concat(frames,ignore_index=True)
#suffle the data frame
result = result.sample(frac=1)


# In[11]:


result.head(5)


# # SPLIT DATA INTO TRAIN AND TEST SET

# In[12]:


from sklearn.model_selection import train_test_split
X = result['col']
y = result['label']
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state = 1,test_size=.2)


# In[13]:


print(X_train[5])


# In[14]:


result.shape


# #  REPRESENTING TEXT AS NUMERICAL DATA

# In[15]:


# import and instantiate CountVectorizer (with the default parameters)
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(tokenizer=lambda a: a.split())


# In[16]:


# learn the 'vocabulary' of the training data (occurs in-place)
X_train_dtm = vect.fit_transform(X_train)
X_test_dtm = vect.transform(X_test)


# # APPLY MULTINOMIAL NAIVE BAYES ALGORITHM

# In[31]:


# import and instantiate a Multinomial Naive Bayes model
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB(alpha=0.1)


# In[32]:


# train the model using X_train_dtm (timing it with an IPython "magic command")
get_ipython().run_line_magic('time', 'nb.fit(X_train_dtm, y_train)')


# In[33]:


# make class predictions for X_test_dtm
y_pred_class = nb.predict(X_test_dtm)


# In[34]:


# calculate accuracy of class predictions
from sklearn import metrics
metrics.accuracy_score(y_test, y_pred_class)


# # APPLY LINEAR SVC CLASSIFIER

# In[21]:


from sklearn.svm import LinearSVC
svc = LinearSVC()
svc.fit(X_train_dtm, y_train)
y_pred_class_svc = svc.predict(X_test_dtm)


# In[22]:


metrics.accuracy_score(y_test, y_pred_class_svc)


# # APPLY LOGISTIC REGRESSION

# In[23]:


from sklearn.linear_model import LogisticRegression
logit = LogisticRegression()
logit.fit(X_train_dtm, y_train)
y_pred_class_logit = logit.predict(X_test_dtm)


# In[24]:


metrics.accuracy_score(y_test, y_pred_class_logit)


# # APPLY RANDOM FOREST CLASSIFIER

# In[25]:


from sklearn.ensemble import RandomForestClassifier
randomf = RandomForestClassifier(n_estimators=1000,max_depth=50)
randomf.fit(X_train_dtm, y_train)
y_pred_class_randomf = randomf.predict(X_test_dtm)


# In[26]:


metrics.accuracy_score(y_test, y_pred_class_logit)

