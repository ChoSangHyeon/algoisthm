# Chapter12_37. 부분 집합 (355p)
# 난이도 : ★★
# Leet code Num. : 78

# 모든 부분
# 예제 1.
# 입력 >> nums = [1, 2, 3]
# 출력 >> [[3], [1], [2], [1,2,3], [1, 3], [2, 3], [1, 2], []]

def boobun(input):
    res = []
    input.sort()
    def zip(x):
        if x:
            res.append(x)
        if len(x) == len(input):
            return
        for i in input:
            if len(x)==0 or x[-1]<i:
                zip(x+[i])
    zip([])
    res.append([])
    return res

print(boobun([1,2,3]))