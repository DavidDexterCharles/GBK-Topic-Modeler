from gbk.gbk import GBK as Model

model = Model()
model.load("sportsmodel.json")
document = "A very close game fun sports"

result = model.predict('model',document)

print(result)
