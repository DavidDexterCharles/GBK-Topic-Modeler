from gbk.gbk import GBK as Model
from topics import topics
import requests
headers = {'Content-Type': 'application/json'}
# apidomain = 'http://127.0.0.1:8082/'
apidomain = 'http://127.0.0.1:8085/api/'
model = Model()

# https://flask-restless.readthedocs.io/en/stable/requestformat.html#clientpagination
article = requests.get(apidomain + 'article', headers=headers).json()
document1 = 'A great game Sports'
document2 = 'The election was over np '
document3 = 'Very clean match, go ball sport'
document4 = 'A clean but forgettable game sports'
document5 = 'It was a close election np'
doclist = [document1, document2, document3, document4, document5]
print(len(article["objects"]))
# ?page=1
numberofpages = article["total_pages"]
nextpage = 1
while nextpage <= numberofpages:
    for i in range(0,len(article["objects"])):
        print(article["objects"][i]["id"])
        doclist.append(article["objects"][i]["CONTENT"])
    nextpage += 1
    article = requests.get(apidomain + 'article?page='+str(nextpage), headers=headers).json()

# print(article["objects"][i]["CONTENT"])

modeltopic = {}
modeltopic['Art and Culture'] = topics['Art and Culture']
models = []
models.append(Model())
models[0].init(topics)

# model.init(topics)



for i, doc in enumerate(doclist):
        models[0].build(topics,doc)

# print(model.model)
model.setweights(modeltopic)
model.tojson("articlemodel2")

# 7