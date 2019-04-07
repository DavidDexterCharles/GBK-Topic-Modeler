from gbk.gbk import GBK as Model

model = Model()

topics = {}
topics['model'] = ['sport','np']
model.init(topics)

document1 = 'A great game Sports'
document2 = 'The election was over np '
document3 = 'Very clean match, go ball sport'
document4 = 'A clean but forgettable game sports'
document5 = 'It was a close election np'
doclist = [document1, document2, document3, document4, document5]

for i, doc in enumerate(doclist):
        model.build(topics,doc)

print(model.model)
model.setweights(topics)
model.tojson("sportsmodel")

# 7