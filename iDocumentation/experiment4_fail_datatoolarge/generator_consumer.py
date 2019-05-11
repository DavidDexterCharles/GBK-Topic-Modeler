from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.naive_bayes import MultinomialNB

import numpy as np
import pandas as pd
from gbc_code.helper import *
from gbc_code.gbc import Gbc as Model


df = pd.read_csv('Consumer_Complaints.csv')
df = df[pd.notnull(df['Consumer complaint narrative'])]
col = ['Product', 'Consumer complaint narrative']
df = df[col]

df.columns = ['Product', 'Consumer_complaint_narrative']
topics = {}
topics['model1'] = ['Prepaid card', 'Vehicle loan or lease', 'Mortgage', 'Virtual currency', 'Payday loan', 'Debt collection', 'Student loan', 'Bank account or service', 'Money transfer, virtual currency, or money service', 'Consumer Loan', 'Checking or savings account', 'Credit reporting', 'Credit reporting, credit repair services, or other personal consumer reports', 'Money transfers', 'Other financial service', 'Credit card', 'Credit card or prepaid card', 'Payday loan, title loan, or personal loan']

x_train, x_test, y_train, y_test = train_test_split(df['Consumer_complaint_narrative'], df['Product'], random_state = 0)

model = Model()
model.init(topics)
for i in range (0,len(x_train)):
    model.build(topics,(x_train.iloc[i])+" "+y_train.iloc[i])  
    print(y_train.iloc[i])
    # topic['model1'].add(y_train.iloc[i])
model.setweights(topics)
model.tojson("exp22")
print(topics['model1'])
# f = open("topics.txt", "w")
# f.write(str(topic['model1']))