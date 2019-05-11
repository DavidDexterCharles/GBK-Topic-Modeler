from gbk.gbk import GBK as Model
from collections import Counter #https://www.geeksforgeeks.org/find-k-frequent-words-data-set-python/
# https://docs.python.org/2/library/collections.html
from documents import document
model = Model()

topics = {}
keys = {}
# tags must be unique and must have a space before and after(to distinguish from other words)
topics['model'] = ['sport','notsport']
keys['sport'] = ['sp']#,'sports','game','ball','match']
keys['notsport'] = [' np']#,'np','death']
# topics['model2'] = ['np','election','close']
# topics['model3'] = ['close']
model.init(topics,keys)#.MinKey(2)

document1 = 'A great game sports  occur sp '
document2 = 'The election was over death np '
document3 = 'Very clean match, go ball sport sp '
document4 = 'A clean but forgettable game sports sp '
document5 = 'It was a close election np'
doclist = [document1, document2, document3, document4, document5]

# def countPhrase(key,content):
#     i=0
#     while key in content:
#         i+=1
#         content = content.replace(key,"",1)
#     return i

# print(countPhrase("have a nice","i,have a nice comma,have a yes but I also have a nice way to live"))
# keyword = 'sport'
# for i in range(0,len(keys[keyword])):
#     wordcounter = Counter(doclist[0].lower().split()) 
#     print(wordcounter[keys[keyword][i]]) 
  
# print(wordcounter['death']) 


for i, doc in enumerate(doclist):
        model.build(doc)

print(model.model["model"]["notsport"]["features"])
print(model.model["model"]["sport"]["features"])
print("\n")
model.setweights()

print(model.model["model"]["notsport"]["features"])
print(model.model["model"]["sport"]["features"])
print("\n")
model.tojson("sportsmodel")

model.removeweights()
print(model.model["model"]["notsport"]["features"])
print(model.model["model"]["sport"]["features"])

model.setweights()

print(model.model["model"]["notsport"]["features"])
print(model.model["model"]["sport"]["features"])
print("\n")

# https://stevenloria.com/tf-idf/
# 7