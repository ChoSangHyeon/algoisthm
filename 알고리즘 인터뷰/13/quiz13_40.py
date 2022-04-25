import collections
import heapq


def networkDelayTime(times:list[list[int]],n:int,k:int):
    q = collections.defaultdict(list)
    for st, ed, dis in times:
        q[st].append([ed, dis])
    hq = []
    heapq.heappush(hq, (0, k))
    dist = collections.defaultdict(int)

    while hq:
        sec, node = heapq.heappop(hq)
        if node not in dist:
            dist[node] = sec
            for v, w in q[node]:
                heapq.heappush(hq, (sec + w, v))
    if len(dist) == n:
        return max(dist.values())
    else:
        return -1

a = [[2,1,1],[2,3,1],[3,4,1]]
print(networkDelayTime(a,4,2))