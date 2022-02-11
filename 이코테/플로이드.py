import sys

INF = 10 ** 10

n = int(sys.stdin.readline())
M = int(sys.stdin.readline())
dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if c < dist[a][b]:
        dist[a][b] = c

for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(1, n + 1):
            dist[b][c] = min(dist[b][c], dist[b][a] + dist[a][c])
            for e in dist:
                print(e)


for row in dist[1:]:
    print(' '.join([str(el) if el != INF else '0' for el in row[1:]]))