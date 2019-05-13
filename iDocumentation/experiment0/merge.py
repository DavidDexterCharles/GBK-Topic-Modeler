from gbk.gbk import GBK as Model
from gbk.gbk import Merger

topics ={}
topics2 ={}
keys = {}
topics['model'] = ['sport','notsport']
topics2['model'] = ['sport','notsport','election']
keys['sport'] = ['sp']
keys['notsport'] = ['np']
keys['election'] = ['elc','election']

model1 = Model()
model2 = Model()
model1.init(topics,keys)
model2.init(topics,keys)

document1 = 'A great game sports  occur sp '
document2 = 'The election was over death np elc'
document3 = 'Very clean match, go ball sport sp '
document4 = 'A clean but forgettable game sports sp '
document5 = 'It was a close election np elc'
document6 = 'The new president Trump won the election elc'
doclist1 = [document1, document2, document3]
doclist2 = [document4, document5]

for i in range (0,len(doclist1)):
    # print(doclist1[i])
    model1.build(doclist1[i])
    
# print(model1.model)
for i in range (0,len(doclist2)):
    model2.build(doclist2[i])
    
print(model2.model)
# model1.load("sportsmodel1.json")
# model2.load("sportsmodel2.json")
model1.setweights()
model2.setweights()
# model1.removeweights()
# model2.removeweights()
model1.tojson("sportsmodel1")
model2.tojson("sportsmodel2")

# model1.load("sportsmodel1.json")
# model2.load("sportsmodel2.json")
# # model1.setweights()
# model2.setweights()
# model1.tojson("sportsmodel1")
# model2.tojson("sportsmodel2")
# print(model1.model)
merger = Merger()
models = []
models.append(model1)
models.append(model2)
merger.merge(models)