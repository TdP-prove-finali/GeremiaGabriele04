import copy
import itertools

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._allNodes = []
        self._idMapArtist = {}
        self._bestPath = []
        self._bestScore = 0

    def getAllCountry(self):
        return DAO.getAllCountry()