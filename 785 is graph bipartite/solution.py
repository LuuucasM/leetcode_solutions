from typing import List

class UnionFind():
    def __init__(self, size):
        self.root = list(range(size))
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootY = self.find(y)
        rootX = self.find(x)
        if rootY != rootX:
            self.root[rootY] = rootX
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        uf = UnionFind(len(graph))

        for v in range(len(graph)):
            rootV = uf.find(v)
            for e in graph[v]:
                rootE = uf.find(e)
                if rootV == rootE:
                    return False
                uf.union(graph[v][0], e)
        return True