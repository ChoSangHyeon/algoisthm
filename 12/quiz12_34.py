import collections

def permutation(input:list[int]):
    re = []
    
    def next(a):
        if len(a) == len(input):
            re.append(a)
            return
        aa = input[:]
        sub = [x for x in aa if x not in a]
        for i in sub:
            next(a+[i])
        return
    next([])
    return re




print(permutation([1,2,3,4]))


# a_sub_b = [x for x in a if x not in b]

# a_sub_b = list(set(a) - set(b))
#
# a_sub_b = list(set(a).difference(b))
#
# print(a_sub_b)