from pages import page
from documents import document
from gbk.gbk import GBK as Model

def getTopic(topic):
    largest = 0
    key = ""
    for k,v in topic.items():
        if v > largest:
            largest = v
            key = k
    return key, largest


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
    'award','labor','politics',
    'religion','society','sport'
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
keys['environment']=["environment","climate",'climate change','energy','water','pollution','waste','sea','forest']
keys['health']=["health","healthcare",'hospital','medicine']
keys['award']=["award","prize",'celebrity','animal']
keys['labor']=["labour","labor",'employment','unemployment']
keys['politics']=["politic","democrat",'republican','election','policy',"president","secretary","minister"]
keys['religion']=["religion","christian",'Mosk','Hindu','church']
keys['society']=["society","ethnic",'ethnic group','communities','poverty','family','homeless','immigration','marriage','population','migration']
keys['sport']=['coach','Racing','winning','champion','matches','games','tournament','win','Cycling',"sport","nfl",'nba','football','basketball','boxing','tennis','cricket','olynmpic','athletic','swimming','cycling']

model.init(topics).setMinMatch(2)


for i in range(0,len(page)):
            model.build(topics,keys,page[i])
model.setweights(topics)
model.tojson("articlemodel")

doc = document[0]
result = model.predict('model',doc).getTopic()

print('Model: {}'.format(result))


# https://www.trinidadexpress.com/news/local/years-for-v-zuelan-on-card-fraud/article_08674e0e-6ae3-11e9-b452-bfb77340e04f.html

# https://www.trinidadexpress.com/news/local/years-for-v-zuelan-on-card-fraud/article_08674e0e-6ae3-11e9-b452-bfb77340e04f.html