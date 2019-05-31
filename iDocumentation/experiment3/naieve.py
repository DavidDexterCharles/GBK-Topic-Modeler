# https://github.com/shreyans29/thesemicolon/blob/master/Text%20Analytics%20CV.ipynb
# https://www.reddit.com/r/MachineLearning/comments/1inxnq/how_to_factor_in_tfidf_with_naive_bayes/
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection  import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix , classification_report


df=pd.read_csv('smsspam.csv',sep='\t',names=['Status','Message'])

# print(df.head())
# print(len(df))
# print(len(df[df.Status=='spam']))
# print(len(df[df.Status=='ham']))

df_x=df["Message"]
df_y=df["Status"]
# print(df_x)
# print(df_y)
# https://medium.com/@contactsunny/how-to-split-your-dataset-to-train-and-test-datasets-using-scikit-learn-e7cf6eb5e0d
xx_train, xx_test, yy_train, yy_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)

df.loc[df["Status"]=='ham',"Status",]=1
df.loc[df["Status"]=='spam',"Status",]=0
# print(df.head())



x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)
# print(x_train.head())

# cv = CountVectorizer()
# x_traincv = cv.fit_transform(["Hi How are you How are you doing","Hi what's up","Wow that's awesome"])
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


mnb = MultinomialNB()#alpha=.01
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


# Explains the target Attribute: https://scikit-learn.org/stable/datasets/index.html

count = 0
y_true = []
y_pred = []
for i in range (len(predictions)):
    y_true.append(a[i])
    y_pred.append(predictions[i])
    if predictions[i]==a[i]:
        count=count+1
    
    # else:
    #     print("\n")
    #     print(xx_test.iloc[i])
print(classification_report(y_true, y_pred,labels=[1,0]))
print(count)
print(len(predictions))
print(count/len(predictions))

# ==========================================================================================================================

# =================================================================================================================================
print("==========Group BY Key================================================================================================================")
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
from gbk.gbk import GBK as Model

 
topics = {}
keys = {}
topics['model'] =['spam','ham']
topics['model2'] =['spam']
topics['model3'] =['ham']
keys['spam']=['spam']
keys['ham']=['ham']
model = Model()
model.init(topics)

# print(len(x_test))
# print(len(y_test))

for i in range(0,len(xx_train)):
    model.build(topics,keys,(xx_train.iloc[i])+" "+yy_train.iloc[i]+" ")
    
def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict

def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    
    # idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            # print(word,val)
            if val > 0:
                if word in idfDict:
                    idfDict[word] += 1
                else:
                    idfDict[word] = 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))
        
    return idfDict

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf    
    

bow = {}
classvectors =[]
for key, val in model.model["model"].items():
    classvectors.append(model.model["model"][key]["features"])
    bow[key] = list(model.model["model"][key]["features"].keys())
tfbow = {}
for key, val in model.model["model"].items():
    tfbow[key] = computeTF(model.model["model"][key]["features"], bow[key])
    
idfs = computeIDF(classvectors)

# for key, val in model.model["model"].items():
#     model.model["model"][key]["features"] = computeTFIDF(tfbow[key],idfs)

    

model.setweights(topics)# https://hal.archives-ouvertes.fr/hal-01418129/document
model.tojson("test")
gbkcount =0
y_true =[]
y_pred = []
for i in range (0,len(xx_test)):
    predictedtag,weight = model.predict('model',(xx_test.iloc[i])).getTopic()
    y_true.append(yy_test.iloc[i])
    y_pred.append(predictedtag)
    if predictedtag == yy_test.iloc[i]:
        gbkcount+=1
    # else:
    #     print(predictedtag)
    #     print("\n")
    #     print(xx_test.iloc[i])
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
# print(confusion_matrix(y_true, y_pred, labels=["ham","spam"]))#https://hackernoon.com/idiots-guide-to-precision-recall-and-confusion-matrix-b32d36463556
# print(yy_test)
# https://www.youtube.com/watch?v=8Oog7TXHvFY
print(classification_report(y_true, y_pred, labels=["ham","spam"]))
print(gbkcount)
print(len(xx_test))
print(gbkcount/len(xx_test))