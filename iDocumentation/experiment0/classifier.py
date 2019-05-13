from gbk.gbk import GBK as Model

model = Model()
model.load("merged.json")
document = "At  election  time the game played on the news ended quickly"
# document = "A  very close sport game was played "


result = model.predict('model',document).getTopics()



print(result)


