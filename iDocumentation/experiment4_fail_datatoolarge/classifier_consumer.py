from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

from gbc_code.gbc import Gbc as Model
from  gbc_code.helper import *
def getTopic(topic):
    largest = 0
    key = ""
    for k,v in topic.items():
        if v > largest:
            largest = v
            key = k
    return key, largest
    
model = Model()
model.load("exp22.json")

df = pd.read_csv('Consumer_Complaints.csv')
df = df[pd.notnull(df['Consumer complaint narrative'])]
col = ['Product', 'Consumer complaint narrative']
df = df[col]
df.columns = ['Product', 'Consumer_complaint_narrative']

x_train, x_test, y_train, y_test = train_test_split(df['Consumer_complaint_narrative'], df['Product'], random_state = 0)

document = "I am disputing the inaccurate information the Chex-Systems has on my credit report. I initially submitted a police report on XXXX/XXXX/16 and Chex Systems only deleted the items that I mentioned in the letter and not all the items that were actually listed on the police report. In other words they wanted me to say word for word to them what items were fraudulent. The total disregard of the police report and what accounts that it states that are fraudulent. If they just had paid a little closer attention to the police report I would not been in this position now and they would n't have to research once again. I would like the reported information to be removed : XXXX XXXX XXXX"

# Expected:Student loan
document = '''National Collegiate Trust is a trust only but American Education
Services claims they are my lender which is an untrue statement.
It is illegal for any company to knowlingly misled a customer,
I spoke with XXXX a supervisor at XXXX XXXX XXXX and he advised me
that National Collegiate Trust does not make any decisions on the loan
plus since American Education is the one reporting to the credit bureau, 
they can remove any negative items because I was told by numerous reps that
is up to National Collegiate Trust to remove any negative items. XXXX advised
me which I did record that call in this entirety because an attorney advised 
me to record calls as proof of American Education Services being dishonest in their 
dealings and I have contacted the board members for XXXX to get this matter resolved once for all. 
American Education Services has over XXXX complaints due to them giving misinformation, all credit marks
will need to remove by law because National Collegiate Trust is not a lender and does not make any
decisions per XXXX. He states American Education Services is well aware of that so he is not sure
why they are telling me to fax a letter to them so they send it to NCT. Per the consumer attorneys 
I spoke with in XXXX and XXXX what AES is doing is unethical, you ca n't tell someone a person is
a lender on your account when they are not. They are not a lender, they hold of all of the loans in a trust.
This information was verified by XXXX and they kept repeating that NCT is only a trust, AES ca n't change 
the terms of the loans but they can remove negative reporting because they are the ones sending this information
to the credit bureaus not NCT ( NCT owns the debt but that 's it ). I also would like to see proof that
NCT still owns this debt as of today. If AES causes me to lost my job, then I will file bankruptcy because 
I wo n't have enough money to make any more payments. I have several recorded calls from AES, XXXX XXXX will 
claim otherwise but she will need to prove me wrong. She does not know anything because her answers to 
the complaints presented are generic at best, clearly not listening to any calls because all of the employees 
should be fired. I do not have any credit marks from any other companies because I can get accurate information 
from them. By the way, I also recorded the day I made a payment on XXXX/XXXX/15 and the automatic system is always 
wrong which I told a supervisor numerous times because it states my past due was {$500.00} which is incorrect my 
past due was {$390.00}, I also recorded that call and she acknowledged the automated system is wrong and
I have it recorded as proof therefore any and all credit reporting should be deleted to AES misinformation 
is illegal. I HAVE IT RECORDED ON MY CELL PHONE AS PROOF THEREFORE NCT/AES WILL HAVE TO REMOVE ALL OF THE NEGATIVE
CREDIT REPORTING BECAUSE ITS THE LAW UNDER THE FAIR CREDIT REPORTING ACT ( fcra ). I have complained to XXXX board
members of XXXX/AES who I have spoken with today because I refuse to play AES stupid games. AES should be shut down
and I will write a letter to every board member to make sure they upset this. I want my loans moved to another 
servicer because AES is a horrible servicer and I hope that the FTC and the CFPB step 
in because people should be able to get accurate answers from their servicer. 
AES and XXXX XXXX totally suck. AES 's automated system tries to make you pay more than you 
need to which is totally illegal. Because of AES 's credit reporting, I ca n't consolidate my private loans 
( private loan are credit based so you need a very good score to get a lower rate ) with XXXX company so
I can have a lower payment which will work better with my overall budget.

'''
# Expected:Payday loan Predicted:Mortgage
document ='''I borrowed {$480.00} and now I 'm expected to pay back quadruple that amount. 
i.e. : XXXX from XX/XX/2016 until XXXX 2016 I 'm XXXX, on a fixed income, this is PREDATORY LENDING at it 's finest. 

WHO IS MAKING ALL THAT INTEREST ON THIS MONEY! IT 'S REALLY A SHAME BEFORE GOD!!! 

Also while checking for the link to try and pay off early, it 's not there, but I did discover there was another loan pending online there, ONE ; I DID NOT APPLY FOR, but NOW, IT 'S GONE! I SCREENED SHOT A COPY TO ATTACH TO THIS COMPLAINT! 

I do believe someone is committing FRAUD!!!
'''

# test = ["apples","apple"]

# from sklearn.feature_extraction.text import CountVectorizer#http://blog.christianperone.com/2011/09/machine-learning-text-feature-extraction-tf-idf-part-i/
# from sklearn.feature_extraction.text import TfidfTransformer#http://www.minerazzi.com/tutorials/term-vector-3.pdf

# vectorizer = CountVectorizer()

# train_set = ["The sky is blue.", "The sun is bright."]
# test_set = ("The sun in the sky is bright.",
#     "We can see the shining sun, the bright sun.")
    
# thecounts = vectorizer.fit_transform(test)
# print(thecounts)

# result = model.predict('model1',(document))
# predictedtag,weight = getTopic(result)
# print(predictedtag)


numFalse = numTrue = 0
for i in range (0,30):#len(x_test)):
    result = model.predict('model1',(x_test.iloc[i]))
    predictedtag,weight = getTopic(result)
    if predictedtag == y_test.iloc[i]:
        numTrue += 1
    else:
        print("\nExpected:{} Predicted:{}\n{}".format(y_test.iloc[i],predictedtag,x_test.iloc[i]))
        numFalse += 1
        # print(numFalse)
        
print("\n")
print("Total: {} \n True: {} \n False: {}".format(len(x_test),numTrue,numFalse))

# https://medium.freecodecamp.org/how-we-changed-unsupervised-lda-to-semi-supervised-guidedlda-e36a95f3a164

# 800
# Total: 93648 
#  True: 418 
#  False: 382

# 800 if(penaltyCNT[val]<numtopics):
# Total: 93648 
#  True: 424 
#  False: 376

# 20
# Total: 93648 
#  True: 13 
#  False: 7

# last options: consider the word repeats within a document is to use tfidf to adjust weights