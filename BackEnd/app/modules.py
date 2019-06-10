from crawler.crawler import Crawler
from classifier.gbc import GBC as Classifier
from classifier.gbc import Merger
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
from collections import Counter 
import requests
import json
headers = {'Content-Type': 'application/json'}
apidomain = 'http://127.0.0.1:8081/api/'


class Modules(object):
    
    def getclassificationmodel(self):
        classifier = Classifier()
        result = json.dumps(classifier.load("classvectors.json"))
        return result
    
    def getCategory(self,query):
        # result = self.traversePages("setTopicandTerms",'topicmodel')
        classifier = Classifier()
        result = self.traversePages("setTopicandTerms",'topicmodel')
        classifier.init(result.topics,result.terms).MinKey(2)
        # classifier.load('articlemodel.json')
        classifier.load('classvectors.json')
        for key,arr in classifier.keys.items(): #Incremental Learning Implemented
            value = classifier.goodtopicscore(arr,query)
            print("{} {}".format(key,value))
            if value>0:
                classifier2 = Classifier()
                classifier2.init(result.topics,result.terms).MinKey(2)
                classifier2.build(query)
                merger = Merger()
                classvectormodels = []
                classvectormodels.append(classifier)
                classvectormodels.append(classifier2)
                merger.merge(classvectormodels)
            
        
        # classifier.init(result.topics,result.terms).MinKey(2)
        # classifier = self.traversePages("retrainClassifier",'article',classifier).classifier
        # classifier.setweights()
        # classifier.tojson('classvectors')
        classifier = Classifier()
        classifier.init(result.topics,result.terms).MinKey(2)
        classifier.load('merged.json')
        outcome = classifier.predict('model',query).getTopics()
        k = Counter(outcome) 
        # Finding 3 highest values 
        answer = k.most_common(3)  
        categories=outcome
        outcome={}
        outcome['categoriestop3']=answer
        outcome['categories']=categories
        outcome['document']=query
        outcome['categorieswordmatch'] = {}
        # outcome['wordmatches']['a']=1 #= classifier.termVectors
        # outcome['wordmatches']['b']=2
        for k,v in classifier.termVectors.items():
            outcome['categorieswordmatch'][k]=str(v)
            # print(k)
            # print(v)
        outcome['categoriesconfidence'] = {}    
        for k,arr in result.terms.items():
            value = classifier.goodtopicscore(arr,query.lower())
            outcome['categoriesconfidence'][k]=value
            # print("{} {}".format(k,value))
            value = 0
        # print(type(classifier.termVectors))
        # print(classifier.termVectors)
        return json.dumps(outcome)
    
    def traversePages(self,action,tablename,optionalParams=100):
        reQuest =requests.get(apidomain + tablename, headers=headers) #DatabaseAPI
        result = reQuest.json()
        numberofpages = result["total_pages"]
        actionObj = ""
        nextpage = 1
        if action == "setTopicandTerms":
            actionObj = TopicsandKeys(action)
        if action == "retrainClassifier":
            actionObj = ClassifierHelper(action,optionalParams)
            
        while nextpage <= numberofpages:
            actionObj = self.processResult(actionObj,result['objects'])
            nextpage += 1
            reQuest =requests.get(apidomain +tablename+'?page='+str(nextpage), headers=headers)
            result = reQuest.json()
        
        return actionObj
    
    def processResult(self,actionObj,result):
        if actionObj.action == "setTopicandTerms":
            actionObj.setTopicandTerms(result)
        if actionObj.action == "retrainClassifier":
            actionObj.retrainClassifier(result)
        return actionObj
    
    def getTopics(self):
        result = self.traversePages("setTopicandTerms",'topicmodel')
        
        
        classifier = Classifier()
        classifier.init(result.topics,result.terms).MinKey(2)
        
        classifier = self.traversePages("retrainClassifier",'article',classifier).classifier
        classifier.setweights()
        classifier.tojson("classvectors")
        return "test2"
    
    def uri_validator(self,x):
        try:
            result = urlparse(x)
            return all([result.scheme, result.netloc, result.path])
        except:
            return False
   
    def updateClassifier(self,query):
        return 1
        
        

class TopicsandKeys(object):
    def __init__(self,action):
        self.action = action
        self.topics ={}
        self.topics['model']=[]
        self.terms = {}
    
    def setTopicandTerms(self,result):
        for i in range(0,len(result)):
            category = result[i]['categorie']['name']
            keyword = result[i]['Keyword']['word']
            if category not in self.topics['model']:
                self.topics['model'].append(category)
                self.terms[category] = []
            self.terms[category].append(keyword) 

class ClassifierHelper(object):
    
    def __init__(self,action,classifier):
        self.action = action
        self.classifier = classifier
    
    def retrainClassifier(self,result):
         for i in range(0,len(result)):
            article = result[i]['CONTENT']
            self.classifier.build(article)