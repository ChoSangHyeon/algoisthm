def combi(input,num):
    re = []
    def kk(n,k):
        if k == 0:
            a = sorted(n)
            if not a in re:
                re.append(a)
            return
        na = list(range(1,input+1))
        nb = list(set(na) - set(n))
        for i in nb:
            kk(n+[i],k-1)
        return
    kk([],num)
    return re

print(combi(10,10))