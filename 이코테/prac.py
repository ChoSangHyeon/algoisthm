# def solution(triangle):
#     res = [[-1]*(i+1) for i in range(len(triangle))]
#     res[0][0] = triangle[0][0]
#     def check(r,c):
#         if r < 0 or c < 0 or c > r:
#             return 0
#         if res[r][c] != -1:
#             return res[r][c]
#         res[r][c] = max(check(r - 1, c - 1), check(r - 1, c)) + triangle[r][c]
#         return res[r][c]
#
#     for i in range(len(triangle[-1])):
#         check(len(triangle[-1])-1,i)
#
#     answer = max(res[len(triangle[-1])-1])
#     return answer
#
# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
import heapq


def solution(n, times):
    st = 0
    ed = max(times) * n
    while st <= ed:
        mid = (st+ed) //2
        cnt = 0
        for time in times:
            cnt += mid // time
        if cnt >= n:
            min_gap = mid
            ed = mid -1
        else:
            st = mid +1

    return min_gap