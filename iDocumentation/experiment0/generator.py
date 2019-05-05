from gbk.gbk import GBK as Model
from collections import Counter #https://www.geeksforgeeks.org/find-k-frequent-words-data-set-python/
# https://docs.python.org/2/library/collections.html
from documents import document
model = Model()

topics = {}
keys = {}
topics['model'] = ['sport','np']
keys['sport'] = ['sport','sports','game','ball','match']
keys['np'] = ['election','np','death']
# topics['model2'] = ['np','election','close']
# topics['model3'] = ['close']
model.init(topics).MinKey(2)

document1 = 'A great game sports death occur'
document2 = 'The election was over death np '
document3 = 'Very clean match, go ball sport'
document4 = 'A clean but forgettable game sports'
document5 = 'It was a close election np'
doclist = [document1, document2, document3, document4, document5]



# keyword = 'sport'
# for i in range(0,len(keys[keyword])):
#     wordcounter = Counter(doclist[0].lower().split()) 
#     print(wordcounter[keys[keyword][i]]) 
  
# print(wordcounter['death']) 


for i, doc in enumerate(doclist):
        model.build(topics,keys,doc)

print(model.model)
model.setweights(topics)
model.tojson("sportsmodel")

# https://stevenloria.com/tf-idf/
# 7