from database.DAO import DAO
from model.model import Model

listObject = DAO.getAllNodes()
mymodel = Model()
mymodel.buildGraph()

edges = DAO.getAllArchi(mymodel.getIdMap())

print(len(listObject),len(edges))