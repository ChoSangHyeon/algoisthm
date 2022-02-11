def find_pix(lst:list[int]):
    st,ed = 0,len(lst)-1
    while st <= ed:
        mid = (st+ed)//2
        if lst[mid] > mid:
            ed = mid-1
        elif lst[mid] < mid:
            st = mid+1
        else:
            return mid
    return -1

a = [-15,-4,2,8,9,13,15]
print(find_pix(a))