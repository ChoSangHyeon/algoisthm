import sys
a,b = map(int,input().split())
dic = {}
for _ in range(a):
    c,d = sys.stdin.readline().split()
    dic[c]=d
for _ in range(b):
    e = sys.stdin.readline().strip('\n')
    print(dic[e])
