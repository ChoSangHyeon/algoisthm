import bisect
import collections
import heapq

N, M = map(int,input().split())
INF = 2**10
a = [INF]* (N+1)
b = collections.defaultdict(list)
for _ in range(M):
    c,d = map(int,input().split())
    b[c].append(d)
    b[d].append(c)
q = []
start = 1
heapq.heappush(q,(0,start))

while q:
    cur, st = heapq.heappop(q)
    for i in b[st]:
        if a[i]< cur:
            continue
        if i == start:
            continue
        if a[i] > cur +1:
            a[i] = cur + 1
            heapq.heappush(q,(a[i],i))

del a[start]
findNum = a[1:]
w = findNum.index(max(findNum))
e = findNum[w]
r = findNum.count(e)
if w >= start:
    w +=2
else:
    w +=1
print(w,e,r)
