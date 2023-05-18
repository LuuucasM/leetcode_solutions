class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        def find(x, root):
            if x != root[x]:
                root[x] = find(root[x], root)
            return root[x]
        def union(x, y, root):
            xroot, yroot = find(x, root), find(y, root)
            if xroot != yroot:
                root[yroot] = xroot
                return 1
            return 0

        root = list(range(n+1))
        removed = bob = alice = 0

        for k, i, j in edges:
            if k == 3:
                if union(i, j, root):
                    alice += 1
                    bob += 1
                else:
                    removed += 1

        roottemp = root[:]

        for k, i, j in edges:
            if k == 1:
                if union(i, j, root):
                    alice += 1
                else:
                    removed += 1

        root = roottemp

        for k, i, j in edges:
            if k == 2:
                if union(i, j, root):
                    bob += 1
                else:
                    removed += 1
        return removed if alice == bob == (n-1) else -1