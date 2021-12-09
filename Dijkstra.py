# -*- coding: utf-8 -*-
import math
from queue import PriorityQueue
import pandas as pd

class Vertex:

    def __init__(self, vname):
        self.vname = vname
        self.d = math.inf
        self.Π = None

class Graph:

    def __init__(self, G):
        self.matrix = pd.DataFrame(columns=G, index=G)
        for i in range(len(G)):
            self.matrix.iloc[i, i] = 0

    def add_edge(self, u, v, weight):
        self.matrix.loc[u, v] = weight

#将所有的vertex添加到list中
def Initialize_Single_Source(G, s):
    v_G = []
    for i in G:
        v = Vertex(i)
        if i == s:
            v.d = 0
        v_G.append(v)
    return v_G

# 返回节点u的所有邻接点
def getAdjV(w, u):
    adjV = list(w.loc[u, :].dropna(axis=0, how='any').index)
    adjV.remove(u)
    return adjV

# 优先队列保持小顶堆的性质
def keepHeap(Q):
    R = PriorityQueue()
    while not Q.empty():
        R.put(Q.get())
    return R

def Dijkstra(G, w, s):
    # 初始化图中所有的点
    v = Initialize_Single_Source(G, s)
    S = []
    # 所有点入队列
    Q = PriorityQueue()
    for i in range(len(G)):
        Q.put([v[i].d, v[i].Π, v[i].vname])

    while not Q.empty():
        current_vertext = Q.get()
        print("u==",current_vertext)
        S.append([current_vertext[0], current_vertext[1],current_vertext[2]])
        for adj_vertext_name in getAdjV(w, current_vertext[2]):
            # 找到优先队列中u的邻接点然后修改
            for q in Q.queue:
                if adj_vertext_name == q[2]:
                    # 松弛
                    if q[0] > current_vertext[0] + w.loc[current_vertext[2], adj_vertext_name]:
                        q[0] = current_vertext[0] + w.loc[current_vertext[2], adj_vertext_name]
                        q[1] = current_vertext[2]
                    Q = keepHeap(Q)#调整完后，重新整理成最小堆
        print(Q.queue)
    print(S)
if __name__ == '__main__':
    G = ['s', 't', 'x', 'y', 'z']
    graph = Graph(G)
    # 10条边
    graph.add_edge('s', 't', 10)
    graph.add_edge('s', 'y', 5)

    graph.add_edge('t', 'x', 1)
    graph.add_edge('t', 'y', 2)

    graph.add_edge('x', 'z', 4)

    graph.add_edge('y', 't', 3)
    graph.add_edge('y', 'x', 9)
    graph.add_edge('y', 'z', 2)

    graph.add_edge('z', 's', 7)
    graph.add_edge('z', 'x', 6)

    w = graph.matrix

    Dijkstra(G, w, 's')
