import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stone_heap = [-x for x in stones]
        heapq.heapify(stone_heap)
        while len(stone_heap):
            if len(stone_heap) == 1:
                return -stone_heap[0]
            new_val = heapq.heappop(stone_heap) - heapq.heappop(stone_heap)
            heapq.heappush(stone_heap, new_val)
        return 0