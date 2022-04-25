import sys
n = int(sys.stdin.readline())
main = [-1] * 15
cnt = 0
visited = [False for _ in range(n)]
def isOk(thatRow):
    for i in range(thatRow):
        if main[i] == main[thatRow] or thatRow - i == abs(main[thatRow]-main[i]):
            return False
    return True
def dfs(row):
    if row >= n:
        global cnt
        cnt += 1
        return
    for i in range(n):
        if visited[i]:
            continue
        main[row] = i
        if isOk(row):
            visited[i]= True
            dfs(row +1)
            visited[i]=False
dfs(0)

print(cnt)
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


# def backTracking(rowPos):
#     global answer
#
#     # 퀸을 모두 배치했다면 끝
#     if rowPos == n:
#         answer += 1
#         return
#
#     for col in range(n):
#         flag = True
#         # 이전 행들에 대해서
#         for row in range(rowPos):
#             # 같은 열에 위치해있거나 대각선에 퀸이 이미 존재한다면 가지치기
#             if queenLocation[row] == col or rowPos - row == abs(col - queenLocation[row]):
#                 flag = False
#                 break
#         if flag:
#             queenLocation[rowPos] = col
#             backTracking(rowPos + 1)
#
#
# n = int(input())
# answer = 0
# # 각 row마다 queen이 위치하는 인덱스를 저장하는 리스트
# queenLocation = [0] * n
# backTracking(0)
# print(answer)
