#!/usr/bin/python3

#import packages
import pandas as pd
import re
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import tweepy

def preprocess_text(raw):
    #lower case
    tmp=raw.lower()

    #remove unwanted text...@, #, http/s etc
    tmp=re.sub('http/S+|https/S+|www/S+',' ',tmp)
    tmp=re.sub('@[a-zA-Z0-9]',' ',tmp)
    tmp=re.sub('#[a-zA-Z0-9]',' ',tmp)
    tmp=re.sub('^a-zA-Z0-9',' ',tmp)

    #remove english stop words...download english stopwords first
    tmp=tmp.split()
    words = [w for w in tmp if not w in set(stopwords.words("english"))]

    #lemmatize...download WordNet first
    lmtzr=WordNetLemmatizer()
    #words_final=[lmtzr.lemmatize(w,pos="a") for w in words]
    words_final=[lmtzr.lemmatize(w) for w in words]
    
    words_final=' '.join(words_final)

    return words_final

def sentiment(proc):
    proc_blb=TextBlob(proc)
    senti=proc_blb.sentiment.polarity
    if senti>0:
        senti_text="Positive"
    elif senti<0:
        senti_text="Negative"
    else:
        senti_text="Neutral"

    return senti_text


#read csv file
data=pd.read_csv("training.1600000.processed.noemoticon.csv",encoding="latin-1")
#print(data.head(50))

# ONLY first 10 rows
data_10rows=data.iloc[:10,5]
print(type(data_10rows))
#print(data_10rows)

# ++++++++++++++++++
# @@@@@@@@@   BE SURE TO REMOVE THE CREDENTIALS  @@@@@@@@@
# ++++++++++++++++++

'''
#authenticate and get twitter api
cons_key="6IOeMSM5ZGJb1iYFjQKFasI7g"
cons_key_secret="Gw2l0gZqXGB0Sj7XGf1Il20L0sFMQibFkUookY4vNGdLlG5w3n"
acctoken_key="813327462696263680-Hb7gBfxwSaviKymb0AMoGk41qbzB1Iq"
acctoken_key_secret="qdaBHBfOerWHZP3iGFQp7p4Odhp7XJJnPwAkkdmUPPEWf"

auth=tweepy.OAuthHandler(cons_key,cons_key_secret)
auth.set_access_token(acctoken_key,acctoken_key_secret)
api=tweepy.API(auth)
print(api)

#get tweets
#tweets=api.user_timeline(screen_name="@BBCWorld",count=20)
#print(tweets)
'''



#pre-process each text
final_list=[]
tmp=dict()
print("===============")
for row in data_10rows:
    print("======RAW=========")
    print(row)
    tmp["raw_text"]=row
    proc=preprocess_text(row)
    print("=====PROCESSED==========")
    print(proc)
    tmp["processed_text"]=proc
    print("=====SENTIMET==========")
    tmp["sentiment"]=sentiment(proc)
    print(tmp["sentiment"])
    print("\n")

    final_list.append(tmp)

    #write to file
    #file.write()

#print(final_list)


#close file






