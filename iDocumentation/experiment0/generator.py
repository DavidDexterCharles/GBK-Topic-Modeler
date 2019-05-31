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


for i, doc in enumerate(doclist):
        model.build(doc)


# print(model.model["model"]["notsport"]["features"])

# import pandas as pd #https://github.com/mayank408/TFIDF/blob/master/TFIDF.ipynb

# classvectors = [model.model["model"]["notsport"]["features"], model.model["model"]["sport"]["features"]]
# result = pd.DataFrame(classvectors)
# # print(result)
# bowNotsport = list(model.model["model"]["notsport"]["features"].keys())
# bowSport = list(model.model["model"]["sport"]["features"].keys())
# # print(bowNotsport)

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

# print(tfbow)

# tfBowNotsport = computeTF(classvectors[0], bowNotsport)
# tfBowSport = computeTF(classvectors[1], bowSport)
# print(tfBowNotsport)

# print(classvectors)

# print(idfs)

# tfidfBowNotsport = computeTFIDF(tfBowNotsport, idfs)
# tfidfBowSport = computeTFIDF(tfBowSport, idfs)
# model.model["model"]["notsport"]["features"] = tfidfBowNotsport
# model.model["model"]["sport"]["features"] = tfidfBowSport
# print(tfidfBowNotsport)

model.setweights()
model.tojson("sportsmodelTFIDF")



# print(model.model["model"]["notsport"]["features"])
# print(model.model["model"]["sport"]["features"])
# print("\n")
# model.setweights()

# print(model.model["model"]["notsport"]["features"])
# print(model.model["model"]["sport"]["features"])
# print("\n")
# model.tojson("sportsmodel")

# # model.removeweights()
# print(model.model["model"]["notsport"]["features"])
# print(model.model["model"]["sport"]["features"])
# model.tojson("sportsmodel")
# model.setweights()

# print(model.model["model"]["notsport"]["features"])
# print(model.model["model"]["sport"]["features"])
# print("\n")

# print(model.topics)
# https://stevenloria.com/tf-idf/
# 7