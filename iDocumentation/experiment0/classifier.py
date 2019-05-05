from gbk.gbk import GBK as Model

model = Model()
model.load("sportsmodel.json")
document = "A  very close game was played during election and time but the election ended quickly"
# document = "A  very close game was played "

result = model.predict('model',document).getTopics()


print(result)


