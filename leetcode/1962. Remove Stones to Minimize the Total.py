import math
import heapq
class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        # max_heapq = []
        # for i in range(len(piles)):
        #     heapq.heappush(max_heapq,-piles[i])
        # for _ in range(k):
        #     temp = heapq.heappop(max_heapq)
        #     heapq.heappush(max_heapq,math.floor(temp/2))
        # return -sum(max_heapq)

        piles = [-x for x in piles]
        heapify(piles)
        for _ in range(k): heapreplace(piles, piles[0]//2)
        return -sum(piles)
