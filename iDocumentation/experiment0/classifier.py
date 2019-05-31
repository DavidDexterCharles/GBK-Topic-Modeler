from gbk.gbk import GBK as Model

model = Model()
# model.load("merged.json")
model.load("sportsmodelTFIDF.json")

document1 = "At  election  time the game of politics is played"
document2 = "A  very close sport game was played "


result1 = model.predict('model',document1).getTopics()
result2 = model.predict('model',document2).getTopics()



print("Result1:{}\nResult2:{}".format(result1,result2))


