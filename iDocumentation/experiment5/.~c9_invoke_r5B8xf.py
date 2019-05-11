# https://github.com/shreyans29/thesemicolon/blob/master/Text%20Analytics%20CV.ipynb
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection  import train_test_split
from sklearn.naive_bayes import MultinomialNB

df=pd.read_csv('smsspam.csv',sep='\t',names=['Status','Message'])

# print(df.head())
# print(len(df))
# print(len(df[df.Status=='spam']))
# print(len(df[df.Status=='ham']))
df.loc[df["Status"]=='ham',"Status",]=1
df.loc[df["Status"]=='spam',"Status",]=0
# print(df.head())

df_x=df["Message"]
df_y=df["Status"]
# print(df_x)
# print(df_y)
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)
print(x_train.head())

cv = CountVectorizer()
x_traincv = cv.fit_transform(["Hi How are you How are you doing","Hi what's up","Wow that's awesome"])
# print(x_traincv.toarray())
# print(cv.get_feature_names())

cv1 = CountVectorizer()
x_traincv=cv1.fit_transform(x_train)
a=x_traincv.toarray()
# print(a[0])
# print(cv1.inverse_transform(a[0]))
print(x_train.iloc[0])
x_testcv=cv1.transform(x_test)
# print(x_testcv.toarray())


mnb = MultinomialNB()
y_train=y_train.astype('int')
