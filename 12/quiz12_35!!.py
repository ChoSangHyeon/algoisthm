# def combi(input,num):
#     re = []
#     def kk(n,k):
#         if k == 0:
#             a = sorted(n)
#             if not a in re:
#                 re.append(a)
#             return
#         na = list(range(1,input+1))
#         nb = list(set(na) - set(n))
#         for i in nb:
#             kk(n+[i],k-1)
#         return
#     kk([],num)
#     return re
#
# print(combi(10,10))
#





def combine(n: int, k: int):
    results = []

    def dfs(elements, start: int, k: int):
        if k == 0:
            results.append(elements[:])
            return

        # 자신 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return results

print(combine(5,3))

# import itertools
# from typing import List
#
#
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         return list(itertools.combinations(range(1, n + 1), k))