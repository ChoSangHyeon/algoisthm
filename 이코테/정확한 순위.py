import collections
import sys

a, b = map(int,input().split())
grade = collections.defaultdict(list)
for _ in range(b):
    ai,bi = map(int,sys.stdin.readline().split())
    grade[ai].append(bi)

mapping = [[a+1]*(a+1) for _ in range(a+1)]
for i in range(1,a+1):
    mapping[i][i] = 0
for low,att in grade.items():
    for high in att:
        mapping[low][high] = 1
for x in range(1,a+1):
    for y in range(1, a + 1):
        for z in range(1, a + 1):
            mapping[y][z] = min(mapping[y][z],mapping[y][x]+mapping[x][z])
res = 0
for cur in range(1,a+1):
    cnt = 0
    for node in range(1,a+1):
        if mapping[cur][node] != a+1 or mapping[node][cur] != a+1:
            cnt += 1
    if cnt == a:
        res +=1

print(res)
# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4