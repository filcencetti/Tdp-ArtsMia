from model.model import Model

mymodel = Model()

mymodel.buildGraph()

print(f"{mymodel.getNumNodes()},{mymodel.getNumEdges( )}")

mymodel.getInfoConnessa(1234)