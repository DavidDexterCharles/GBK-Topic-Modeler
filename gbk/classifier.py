from gbk.gbk import GBK as Model

model = Model()
model.load("sportsmodel.json")
document = "A  very close game was played during election and time but the election ended quickly"
model.setpenaltyborder(100)
# the point at which words supposedly related are ignored, due to the extent to which they are repeated in other term vectors
# Higher the penalty border the more words allowed, it was observed that ignoreing words above average penalty helps to penalise words that repeat
# accross vectors, however in the event that we want to classify based on grouping of term vectors(that is multiple models),
# then increaseing the penalty border is recommended so that term vectors within a particular model wont compete to much with each other
result = model.predict('model',document)
result2 = model.predict('model2',document)

print(result)
print(result2)
