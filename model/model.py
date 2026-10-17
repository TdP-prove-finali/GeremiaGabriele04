import copy
import itertools
import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._allNodes = []
        self._idMapCustomer = {}

    def buildGraph(self, country):
        self._graph.clear()
        self._graph.clear_edges()
        self._idMapCustomer.clear()

        self._allNodes = DAO.getAllNodes(country)
        for a in self._allNodes:
            self._idMapCustomer[a.CustomerId] = a

        self._graph.add_nodes_from(self._allNodes)
        self.addEdges(country)

    def addEdges(self, country):
        dictionaryID = DAO.getAllEdges(country, self._idMapCustomer)
        listaAggiunti = []

        listaCoppie = list(itertools.combinations(dictionaryID.keys(), 2))
        print(len(listaCoppie))

        for c in listaCoppie:
            if (c[0], c[1]) in listaAggiunti or (c[1], c[0]) in listaAggiunti:
                continue
            else:
                c1 = self._idMapCustomer[c[0]]
                c2 = self._idMapCustomer[c[1]]
                risultato = len(list(set(dictionaryID[c[0]]).intersection(dictionaryID[c[1]])))
                self._graph.add_edge(c1, c2, weight=risultato)
                listaAggiunti.append((c[1], c[0]))


    def getAllCountry(self):
        return DAO.getAllCountry()

    def getCustomers(self):
        return self._allNodes

    def getNumNodi(self):
        return len(self._graph.nodes)

    def getNumArchi(self):
        return len(self._graph.edges)