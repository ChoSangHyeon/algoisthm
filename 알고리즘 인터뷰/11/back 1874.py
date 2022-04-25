import sys

c = int(input())
d = []
e = []
f = 0
flag =0
for _ in range(c):
    k = int(sys.stdin.readline())
    while f <= c:
        if not e:
            f += 1
            e.append(f)
            d.append('+')
        if e[-1] == k:
            e.pop()
            d.append('-')
            break
        elif e[-1] < k:
            f += 1
            e.append(f)
            d.append('+')
        else:
            flag =1
            break
if flag==0:
    for h in d:
        print(h)
else:
    print('NO')


