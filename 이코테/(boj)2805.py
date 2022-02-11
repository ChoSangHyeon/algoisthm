import sys
def tree(lst, total):
    lst.sort()
    st = 0
    ed = lst[-1]
    if total == 0:
        return 0
    while st <= ed:
        sum = 0
        mid = (st + ed) // 2
        for i in lst:
            if i >= mid:
                sum += i - mid

        if sum < total:
            ed = mid -1

        if sum >= total:
            givemax = mid
            st = mid + 1
    return givemax

a,b = map(int,input().split())
c = list(map(int,sys.stdin.readline().split()))
print(tree(c,b))