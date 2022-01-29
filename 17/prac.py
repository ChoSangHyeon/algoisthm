def bubblesort(lst):
    ai = len(lst)-1
    for i in range(ai):
        ia = ai - i
        for a in range(ia):
            if lst[a] > lst[a+1]:
                lst[a],lst[a+1] = lst[a+1],lst[a]
    return lst

def selectionsort(lst):
    ai = len(lst)-1
    for i in range(ai):
        min = i
        for a in range(i+1,len(lst)):
            if lst[min] > lst[a]:
                min = a

        if i != min:
            a[i],a[min] = a[min],a[i]
    return lst

def insertionsort(lst):
    index = len(lst)
    for num in range(1,index):
        for i in range(1,num+1):
            if lst[num-i] > lst[num-i+1]:
                lst[num - i], lst[num - i + 1] = lst[num-i+1],lst[num-i]
    return lst

def insertionsort2(lst):
    

    return lst
assert insertionsort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert insertionsort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]