from crawler.crawler import Crawler
from classifier.gbc import GBC as Classifier
import requests
import json
headers = {'Content-Type': 'application/json'}
apidomain = 'http://127.0.0.1:8081/api/'



class Model(object):
    
    def getCategory(self,query):
        return self.getalltopicmodels()
        
    def updateClassifier(self,query):
        return 1
    
    def getTopics(self):
        result = requests.get(apidomain + 'topicmodel', headers=headers).json()
        data = json.dumps(result["objects"][0])
        return data
    
    def getalltopicmodels(self):
        return requests.get(apidomain + 'topicmodel', headers=headers).content
    
    def getallKeyWords(self):
        return requests.get(apidomain + 'keyword', headers=headers).content
        
    def getcategoriekey(self,query):
        q = '?q={"filters":[{"name":"name","op":"eq","val":"'+query+'"}]}'
        result = requests.get(apidomain+"categorie"+q, headers=headers).content
        return result