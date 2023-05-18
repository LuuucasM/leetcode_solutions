import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.currentmin = 1
        self.minset = []

    def popSmallest(self) -> int:
        if len(self.minset):
            ans = heapq.heappop(self.minset)
        else:
            ans = self.currentmin
            self.currentmin += 1
        return ans

    def addBack(self, num: int) -> None:
        if num < self.currentmin and num not in self.minset:
            heapq.heappush(self.minset, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)