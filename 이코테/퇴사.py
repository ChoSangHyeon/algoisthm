import sys

day = int(input())
sche = []
for _ in range(day):
    sche.append(list(map(int,sys.stdin.readline().split())))

res = []
def manimani(i,sum):
    if i >= day:
        res.append(sum)
        return
    sumM = sche[i][1] + sum
    for j in range(2):
        if j == 1:
            if i + sche[i][0] >day:
                return
            manimani(i + sche[i][0], sumM)
        else:
            manimani(i + 1, sum)

manimani(0,0)
print(max(res))