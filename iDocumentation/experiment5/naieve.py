# https://github.com/shreyans29/thesemicolon/blob/master/Text%20Analytics%20CV.ipynb
# https://www.reddit.com/r/MachineLearning/comments/1inxnq/how_to_factor_in_tfidf_with_naive_bayes/
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

df_x=df["Message"]
df_y=df["Status"]
# print(df_x)
# print(df_y)

xx_train, xx_test, yy_train, yy_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)

df.loc[df["Status"]=='ham',"Status",]=1
df.loc[df["Status"]=='spam',"Status",]=0
# print(df.head())



x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)
# print(x_train.head())

cv = CountVectorizer()
x_traincv = cv.fit_transform(["Hi How are you How are you doing","Hi what's up","Wow that's awesome"])
# print(x_traincv.toarray())
# print(cv.get_feature_names())

cv1 = CountVectorizer()
x_traincv=cv1.fit_transform(x_train)
a=x_traincv.toarray()
# print(a[0])
# print(cv1.inverse_transform(a[0]))
# print(x_train.iloc[0])
x_testcv=cv1.transform(x_test)
# print(x_testcv.toarray())


mnb = MultinomialNB()
y_train=y_train.astype('int')
# print(y_train)
res = mnb.fit(x_traincv,y_train)
# print(res)
testmessage=x_test.iloc[0]
print(testmessage)
predictions=mnb.predict(x_testcv)
print(predictions)
a=np.array(y_test)
print(a)

count = 0
for i in range (len(predictions)):
    if predictions[i]==a[i]:
        count=count+1
    # else:
    #     print("\n")
    #     print(xx_test.iloc[i])
print(count)
print(len(predictions))
print(count/len(predictions))

# ==========================================================================================================================

# =================================================================================================================================

# https://github.com/DavidDexterCharles/bit-of-data-science-and-scikit-learn/blob/master/notebooks/FeatureExtraction.ipynb
print("==========Group BY Key================================================================================================================")
from gbk.gbk import GBK as Model
topics = {}
keys = {}
topics['model'] =['spam','ham']
keys['spam']=['spam']
keys['ham']=['ham']
model = Model()
model.init(topics)

# print(len(x_test))
# print(len(y_test))

for i in range(0,len(xx_train)):
    model.build(topics,keys,(xx_train.iloc[i])+" "+yy_train.iloc[i]+" ")
model.setweights(topics)
gbkcount =0
for i in range (0,len(xx_test)):
    predictedtag,weight = model.predict('model',(xx_test.iloc[i])).getTopic()
    if predictedtag == yy_test.iloc[i]:
        gbkcount+=1
    # else:
    #     print("\n")
    #     print(xx_test.iloc[i])
print(gbkcount)

# https://github.com/bapspatil/ML-Lab/blob/master/6-MNB.py