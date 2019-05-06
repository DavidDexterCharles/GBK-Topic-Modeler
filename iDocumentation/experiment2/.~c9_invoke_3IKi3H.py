from pages import page
from documents import document
from gbk.gbk import GBK as Model
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize 


def remove_stop_words(words):
    customStopWords = ['into','on','was','very','he','she','a','of','to','his','her','the', 'it', 'not','as','also','from','is','for','we','in',"which","are","and","having","have","has"]
    for k in customStopWords:
        words = words.replace(' '+k+' '," ")
    return words

def applynounfilter(thedata):
    tokenized = nltk.word_tokenize(thedata)
    is_noun = lambda pos: pos[:2] == 'NN'
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    # nouns = remove_stop_words(nouns)
    thedata = ' '.join(nouns)
    # thedata = re.sub("[-()\"#/@;:<>{}`+=~*\\|.!?,]", "", thedata)
    
    # print(thedata)
    return thedata

model = Model()
topics ={}
# topics['model'] = [
#     'ar1t','sch1ool','cr1ime',
#     # 'di1saster', 'ec1onomy',
#     # 'en1vironment','he1alth',
#     # 'aw1ard','labor','po1litics',
#     # 're1ligion','so1ciety','sp1ort'
# ]
topics['model'] = [
    'art',
    'school',
    'crime',
    'disaster',
    'economy',
    'environment','health',
keys['sport']=['captain','coach','Racing','winning','champion','matches','game','tournament','win','Cycling',"sport","nfl",'nba','football','basketball','boxing','tennis','cricket','olynmpic','athletic','swimming','cycling']
    'religion',
    # 'society',
    'sport'
]
keys ={}
keys['art'] =['art','culture','entertainment','music','history',
'film','media','book','fashion','festival','comedy','museums','opera',
'drama','poetry','documentary','painting','theatre','sculpture']
keys['school'] = ["school","education","teach","student","lecturer",
"Campus","academic","university"]
keys['crime'] = ['crime','Magistrate','law','rape',
'supreme-court','human-rights','police','criminal-justice','shot','shooting','dead']
keys['disaster'] = ['flood',"natural","disaster",'natural disaster','hurricane','flooding','earthquake','drought','wildfire','forest fire','fire']
keys['economy']=["economy","business",'economics','banking','advertising','transport','market','realestate','investing']
keys['environment']=["environment","climate",'climate change','energy','water','pollution','waste','sea','forest','season']
keys['health']=["health","healthcare",'hospital','medicine']
keys['award']=["award","prize",'celebrity','animal']
keys['labor']=["labour","labor",'employment','unemployment']
keys['politics']=["politic","democrat",'republican','election','policy',"president","secretary","minister"]
keys['religion']=["religion","christian",'Mosk','Hindu','church']
# keys['society']=["society","ethnic",'ethnic group','communities','poverty','family','homeless','immigration','marriage','population','migration']
keys['sport']=['captain','coach','Racing','winning','champion','match','game','tournament','win','Cycling',"sport","nfl",'nba','football','basketball','boxing','tennis','cricket','olynmpic','athletic','swimming','cycling']

model.init(topics).MinKey(2)


for i in range(0,len(page)):
            model.build(topics,keys,page[i])
# for i in range(0,len(document)):
#             model.build(topics,keys,(document[i]))
            
model.setweights(topics)
model.tojson("articlemodel")

doc = document[7]

result = model.predict('model',(doc)).getTopics()
print("========================================================")
print(model.goodtopicscore(keys['c'],doc))

print('Model: {}\n'.format(result)) 

# print(model.penalty)
# print(model.termVectors['sport'])
# print(model.termVectors['crime'])

print(remove_stop_words(doc)) 


# https://www.trinidadexpress.com/news/local/years-for-v-zuelan-on-card-fraud/article_08674e0e-6ae3-11e9-b452-bfb77340e04f.html

# https://www.trinidadexpress.com/news/local/years-for-v-zuelan-on-card-fraud/article_08674e0e-6ae3-11e9-b452-bfb77340e04f.html

'''
 FORMER West Indies captain Brian Lara turns 50 tomorrow week celebrations mark half-century, including T20 match at newly renovated Diego Martin Sporting Complex tonight.

Lara reflective mood yesterday invited media home Lady Chancellor Hill share toast reveal more personal side man who now grandfather.
'''