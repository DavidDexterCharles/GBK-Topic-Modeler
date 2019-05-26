from gbc.gbc import GBC as Model

model = Model()

topics        = {}
topictags     = {}

topics['model']  = ['sport','notsport']
topictags['sport']    = ['sp']
topictags['notsport'] = ['np']

model.init(topics,topictags)
model.tojson("model_Initial")

document1 = 'A great game sports  occur sp '
document2 = 'The election was over  np '
document3 = 'Very clean match sp '
document4 = 'A clean but unforgettable game sp '
document5 = 'It was a close election np'
doclist = [document1, document2, document3, document4, document5]

for i in range(0,len(doclist)):
    model.build(doclist[i])

model.tojson("model_NotStandardized")


model.setweights()
model.tojson("model_Standardized")

model.removeweights()
model.tojson("model_destandardized")
model.removeweights()



document6 = 'There was a nurder at broadway crime'

# from gbc.gbc import Merger

# model2 = Model()
# topics['model']  = ['crimeactivity']
# topictags['crimeactivity']    = ['crime']


# model2.init(topics,topictags)

# model2.build(document6)

# print(model2.model)
# print(model.model)

# merger = Merger()
# themodels = [model,model2]

# merger.merge(themodels)

# A great game”	Sports
# “The election was over”	Not sports
# “Very clean match”	Sports
# “A clean but forgettable game”	Sports
# “It was a close election”	Not sports


# for i, doc in enumerate(doclist):
#         model.build(doc)


# model.setweights()


# model.tojson("model")


# print(model.topics)
# https://stevenloria.com/tf-idf/
# 7