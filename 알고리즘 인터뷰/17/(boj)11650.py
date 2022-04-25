import sys

a = int(input())
d = []
for _ in range(a):
    b,c = map(int,sys.stdin.readline().split())
    d.append([b,c])
d.sort(key=lambda x : (x[0],x[1]))
for i in d:
    print(*i)