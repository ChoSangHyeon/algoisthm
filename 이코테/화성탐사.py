
import heapq

dx = [0, 1]
dy = [1, 0]
import sys



def mars(lst):
    INF = 2**10
    max = []
    for _ in range(len(lst)):
        max.append([INF]*len(lst))
    q = []
    heapq.heappush(q,(lst[0][0],0,0))
    while q:
        cur,x,y = heapq.heappop(q)
        if max[x][y] < cur:
            continue
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(lst[0]):
                continue
            if ny < 0 or ny >= len(lst):
                continue
            if max[nx][ny] > cur + lst[nx][ny]:
                max[nx][ny] = cur + lst[nx][ny]
                heapq.heappush(q,(max[nx][ny],nx,ny))

    return max[-1][-1]


with open('mars.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N = int(input())
        graph = []
        for __ in range(N):
            graph.append(list(map(int, input().split())))

        print(mars(graph))

# input = [[3,7,2,0,1],[2,8,0,9,1],[1,2,1,8,1],[9,8,9,2,0],[3,6,5,1,5]]
#
# print(mars(input))