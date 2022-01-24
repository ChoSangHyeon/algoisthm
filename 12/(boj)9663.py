n = int(input())
def nqueen(n):
    main = [-1] * n
    main1 = [[-1] * n for _ in range(n)]
    input = list(range(n))
    cnt = 0
    res = []
    def isOk(thatRow,i):
        for a in range(thatRow):
            if thatRow - a == abs(main[a] - main[thatRow]):
                input.append(i)
                input.sort()
                return False
        return True
    def dfs(row):
        if row >= n:
            nonlocal cnt
            cnt += 1
            grid = [['.'] * n for _ in range(n)]
            u = []
            for a,b in enumerate(main):
                grid[a][b] ='Q'
            for c in grid:
                u.append(''.join(c))
            res.append(u)
            return
        for i in input:
            main[row] = i
            input.remove(i)
            if isOk(row,i):
                for j in range(n):
                    main1[j] = 
                dfs(row +1)
            if not i in input:
                input.append(i)
                input.sort()
    dfs(0)
    return cnt
print(nqueen(n))
# def nqueen(n):
#     visited = [-1] * n
#     cnt = 0
#     answers = []
#
#     def is_ok_on(nth_row):
#         for row in range(nth_row):
#            if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
#                 return False
#         return True
#
#     def dfs(row):
#       if row >= n:
#             # nonlocal 은 지역변수가 아님을 의미한다.
#             nonlocal cnt
#             cnt += 1
#             print("*" * 80)
#             print(f"{cnt}번째 답 - visited: {visited}")
#             grid = [['.'] * n for _ in range(n)]
#             for idx, value in enumerate(visited):
#                 grid[idx][value] = 'Q'
#             result = []
#             for row in grid:
#                 print(row)
#                 result.append(''.join(row))
#             answers.append(result)
#             return
#
#
#         for col in range(n):
#            visited[row] = col
#             if is_ok_on(row):
#                 dfs(row + 1)
#
#     dfs(0)
#     return answers
#
# assert nqueen(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]

