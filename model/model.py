import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = DAO.getAllNodes()
        self._idMap = {}
        for v in self._nodes:
            self._idMap[v.object_id] = v

    def buildGraph(self):
        self._graph.add_nodes_from(self._nodes)
        self.addAllEdges()

    def addEdgesV1(self):
        for u in self._nodes:
            for v in self._nodes:
                peso = DAO.getPeso(u,v)
                if peso != None :
                    self._graph.add_edge(u, v,weight=peso)


    def addAllEdges(self):
        allEdges = DAO.getAllArchi(self._idMap)
        for e in allEdges:
            self._graph.add_edge(e.o1, e.o2,wight = e.peso)

    def getInfoConnessa(self,idInput):
        """
        Identifica la componente connessa che contiene idInput e ne restituisce la dimensione
        """
        if not self.hasNode(idInput):
            return None

        # Deep First Search
        source = self._idMap[idInput]

        # Modo 1: conto i successori
        succ = nx.dfs_successors(self._graph,source)
        print(succ)

    def hasNode(self,idInput):
        # return self._idMao[idInput] in self._graph
        return idInput in self._idMap

    def getNumNodes(self):
        return len(self._graph.nodes())

    def getNumEdges(self):
        return len(self._graph.edges())

    # def getIdMap(self):
    #     return self._idMap
