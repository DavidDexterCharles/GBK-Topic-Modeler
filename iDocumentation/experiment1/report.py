import numpy as np
import pandas as pd
from gbk.gbk import GBK as Model
from sklearn.model_selection import train_test_split

df=pd.read_csv('smsspam.csv',sep='\t',names=['Status','Message'])
# print(len(df["Message"]))
# print(len(df["Status"]))
df_x=df["Message"]
df_y=df["Status"]
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)


# print(len(x_train))
# print(len(y_train))
# print(x_train)
# for row in x_train:
#     print(row[0])
# https://github.com/shreyans29/thesemicolon/blob/master/Text%20Analytics%20tfidf.ipynb
topics = {}
keys = {}
topics['model'] =['spam','ham']
keys['spam']=['spam']
keys['ham']=['ham']
model = Model()
model.init(topics)

for i in range(0,len(x_train)):#applynounfilter
    # print(y_train.iloc[i])
    model.build(topics,keys,(x_train.iloc[i])+" "+y_train.iloc[i]+" ")
    # print(df["Status"][i])
model.setweights(topics)
model.tojson("spammodel")
test = "CLAIRE   havin borin time  now alone  wanna cum over 2nite? Chat now 09099725823 hope    Luv CLAIRE  Calls£1/minmoremobsEMSPOBox45PO139WA"

numFalse = numTrue = 0
for i in range (0,len(x_test)):
    result = model.predict('model',(x_test.iloc[i])).getTopic()
    predictedtag,weight = result
    if predictedtag == y_test.iloc[i]:
        numTrue += 1
    else:
        print("\nresult:{} \n{}".format(result,x_test.iloc[i]))
        numFalse += 1
        
print("\n")
print("Total: {} \n True: {} \n False: {}".format(len(x_test),numTrue,numFalse))

# https://github.com/shreyans29/thesemicolon/blob/master/Text%20Analytics%20tfidf.ipynb