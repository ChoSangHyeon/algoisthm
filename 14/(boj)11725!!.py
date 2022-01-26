import sys
import collections

a = int(input())
main = collections.defaultdict(list)
free = [-1]*(a+1)
q = collections.deque()
q.append(1)

for _ in range(a-1):
    b,c = map(int,sys.stdin.readline().split())
    main[b].append(c)
    main[c].append(b)
while q:
    temp = q.popleft()
    for i in main[temp]:
        if free[i] == -1:
            free[i] = temp
            q.append(i)


for i in free[2:]:
    print(i)

