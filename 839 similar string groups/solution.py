class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.group_count = size

    def find(self, x):
        return self.root[x]
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root = [rootX if i == rootY else i for i in self.root]
            self.group_count -= 1
    def num_groups(self):
        return self.group_count

def is_similar(str1, str2):
    diff = sum(1 for a, b in zip(str1, str2) if a != b)
    return (diff == 0 or diff == 2)

class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        uf = UnionFind(len(strs))
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if is_similar(strs[i], strs[j]):
                    uf.union(i, j)