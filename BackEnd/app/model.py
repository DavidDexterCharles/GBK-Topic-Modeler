from crawler.crawler import Crawler
from classifier.gbc import GBC as Classifier
from collections import Counter 
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
        result = self.traversePages("setTopicandTerms",'topicmodel')
        classifier.init(result.topics,result.terms).MinKey(2)
        classifier.load('articlemodel.json')
        # classifier.load('classvectors.json')
        # classifier.init(result.topics,result.terms).MinKey(2)
        
        # classifier = self.traversePages("retrainClassifier",'article',classifier).classifier
        # classifier.setweights()
        # classifier.tojson('classvectors')
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
            print("{} {}".format(k,value))
            value = 0
        # print(type(classifier.termVectors))
        # print(classifier.termVectors)
        return json.dumps(outcome)
    
    def getKeyword(self,query):
        q = '?q={"filters":[{"name":"word","op":"eq","val":"'+query+'"}]}'
        result = requests.get(apidomain+'keyword'+q).content
        return result
    
    def createkeyword(self, request):
        data = json.dumps(request.get_json())
        return requests.post(apidomain + 'keyword', data, headers=headers).content

    def updatekeyword(self, request):
        data = json.dumps(request.get_json())
        return requests.patch(apidomain + 'keyword', data, headers=headers).content

    def deletekeyword(self, id):
        return requests.delete(apidomain + 'keyword/'+id, headers=headers).content
         
    def getallkeywords(self):
        return requests.get(apidomain + 'keyword', headers=headers).content
        
    def getbyidkeyword(self, id):
        return requests.get(apidomain + 'keyword/'+id, headers=headers).content
        
    def getTopics(self):
        result = self.traversePages("setTopicandTerms",'topicmodel')
        
        
        classifier = Classifier()
        classifier.init(result.topics,result.terms).MinKey(2)
        
        classifier = self.traversePages("retrainClassifier",'article',classifier).classifier
        classifier.setweights()
        classifier.tojson("classvectors")
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
        
    
   
    def get_article_data(self,request):
        # print(request.form['url'])
        # data = request.data
        
        '''
        Filter to see if the domain exists in domain table if it does then, get the id, if it does not then, 
        domain is unsupported and wont be added to the db, however best attempt classigication, would still be done.
        On submission of the url to the article table, if integrigity violated then just return the article with its categoriese
        '''
        
        #  q = '?q={"filters":[{"name":"domainname","op":"like","val":"%'+query+'%"}]}'
        # qresult = requests.get("http://0.0.0.0:8085/api/domain"+q).content
        
        data =request.get_json()
        # print(data['url'])
        if("trinidadexpress.com" in data['url']):
            spider = Crawler('https://www.trinidadexpress.com',"",['p'],['time'],['h1','headline'])
        elif("guardian.co.tt" in data['url']):
            spider = Crawler('https://www.guardian.co.tt',"",['p','bodytext'],['span','textelement-publishing date'],['h1','headline'])
        # elif("newsday.co.tt" in data['url']):
        #     spider = Crawler('https://newsday.co.tt',"",['p'],['time'],['h1'])
        elif("looptt.com" in data['url']):
            spider = Crawler('http://www.looptt.com',"",['p'],['span','date-tp-4 border-left'],['span','field field--name-title field--type-string field--label-hidden'])
        else:
            result = "Invalid Link"
        
        result = spider.get_article_data(data['url'])
        r = requests.post(apidomain + 'article', result, headers=headers)#use y api to post the data to database
        print(r)
        # result["domain_id"] = 1
        # elif("looptt.com" in data['url']):
        #     spider = Crawler('http://www.looptt.com',"",['p'],['i'],['h1','headline'])
        
        # print(result)
        return result