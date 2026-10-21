import copy
import itertools
import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._allNodes = []
        self._idMapCustomer = {}
        self._allTracks = []
        self._idMapTrack = {}
        self._allEmployees = []
        self._idMapEmployee = {}

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
                print(c[0], c[1], risultato)
                self._graph.add_edge(c1, c2, weight=risultato)
                listaAggiunti.append((c[1], c[0]))

    def getCrossSellingPlan(customer):
        pass


    def getAllCountry(self):
        return DAO.getAllCountry()

    def getCustomers(self):
        return self._allNodes

    def getNumNodi(self):
        return len(self._graph.nodes)

    def getNumArchi(self):
        return len(self._graph.edges)

    def getTop5Customers(self, country):
        listaIDTotal = DAO.getAllTotali(country)
        dictionaryIDTrack = DAO.getAllEdges(country, self._idMapCustomer)
        lista = []
        #[(idC, numTrack, total), ...]

        for tupla in listaIDTotal:
            customer = self._idMapCustomer[tupla[0]]
            numTrack = len(list(dictionaryIDTrack[tupla[0]]))
            total = float(tupla[1])
            lista.append((customer, numTrack, total))

        return lista[:5]

    def getTop5Tracks(self, country):
        self._idMapTrack.clear()

        self._allTracks = DAO.getAllTracks(country)
        for a in self._allTracks:
            self._idMapTrack[a.TrackId] = a

        listaIDAcquisti = DAO.getAllAcquisti(country)
        dictionaryArtistAlbumGenre = DAO.getAllArtistAlbumGenre(country)
        lista = []
        for tupla in listaIDAcquisti:
            track = self._idMapTrack[tupla[0]]
            artist = dictionaryArtistAlbumGenre[tupla[0]][0]
            album = dictionaryArtistAlbumGenre[tupla[0]][1]
            genre = dictionaryArtistAlbumGenre[tupla[0]][2]
            lista.append((track, tupla[1], artist, album, genre))

        return lista[:5]

    def getRankEmployees(self, country):
        self._idMapEmployee.clear()

        self._allEmployees = DAO.getAllEmployees(country)
        for a in self._allEmployees:
            self._idMapEmployee[a.EmployeeId] = a

        dictionaryEmpStats = DAO.getAllEmpStats(country)
        lista = []
        for idEmp in dictionaryEmpStats.keys():
            emp = self._idMapEmployee[idEmp]
            numClienti = dictionaryEmpStats[idEmp][0]
            numTracce = dictionaryEmpStats[idEmp][1]
            ricavo = float(dictionaryEmpStats[idEmp][2])
            lista.append((emp, numClienti, numTracce, ricavo))

        return lista







