import collections
import heapq
import sys


def cheapest(n:int,flights:list[list[int]],src:int,dst:int,k:int):
    q = collections.defaultdict(list)
    # weight = [(sys.maxsize,k)] * n
    for st, ed, money in flights:
        q[st].append([ed, money])
    hq = [(0, src, k)]
    print(q)
    while hq:
        much, name, cango = heapq.heappop(hq)
        if name == dst:
            return much
        if cango >= 0:
            for end, muny in q[name]:
                summ = muny + much
                # if summ < weight[end][0] or k -1 >= weight[end][1]:
                # weight[end] = (summ,k-1)
                heapq.heappush(hq, (summ, end, cango - 1))
    return -1

print(cheapest(4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,3,1))


def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    d = collections.defaultdict(list)

    for fro, to, cost in flights:
        d[fro].append((to, cost))

    visited_cost_dict = {}
    visited_cost_dict[src] = (0, 0)

    hp = [(0, 0, src)]

    while hp:

        price, stops, pit = heapq.heappop(hp)

        if pit == dst:
            return price

        if stops > k:
            continue

        else:
            for otherDst, otherCost in d[pit]:
                if otherDst not in visited_cost_dict or (otherCost + price < visited_cost_dict[otherDst][0]) or (
                        stops + 1 < visited_cost_dict[otherDst][1]):
                    visited_cost_dict[otherDst] = (otherCost + price, stops + 1)
                    heapq.heappush(hp, (otherCost + price, stops + 1, otherDst))

    return -1


from collections import defaultdict
import heapq

INF = float('inf')


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(dict)
        for f, t, p in flights:
            adj[f][t] = p

        stop = [INF] * n
        heap = [(0, 0, src)]

        while heap:
            current_price, current_stop, current_node = heapq.heappop(heap)

            if current_node == dst:
                return current_price
            if current_stop == k + 1 or current_stop >= stop[current_node]:
                continue

            stop[current_node] = current_stop

            for c, p in adj[current_node].items():
                heapq.heappush(heap, (current_price + p, current_stop + 1, c))

        return -1