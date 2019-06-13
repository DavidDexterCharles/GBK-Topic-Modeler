from classifier.gbc import GBC as Model
from classifier.gbc import Merger


model1 = Model()
model2 = Model()

model1.load("articlemodel.json")
model2.load("classvectors.json")
# model1.setweights()
# model2.setweights()
# model1.removeweights()
# model2.removeweights()

merger = Merger()
models = []
models.append(model1)
models.append(model2)
merger.merge(models)