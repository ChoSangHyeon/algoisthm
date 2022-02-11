import sys


def money(lst, total):
    lst.sort()
    st = 0
    ed = lst[-1]
    while st <= ed:
        sum = 0
        mid = (st + ed) // 2
        for i in lst:
            if i >= mid:
                sum += mid
            else:
                sum += i
        if sum <= total:
            givemax = mid
            st = mid + 1
        if sum > total:
            ed = mid - 1

    return givemax

a = [70,80,30,40,100]

print(money(a,450))

a = int(input())
b = list(map(int,sys.stdin.readline().split()))
c = int(input())

# 입력값의 범위가 터무니없이 크다 ! 이진탐색