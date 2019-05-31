from crawler.crawler import Crawler
from classifier.gbc import GBC as Classifier
import requests
import json
headers = {'Content-Type': 'application/json'}
apidomain = 'http://127.0.0.1:8081/api/'


class TopicModel(object):
    def __init__(self,action):
        self.action = action
        self.topics ={}
        self.topics['model']=[]
        self.terms = {}
    
    def setTopicandTerms(self,result):
        # print ("tesr")
        # # print(result)
    
        for i in range(0,len(result)):
            category = result[i]['categorie']['name']
            keyword = result[i]['Keyword']['word']
            if category not in self.topics['model']:
                self.topics['model'].append(category)
                self.terms[category] = []
            self.terms[category].append(keyword) 
        


class Model(object):
    
    
    def getTopics(self):
        apiroute ='topicmodel'
        result = self.traversePages("setTopicandTerms",apiroute)
        print(result.topics)
        print(result.terms)
        return "test2"
    
    
    
    def traversePages(self,action,tablename):
        reQuest =requests.get(apidomain + tablename, headers=headers) #DatabaseAPI
        result = reQuest.json()
        numberofpages = result["total_pages"]
        actionObj = ""
        nextpage = 1
        if action == "setTopicandTerms":
            actionObj = TopicModel(action)
            
        while nextpage <= numberofpages:
            actionObj = self.processResult(actionObj,result['objects'])
            nextpage += 1
            reQuest =requests.get(apidomain +tablename+'?page='+str(nextpage), headers=headers)
            result = reQuest.json()
        
        return actionObj
    
    def processResult(self,actionObj,result):
        if actionObj.action == "setTopicandTerms":
            actionObj.setTopicandTerms(result)
        return actionObj
        
    
    def getCategory(self,query):
        return self.getalltopicmodels()
        
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