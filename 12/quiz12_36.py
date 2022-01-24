# Chapter12_36. 조합의 합 (351p)
# 난이도 : ★★
# Leet code Num. : 39

# 숫자 집합 candidates 조합하여 합이 target이 되는 원소는 나열하라. 각 원소는 중복으로 나열 가능하다.
# 예제 1.
# 입력 >> candidates = [2, 3, 6, 7], target = 7
# 출력 >> [[7], [2, 2, 3]]
# 예제 2.
# 입력 >> candidates = [2, 3, 5], target = 8
# 출력 >> [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
def con(input,num):
    res = []
    def plus(x):
        if x:
            if sum(x) >= num:
                if sum(x) == num:
                    res.append(x)
                    return
                else:
                    return

        for i in input:
            if len(x) == 0 or x[-1] <= i:
                plus(x + [i])
    plus([])
    return res

print(con([2,3,4],7))

# def combinationSum(candidates: List[int], target: int):
#     result = []
#     sum = 0
#
#     def dfs(sum, index, path):
#         if sum > target:
#             return
#         if sum == target:
#             print(path)
#             only = path.sort()
#             print("sorted :", path)
#             result.append(path)
#             return
#          인덱스 추가해서 이미 더한값으 더 더하지않음
#         for i in range(index, len(candidates)):
#             sum += candidates[i]
#             dfs(sum, i, path + [candidates[i]])
#             sum -= candidates[i]
#     dfs(sum, 0, [])
#     result
#     return result


#
# def combinationSum( candidates: List[int], target: int) -> List[List[int]]:
#     ans = []
#     candidates.sort()
#
#     def bt(candidate, t):
#         if t == 0:
#             ans.append(candidate)
#             return
#
#         for cand in candidates:
#             if t - cand >= 0:
#                 if len(candidate) == 0 or candidate[-1] <= cand:
#                     next_candidate = candidate[:] + [cand]
#                     bt(next_candidate, t - cand)
#
#     bt([], target)
#     return ans



# def combinationSum( candidates: List[int], target: int) -> List[List[int]]:
#     candidates = sorted(candidates)
#     q = []
#     out = []
#     for i, e in enumerate(candidates):
#         if e == target:
#             out.append([e])
#         elif e < target:
#             q.append(([i], candidates[i]))
#         else:
#             break
#
#     while q:
#         e, s = q.pop(0)
#         last_idx = e[-1]
#         for i in range(last_idx, len(candidates)):
#             if s + candidates[i] == target:
#                 out.append([candidates[k] for k in e] + [candidates[i]])
#             elif s + candidates[i] < target:
#                 q.append((e + [i], s + candidates[i]))
#     return out