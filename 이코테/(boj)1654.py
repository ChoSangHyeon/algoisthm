import sys


def cut_lan(lst: list[int], num):
    lst.sort()
    st = 1
    ed = lst[-1]
    while st <= ed:
        mid = (st + ed) // 2
        cnt = 0
        for i in lst:
            ct = i // mid
            cnt += ct

        if cnt >= num:
            st = mid + 1
            length = mid
        else:
            ed = mid - 1
    return length


a,b = map(int,input().split())
c = []
for _ in range(a):
    c.append(int(sys.stdin.readline()))
print(cut_lan(c,b))