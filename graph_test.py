from queue_test import *
class Vertext:
    def __init__(self,key):
        self.id = key
        self.color = "white"
        self.distance = 0
        self.prev = None
        self.connectedTo = {}

    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color = color

    def getDistance(self):
        return self.distance
    def setDistance(self,d):
        self.distance = d
    def getPrev(self):
        return self.prev
    def setPrev(self,prev):
        self.prev = prev

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo:' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices +1
        newVertext = Vertext(key)
        self.vertList[key] = newVertext
        return newVertext

    def getVertext(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(n)
        self.vertList[f].addNeighbor(self.vertList[t],cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values)


def bfs(g,s):
    s.setColor("black")
    s.setDistance(0)
    s.setPrev(None)

    q = Queue()
    q.enqueue(s)

    while q.length()>0:
        currenVertext = q.dequeue()
        nbs = currenVertext.getConnections()
        for i in nbs:
            if i.getColor =="white":
                i.setColor("grey")
                i.setDistince(currenVertext.getDistance() +1)
                i.setPrev = currenVertext
                q.enqueue(i)
        currenVertext.setColor("black")






