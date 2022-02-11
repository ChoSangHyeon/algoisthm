import bisect


def how_many(lst: list[int], target: int):
    a = bisect.bisect_left(lst, target)
    b = bisect.bisect_right(lst, target)
    if a < len(lst) and lst[a] == target:
        return b - a
    else:
        return -1

a = [1,1,2,2,2,3]
b = 1
print(how_many(a,b))