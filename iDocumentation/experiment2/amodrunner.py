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
    'award',
    'labor',
    'politics',
    'religion',
    'society',
    'sport'
]
keys ={}
keys['art'] =['art','culture','entertainment','music','history',
'film','media','book','fashion','festival','comedy','museums','opera',
'drama','poetry','documentary','painting','theatre','sculpture','carnival','celebrate']
keys['school'] = ["school","education","teach","student","lecturer",
"Campus","academic","university"]
keys['crime'] = ['crime','Magistrate','law','rape','supreme-court','human-rights','police','criminal-justice','shot','shooting','dead']
keys['disaster'] = ['flood',"natural","disaster",'natural disaster','hurricane','flooding',
'earthquake','drought','wildfire','forest fire','fire','Volcano']
keys['economy']=['insurance','banking','Financial',"economy","business",'economics','banking',
'advertising','transport','market','realestate','investing','finance','shareholders']
keys['environment']=["environment",
"climate",'climate change','energy',
'water','pollution','waste','sea','forest','season','Volcano','mountain','clouds']
keys['health']=["health","healthcare",'hospital','medicine','drug','cancer','multivitamins']
keys['award']=["award","prize",'celebrity','animal']
keys['labor']=["labour","labor",'employment','unemployment']
keys['politics']=['prosecution','Senator',"politic",
"democrat",'republican','election',
'policy',"president","secretary",
"Minister"]
keys['religion']=["religion","christian",'Mosk','Hindu','church']
keys['society']=["society","ethnic",'ethnic group','communities','poverty','family','homeless','immigration','marriage','population','migration']
keys['sport']=['medals','games','volleyball','Coaching','captain','coach','Racing',
'winning','champion','match','game','tournament','win','Cycling',"sport","nfl",'nba','football','basketball',
'boxing','tennis','cricket','olynmpic','athletic','swimming','cycling']

model.init(topics).MinKey(2)

doc = document[0]


# https://monkeylearn.com/text-classification/
# https://www.researchgate.net/post/What_is_a_scientific_contribution
# A contribution in Science is a result which is: new, useful and applicable

#  A scientific contribution is anything which adds to the current knowledge
#  of science or other fields and the number of things that can be achieved by it.
#  It might be a discovery, an innovation, etc. that contribute to society development.


# https://monkeylearn.com/text-classification/
# https://www.quora.com/What-are-the-advantages-and-disadvantages-of-TF-IDF
# https://www.reddit.com/r/MachineLearning/comments/1inxnq/how_to_factor_in_tfidf_with_naive_bayes/

# Word Importance in the Naieve Bayes approach the weights used when trying to get
# the the model to be more accurate in prediction is often times the tf-idf weights, 
# Justification:
# think about it as transforming the documents: before, each word in each document counted as 1,
# but after, the words in the documents are counted as their TF-IDF weight. 
# Then you get your probabilities for Naive Bayes using the formula
# P(word|class)=(word_count_in_class + 1)/(total_words_in_class+total_unique_words_in_class) 

# However with the presented algorithm: Tf-Idf isn't needed for the penalisation of certain kewords to work also, 
# Treating t

# for i in range(0,len(page)):
#             model.build(topics,keys,applynounfilter(page[i]))
# for i in range(0,len(document)):
#             model.build(topics,keys,(document[i]))
            
# model.setweights(topics)
# model.tojson("articlemodel")
model.load("articlemodel.json")



print("========================================================")

maxconsidered = 0
value = 0
for key,arr in keys.items():
    # print(arr)
    value = model.goodtopicscore(arr,doc.lower())
    # if vlaue >= maxconsidered:
    print("{} {}".format(key,value))
    value = 0


print("Answer:{}".format(model.predict('model',(doc)).getTopic()))
result = model.predict('model', (doc)).getTopics()
print('Model: {}\n'.format(result)) 

# print(model.penalty)
# print(model.termVectors['economy'])
# print(model.termVectors['sport'])

print(applynounfilter(doc)) #applynounfilter


# https://www.trinidadexpress.com/news/local/years-for-v-zuelan-on-card-fraud/article_08674e0e-6ae3-11e9-b452-bfb77340e04f.html

# https://www.trinidadexpress.com/news/local/years-for-v-zuelan-on-card-fraud/article_08674e0e-6ae3-11e9-b452-bfb77340e04f.html

'''
 FORMER West Indies captain Brian Lara turns 50 tomorrow week celebrations mark half-century, including T20 match at newly renovated Diego Martin Sporting Complex tonight.

Lara reflective mood yesterday invited media home Lady Chancellor Hill share toast reveal more personal side man who now grandfather.
'''