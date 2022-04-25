def bubblesort(lst):
    index = len(lst) - 1
    for i in range(index):
        wall = index - i
        for a in range(wall):
            if lst[a] > lst[a + 1]:
                lst[a], lst[a + 1] = lst[a + 1], lst[a]
    return lst


def selectionsort(lst):
    ai = len(lst) - 1
    for i in range(ai):
        min = i
        for a in range(i + 1, len(lst)):
            if lst[min] > lst[a]:
                min = a

        if i != min:
            a[i], a[min] = a[min], a[i]
    return lst


def insertionsort(lst):
    index = len(lst)
    for num in range(1, index):
        for i in range(1, num + 1):
            if lst[num - i] > lst[num - i + 1]:
                lst[num - i], lst[num - i + 1] = lst[num - i + 1], lst[num - i]
    return lst


def insertionsort2(lst):
    for num in range(1, len(lst)):
        val = lst[num]
        cmp = num - 1
        while lst[cmp] > val and cmp >= 0:
            lst[cmp + 1] = lst[cmp]
            cmp -= 1
        lst[cmp + 1] = val

    return lst


def quicksort(lst, start, end):
    def partition(lst, ps, pe):
        pivot = lst[pe]
        i = ps - 1
        for j in range(ps, pe):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        lst[i + 1], lst[pe] = lst[pe], lst[i + 1]
        return i + 1

    if start >= end:
        return None

    p = partition(lst, start, end)
    quicksort(lst, start, p - 1)
    quicksort(lst, p + 1, end)
    return lst


def merge(arr1, arr2):
    i, j = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] >= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    while i < len(arr1):
        res.append(arr1[i])
        i += 1
    while j < len(arr2):
        res.append(arr2[j])
        j += 1
    return res

def mergesort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    L = lst[:mid]
    R = lst[mid:]

    return merge(mergesort(L), mergesort(R))


assert insertionsort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert insertionsort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]
