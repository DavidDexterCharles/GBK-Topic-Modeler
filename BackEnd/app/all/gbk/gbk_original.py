import json
# GBC(group by Key) Model by David Charles
# words in a doc are related, and the strength of the relation increases across multiple documents 
# as the co-occurence between words across the documents increase.

class GBK:
    
    def __init__(self):
        self.model = {}
        self.keycount = {}
        self.name = "gbk"
    def init(self,topics):
        for topic,topiclist in topics.items():
             self.model[topic] = {}
             self.keycount[topic]  = {}
             for i in range(0,len(topiclist)):
                keyword = topiclist[i]
                self.model[topic][keyword]={}
                self.model[topic][keyword]['features'] = {}
                self.keycount[topic][keyword] = 0
           
    def build(self,topics,articlecontent): #check and see if key word exists for each topic
        articlecontent = articlecontent.lower()
        for topic,topiclist in topics.items():
            print(topic)
            for i in range(0,len(topiclist)):
                keyword = topiclist[i]
                if keyword.lower() in articlecontent:
                    visited = {}
                    result = articlecontent.split()
                    for j in range(0,len(result)):
                            if result[j] in self.model[topic][keyword]['features'] :
                                if result[j] not in visited:
                                    self.model[topic][keyword]['features'][result[j]] += 1
                                    visited[result[j]] = 1
                            else:
                                self.model[topic][keyword]['features'][result[j]] = 1
                                visited[result[j]] = 1
                                
                    self.keycount[topic][keyword] += 1
                    self.model[topic][keyword]['features'][keyword] = self.keycount[topic][keyword] # Ensures Keyword is always 100 %
   
    def setweights(self,topics):
        for topic,topiclist in topics.items():
            for i in range(0,len(topiclist)):
               
                largestkey = 0 #each key word has its own feturevector, and hence its own average weighting value
                total = 0
                sumofweights = 0
                numberofweights = 0
                averageweight = 0
                keyword = topiclist[i]
                features = self.model[topic][keyword]['features']
                sortedweights = sorted(features.items(),key=lambda p:p[1])
                for k,v in sortedweights:
                    if largestkey < v:
                        largestkey = v # prevents counting duplicated weights
                        sumofweights += v
                        numberofweights += 1

                if(sumofweights > 0 and numberofweights>0):
                    averageweight = sumofweights/numberofweights
                    # maxaverageweight = (largestkey/averageweight)
                    for k,v in sortedweights:
                        averageweightofvalue = round(v/averageweight,6)
                        
                        # self.model[topic][keyword]['features'][k] = round((averageweightofvalue /maxaverageweight)*100,6)        
                        self.model[topic][keyword]['features'][k] = round((averageweightofvalue)*100,6)  
                else:
                    # print("Error: sumofweights or numberofweights was <= 0 {}".format(self.model[topic][keyword]['features']))
                    error =1
                
                # self.model[topic][keyword]['features'][keyword] = 100        # Ensures Keyword is always 100 %
                # print(self.model[topic][keyword]['features'])
        
    def tojson(self,path):
        self.name = path
        with open(self.name+'.json', 'w') as modelobj:
            json.dump(self.model, modelobj,sort_keys=True, indent=4)
        
    def load(self,path):
        with open(path, 'r') as fp:
            self.model = json.load(fp)
    
    def getAvergaePenalty(self,penalty):
        totalpenalty = 0
        for k,v in penalty.items():
            totalpenalty += v
        averagepenalty = totalpenalty/len(penalty)
        
        return averagepenalty
    
    def predict(self,modeloption,doc):
        docset = set(doc.lower().split())
        topic = {}
        penalty = {}
        # penaltyCNT = {}
        numberOftopics = len(self.model[modeloption].items())
        for row,col in self.model[modeloption].items():
            result = col['features'].keys() & docset
            for val in result:
                if val in penalty:
                    penalty[val] += col['features'][val]
                    # penaltyCNT[val] +=1
                else:
                    penalty[val] = col['features'][val]
                    # penaltyCNT[val] = 1
        
        for row,col in self.model[modeloption].items():
            result = col['features'].keys() & docset
            marker=1
            numberofterms = len(doc.lower().split())
            numtopics = len(self.model[modeloption])
            # print("{} {}".format(row,result))
            for val in result:
                scale = doc.lower().count(val)
                # print("Scale:{} Word:{} ScaleValue:{}".format(scale,val,(col['features'][val] * scale)))
                
                if (penalty[val] == col['features'][val]):
                    # print("ImportantWord {} = {}".format(val,col['features'][val]))
                    penalty[val]  = 1
                averagepenalty =  self.getAvergaePenalty(penalty)
                penaltyoutcome = penalty[val]/averagepenalty
                # if(penaltyCNT[val]<numtopics):
                if penaltyoutcome <=1:
                    # print("{} {}".format(val,penaltyoutcome))
                    if marker:
                        topic[row] = (col['features'][val] * scale)/penalty[val]
                        marker=0
                    else:
                        topic[row] +=  (col['features'][val] * scale)/penalty[val]
                # else:
                #     print("{} {}".format(val,penaltyoutcome))
                #     if marker:
                #         topic[row] = (col['features'][val])/penalty[val]  
                #         marker=0
                #     else:
                #         topic[row] +=  (col['features'][val])/penalty[val]  
        print(topic)
        # print("\nPenalty: {}".format(penalty))
        return (topic)
            
    def showfeatures(self):        
        for model,modelvalue in self.model.items():
            for row,col in modelvalue.items():
                sortedweights = sorted(col['features'].items(),key=lambda p:p[1],reverse=True)
                print("{}[{} : {}]".format(model,row,sortedweights))
                
    def showmodels(self):
        for model,modelvalue in self.model.items():
            print(model)
            
            
