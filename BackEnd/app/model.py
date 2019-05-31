from crawler.crawler import Crawler
from classifier.gbc import GBC as Classifier
import requests
import json
headers = {'Content-Type': 'application/json'}
apidomain = 'http://127.0.0.1:8081/api/'


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


class Model(object):
    
    def getCategory(self,query):
        # result = self.traversePages("setTopicandTerms",'topicmodel')
        classifier = Classifier()
        classifier.load('articlemodel.json')
        # classifier.init(result.topics,result.terms).MinKey(2)
        
        # classifier = self.traversePages("retrainClassifier",'article',classifier).classifier
        # classifier.setweights()
        # classifier.tojson('classvectors')
        outcome = classifier.predict('model',query).getTopics()
        outcome['Answer']=classifier.predict('model',query).getTopic()
        print(outcome)
        return json.dumps(outcome)
        
    def getTopics(self):
        result = self.traversePages("setTopicandTerms",'topicmodel')
        
        
        classifier = Classifier()
        classifier.init(result.topics,result.terms).MinKey(2)
        
        classifier = self.traversePages("retrainClassifier",'article',classifier).classifier
        classifier.setweights()
        classifier.tojson("classvectors")
        classifier.predict()
        return "test2"
    
    
    
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
        
    
    
        
    def updateClassifier(self,query):
        return 1
    
    
    def getalltopicmodels(self):
        return requests.get(apidomain + 'topicmodel', headers=headers).content
    
    def getallKeyWords(self):
        return requests.get(apidomain + 'keyword', headers=headers).content
        
    def getcategoriekey(self,query):
        q = '?q={"filters":[{"name":"name","op":"eq","val":"'+query+'"}]}'
        result = requests.get(apidomain+"categorie"+q, headers=headers).content
        return result